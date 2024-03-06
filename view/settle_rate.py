from .base import Base
from model import model_dict
from config import EnumerateData, Config
from response import ExcelResponse
from sqlalchemy.sql import func, distinct
from config import StaticData, EnumerateData

class SettleRate(Base):
    
    methods = ['get']
    model_name = "settle_data"
    allowed_parameter = {
        "GET": {'year': ("enum", None, '', True, None), 'compare_year': ("enum", None, '', True, None),
            "person_type": ("enum", None, 'settle_data', False, None), "cure_type": ("enum", None, 'settle_data', False, None), "year_settle_date": ("combine_date", None, 'settle_data', False, None), "compare_year_settle_date": ("combine_date", None, 'settle_data', False, None),
            'is_refund': ('bool', None, 'settle_data', False, None), 'is_valid': ('bool', None, 'settle_data', False, None)
        }
    }
    sum_field_list = ['time_count', 'number_count', 'all_expense', 'all_pay']
    fix_field_list = ['hospital_place', 'year', 'settle_type']
    field_dict = dict.fromkeys(fix_field_list, '')
    field_dict.update(dict.fromkeys(sum_field_list, 0))

    def make_get_query(self):
        settle_date_dict = {}
        for year_key in ('compare_year', 'year'):
            settle_date_dict[year_key] = self.parameter_dict[self.model_name].pop(f'{year_key}_settle_date', None)
        for year_key in ('compare_year', 'year'):
            year = self.parameter_dict.get(year_key, Config.DEFAULT_YEAR)
            if settle_date_dict[year_key]:
                self.parameter_dict[self.model_name]['settle_date'] = settle_date_dict[year_key]
            self.model = model_dict[f'{self.model_name}_{year}']
            self.query = self.model.query
            self.query = self.query.with_entities(self.model.hospital_place, self.model.is_centre, func.count(self.model.id).label('time_count'), func.count(distinct(self.model.id_number)).label('number_count'), func.sum(self.model.all_expense).label('all_expense'), func.sum(self.model.all_pay).label('all_pay')).group_by(self.model.hospital_place, self.model.is_centre)
            super().make_get_query()
            self.query_list.append((year_key, self.query))


    def clean_get_response(self):
        self.response_data = []
        data_group_dict = {}
        settle_type_dict = {0: '直接结算', 1: '中心结算'}
        for hospital_place in EnumerateData.hospital_place:
            for year_key in ('compare_year', 'year'):
                for is_centre in (0, 1):
                    data_group_dict.setdefault(hospital_place, {}).setdefault(year_key, {}).setdefault(is_centre,{}).setdefault('hospital_place', hospital_place)
                    data_group_dict[hospital_place][year_key][is_centre]['year'] = self.extra_response_data[year_key]
                    data_group_dict[hospital_place][year_key][is_centre]['settle_type'] = settle_type_dict[is_centre]
                    for field in self.sum_field_list:
                        data_group_dict[hospital_place][year_key][is_centre][field] = 0
        for query_group in self.query_list:
            year_key, query = query_group
            data_list = query.all()
            for data in data_list:
                hospital_place, is_centre, *_ = data
                for field in self.sum_field_list:
                    data_group_dict[hospital_place][year_key][is_centre][field] = self.to_float(getattr(data, field))
        for hospital_place in EnumerateData.hospital_place:
            percent_group_dict = {'compare_year': {}, 'year': {}}
            for year_key in ('compare_year', 'year'):
                all_dict = dict(self.field_dict)
                percent_dict = dict(self.field_dict)
                for is_centre in (0, 1):
                    data_group = data_group_dict[hospital_place][year_key][is_centre]
                    self.response_data.append(data_group)
                    for field in self.sum_field_list:
                        all_dict[field] += data_group[field]
                        all_dict[field] = self.to_float(all_dict[field])
                all_dict['settle_type'] = '合计'
                self.response_data.append(all_dict)
                direct_data = data_group_dict[hospital_place][year_key][0]
                for field in self.sum_field_list:
                    percent = direct_data[field]/all_dict[field]
                    percent_dict[field] = self.to_percent(percent)
                    percent_group_dict[year_key][field] = percent
                percent_dict['settle_type'] = '直接结算占比'
                self.response_data.append(percent_dict)
                if year_key == 'compare_year':
                    self.response_data.append({})
            increase_dict = dict(self.field_dict)
            increase_dict['settle_type'] = '直接结算增长率'
            for field in self.sum_field_list:
                increase_dict[field] = self.to_percent(percent_group_dict['year'][field]-percent_group_dict['compare_year'][field])
            self.response_data.append(increase_dict)

class SettleRateDownload(SettleRate):

    response_type_dict = {'GET': ExcelResponse}

    def clean_get_response(self):
        super().clean_get_response()
        self.response_data = (tuple(i.values()) for i in self.response_data)
        self.extra_response_data = ['医疗机构地点', '年份', '结算类别', '人次', '人数', '总费用（元）', '基金总支付（元）']