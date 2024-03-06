from .base import Base
from model import model_dict
from config import EnumerateData, Config
from response import ExcelResponse
from sqlalchemy.sql import func, distinct
from config import StaticData, EnumerateData


class EvidenceRate(Base):
    methods = ['get']
    model_name = "settle_data"
    allowed_parameter = {
        "GET": {'year': ("enum", None, '', True, None), 'compare_year': ("enum", None, '', True, None),
                "person_type": ("enum", None, 'settle_data', False, None),
                "cure_type": ("enum", None, 'settle_data', False, None),
                "year_settle_date": ("combine_date", None, 'settle_data', False, None),
                "compare_year_settle_date": ("combine_date", None, 'settle_data', False, None),
                'is_refund': ('bool', None, 'settle_data', False, None),
                'is_valid': ('bool', None, 'settle_data', False, None), "hospital_place": ("enum", None, 'settle_data', False, None), "hospital_id": ('list', None, "settle_data", False, None),
                "hospital_name": ('str', None, "settle_data", False, 80)
                }
    }
    fuzzy_field = ('hospital_name', )

    def make_get_query(self):
        settle_date_dict = {}
        for year_key in ('compare_year', 'year'):
            settle_date_dict[year_key] = self.parameter_dict[self.model_name].pop(f'{year_key}_settle_date', None)
        for year_key in ('compare_year', 'year'):
            year = self.parameter_dict.get(year_key, Config.DEFAULT_YEAR)
            self.parameter_dict[self.model_name]['settle_date'] = settle_date_dict[year_key]
            self.model = model_dict[f'{self.model_name}_{year}']
            self.query = self.model.query
            self.query = self.query.with_entities(self.model.hospital_name, self.model.evidence_type, func.count(self.model.id).label('time_count')).group_by(self.model.hospital_name, self.model.evidence_type)
            super().make_get_query()
            self.query_list.append((year_key, self.query))

    def clean_get_response(self):
        self.response_data = []
        data_group_dict = {}
        for query_group in self.query_list:
            year_key, query = query_group
            for hospital_name, evidence_type, time_count in query.all():
                data_group_dict.setdefault(hospital_name, {}).setdefault(year_key, {})[evidence_type] = time_count
        sum_dict = {'number': '', 'hospital_name': '合计', 'compare_year_sum_count': 0, 'compare_year_evidence_count': 0, 'compare_year_evidence_rate': 0, 'year_sum_count': 0, 'year_evidence_count': 0, 'year_evidence_rate': 0}
        for hospital_name, data_dict in data_group_dict.items():
            response_group = {'number': '', 'hospital_name': hospital_name, }
            for year_key in ('compare_year', 'year'):
                data = data_dict.get(year_key, {})
                evidence_count = data.get('医保电子凭证', 0)
                sum_count = sum(data.values())
                evidence_rate = (evidence_count / sum_count) if sum_count else 0
                response_group[f'{year_key}_sum_count'] = sum_count
                response_group[f'{year_key}_evidence_count'] = evidence_count
                sum_dict[f'{year_key}_sum_count'] += sum_count
                sum_dict[f'{year_key}_evidence_count'] += evidence_count
                response_group[f'{year_key}_evidence_rate'] = evidence_rate
            response_group[f'increase_evidence_rate'] = response_group[f'year_evidence_rate'] - response_group[f'compare_year_evidence_rate']
            self.response_data.append(response_group)
        sum_dict['compare_year_evidence_rate'] = (sum_dict['compare_year_evidence_count'] / sum_dict['compare_year_sum_count']) if sum_dict['compare_year_sum_count'] else 0
        sum_dict['year_evidence_rate'] = (sum_dict['year_evidence_count'] / sum_dict['year_sum_count']) if sum_dict['year_sum_count'] else 0
        sum_dict['increase_evidence_rate'] = sum_dict['year_evidence_rate'] - sum_dict['compare_year_evidence_rate']
        self.response_data.sort(key=lambda x:x['year_evidence_rate'], reverse=True)
        self.response_data.append(sum_dict)
        for data_index, data_dict in enumerate(self.response_data, 1):
            data_dict['number'] = data_index
            data_dict['compare_year_evidence_rate'] = self.to_percent(data_dict['compare_year_evidence_rate'])
            data_dict['year_evidence_rate'] = self.to_percent(data_dict['year_evidence_rate'])
            data_dict['increase_evidence_rate'] = self.to_percent(data_dict['increase_evidence_rate'])


class EvidenceRateDownload(EvidenceRate):
    response_type_dict = {'GET': ExcelResponse}

    def clean_get_response(self):
        super().clean_get_response()
        self.response_data = (tuple(i.values()) for i in self.response_data)
        self.extra_response_data = ['序号', '定点医药机构名称', '总结算人次', '医保电子凭证结算人次', '医保电子凭证结算率', '总结算人次', '医保电子凭证结算人次', '医保电子凭证结算率', '增长率']