from .base import BaseList
from response import ExcelResponse
from sqlalchemy.sql import func
from sqlalchemy import or_

class OpenDataList(BaseList):

    methods = ['get']
    model_name = 'settle_data'
    allowed_parameter = {'GET': {'year': ("enum", None, '', True, None), "person_type": ("enum", None, 'settle_data', False, None), "settle_date": ("combine_date", None, 'settle_data', False, None), 'is_refund': ('bool', None, 'settle_data', False, None), 'is_valid': ('bool', None, 'settle_data', False, None)}}
    response_type_dict = {'GET': ExcelResponse}
    is_page = False

class OpenDataHospitalListDownload(OpenDataList):

    def make_get_query(self):
        self.query = self.query.with_entities(func.count(self.model.id).label('data_count'), func.sum(self.model.rescue_pay).label('rescue_pay'), self.model.hospital_name).filter(self.model.rescue_pay>0).group_by(self.model.hospital_name)
        super().make_get_query()

    def clean_get_response(self):
        super().clean_get_response()
        self.response_data = (tuple(i.values()) for i in self.response_data)
        self.extra_response_data = ['序号', '人次', '民政医疗救助基金支付', '机构名称']

class OpenDataPayListDownload(OpenDataList):

    decimal_field_list = ('overall_pay', 'big_pay', 'rescue_pay', 'other_pay')

    def make_get_query(self):
        self.query = self.query.with_entities(self.model.self_number, *(func.sum(getattr(self.model, i)).label(i) for i in self.decimal_field_list)).filter(or_(getattr(self.model, i)>0 for i in self.decimal_field_list)).group_by(self.model.self_number)
        super().make_get_query()

    def clean_get_response(self):
        super().clean_get_response()
        for data in self.response_data:
            data['self_number'] = data['self_number'][:-4] + '****'
        self.response_data = (tuple(i.values()) for i in self.response_data)
        self.extra_response_data = ['序号', '个人编号', '统筹基金支出', '大病保险支出', '医疗救助支出', '其他基金支付']

class OpenDataRescueListDownload(OpenDataList):

    def make_get_query(self):
        self.query = self.query.with_entities(self.model.name, self.model.self_number, func.sum(self.model.rescue_pay).label('rescue_pay')).filter(self.model.rescue_pay>0).group_by(self.model.name, self.model.self_number)
        super().make_get_query()

    def clean_get_response(self):
        super().clean_get_response()
        for data in self.response_data:
            data['name'] = data['name'][1] + '**'
            data['self_number'] = data['self_number'][:-4] + '****'
        self.response_data = (tuple(i.values()) for i in self.response_data)
        self.extra_response_data = ['序号', '姓名', '个人编号', '医疗救助金额']