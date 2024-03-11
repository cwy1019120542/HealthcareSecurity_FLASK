import os
from .base import BaseList, Base, Attachment
from flask import session
from config import Config
from response import ExcelResponse, OK
from sqlalchemy.sql import func, distinct

class ChronicIllness(Base):

    methods = ['get']
    model_name = "chronic_illness"
    join_model_name = 'person'
    is_year = False
    entities_dict = {'model': ['id_number', 'illness_name', 'illness_number', 'start_date', 'end_date', 'hospital_id', 'hospital_name', 'hospital_place', 'person_type_simple', 'illness_type', 'identify_date', 'apply_date', 'operator', 'operate_date', 'is_valid', 'apply_source'], 'join_model': ['name', 'civil_attribute', 'poverty_state', 'orphan_attribute', 'disable_attribute', 'treat_attribute', 'accident_attribute', 'town', 'village', 'phone_number', 'family_number']}
    allowed_parameter = {
        "GET": {
            "id_number": ('str', None, 'person', False, 18), "family_number": ('str', None, 'person', False, 20), 'name': ('str', None, "person", False, 20),
            "civil_attribute": ("enum", 'or_', "person", False, None), "orphan_attribute": ("enum", 'or_', "person", False, None), "disable_attribute": ("enum", 'or_', "person", False, None), "treat_attribute": ("enum", 'or_', "person", False, None),
            "accident_attribute": ("enum", 'or_', "person", False, None), "poverty_state": ("enum", 'or_', "person", False, None), "town": ("enum", None, "person", False, None), "village": ("enum", None, "person", False, None),
            "page": ('int', None, '', False, None), "birthday": ('combine_date', None, 'person', False, None), "limit": ('int', None, '', False, 1000), 'illness_name': ('str', None, "chronic_illness", False, 20), "person_type_simple": ("enum", None, 'chronic_illness', False, None), "hospital_place": ("enum", None, 'chronic_illness', False, None),
            'is_valid': ('bool', None, 'chronic_illness', False, None), 'apply_source': ("enum", None, 'chronic_illness', False, None), 'illness_type': ("enum", None, 'chronic_illness', False, None), 'operate_date': ("combine_date", None, 'chronic_illness', False, None), "hospital_name": ('str', None, "chronic_illness", False, 80)}
    }
    fuzzy_field = ('name', 'illness_name', 'hospital_name')

class ChronicIllnessList(BaseList, ChronicIllness):

    def clean_get_response(self):
        super().clean_get_response()
        for data_group in self.response_data:
            for key in ('start_date', 'end_date', 'identify_date', 'apply_date'):
                data_group[key] = self.to_string_date(data_group[key], False)
            data_group['operate_date'] = self.to_string_date(data_group['operate_date'])
            data_group['attribute'] = self.merge_attribute(data_group)
            data_group['is_valid'] = self.bool_to_string(data_group['is_valid'])

class ChronicIllnessStatistic(ChronicIllness):

    def make_get_query(self):
        self.query = self.query.with_entities(func.count(self.model.id).label('time_count'), func.count(distinct(self.model.id_number)).label('number_count'))
        super().make_get_query()

    def clean_get_response(self):
        result = self.query.first()
        for key in result.keys():
            self.response_data[key] = getattr(result, key)

class ChronicIllnessListDownload(ChronicIllnessList):

    is_page = False
    response_type_dict = {'GET': ExcelResponse}

    def clean_get_response(self):
        super().clean_get_response()
        self.response_data = (tuple(i.values()) for i in self.response_data)
        self.extra_response_data = ['序号', '证件号码', '病种名称', '病种编号', '开始日期', '结束日期', '定点医药机构编号', '定点医药机构名称', '医药机构地点类别', '人员类别', '病种类型', '鉴定日期', '申请日期', '经办人', '经办日期', '是否有效', '申报来源', '姓名', '乡镇', '村居', '手机号', '家庭户号', '人员属性']

class ChronicIllnessStatisticDownload(ChronicIllnessStatistic):

    response_type_dict = {'GET': ExcelResponse}

    def clean_get_response(self):
        super().clean_get_response()
        self.response_data = [tuple(self.response_data.values())]
        self.extra_response_data = ['条数', '人数']

class ChronicIllnessCard(Attachment):

    methods = ['get']
    allowed_parameter = {
        'GET': {"id_number": ('str', None, '', True, 18), "town": ("enum", None, "", True, None), "village": ("enum", None, "", True, None)},
    }
    model_name = "chronic_illness"
    method_dict = {"GET": "args"}
    response_type_dict = {'GET': ''}
    base_dir = Config.CHRONIC_ILLNESS_CARD_DIR

    def get_file_path(self):
        return os.path.join(self.base_dir, self.parameter_dict['town'], self.parameter_dict['village']), f'{self.parameter_dict["id_number"]}.pdf'

