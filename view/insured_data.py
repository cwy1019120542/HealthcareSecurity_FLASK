from .base import BaseList, Base
from flask import session
from response import ExcelResponse, OK
from config import StaticData
from sqlalchemy.sql import func

class InsuredData(Base):

    methods = ['get']
    model_name = "insured_data"
    join_model_name = 'person'
    entities_dict = {'model': ['id_number', 'own_expense', 'pay_date', 'insured_state', 'is_civil', 'remark', 'is_account_pay'], 'join_model': ['name', 'civil_attribute', 'poverty_state', 'orphan_attribute', 'disable_attribute', 'treat_attribute', 'accident_attribute', 'town', 'village', 'phone_number']}
    allowed_parameter = {
        "GET": {
            "id_number": (str, 18, 'person', False), "own_expense": (int, None, 'insured_data', False), "pay_date": ("date", None, 'insured_data', False), "insured_state": ("enum", None, 'insured_data', False), "is_civil": (bool, None, 'insured_data', False), "is_account_pay": (bool, None, 'insured_data', False),'name': (str, 20, "person", False),
            "civil_attribute": ("enum", 'or_', "person", False), "orphan_attribute": ("enum", 'or_', "person", False), "disable_attribute": ("enum", 'or_', "person", False), "treat_attribute": ("enum", 'or_', "person", False),
            "accident_attribute": ("enum", 'or_', "person", False), "poverty_state": ("enum", 'or_', "person", False), "town": ("enum", None, "person", False), "village": ("enum", None, "person", False),'year': ("enum", None, '', True),
            "page": (int, None, '', False)}
    }

class InsuredDataList(BaseList, InsuredData):

    def clean_response(self):
        super().clean_response()
        for data_group in self.response_data:
            data_group['pay_date'] = self.to_string_date(data_group['pay_date'])
            data_group['attribute'] = self.merge_attribute(data_group)
            data_group['is_civil'] = self.bool_to_string(data_group['is_civil'])
            data_group['is_account_pay'] = self.bool_to_string(data_group['is_account_pay'])

class InsuredDataStatistic(InsuredData):

    def make_query(self):
        self.query = self.query.with_entities(func.count(self.model.id), self.model.own_expense)
        super().make_query()

    def clean_response(self):
        own_expense_standard = StaticData.own_expense_standard_dict[self.year]
        result_list = self.query.group_by(self.model.own_expense).all()
        result_dict = {'all_count': 0, 'insured_count':0, 'not_insured_count': 0, 'perk_count': 0, 'own_expense': 0, 'perk': 0}
        for result in result_list:
            result_count, result_own_expense = result
            result_dict['all_count'] += result_count
            if result_own_expense == None:
                result_dict['not_insured_count'] += result_count
                continue
            result_dict['insured_count'] += result_count
            result_dict['own_expense'] += result_own_expense * result_count
            if own_expense_standard > result_own_expense:
                result_dict['perk_count'] += result_count
                result_dict['perk'] += (own_expense_standard-result_own_expense) * result_count
        self.response_data = result_dict

class InsuredDataListDownload(InsuredDataList):

    is_page = False
    response_type_dict = {'GET': ExcelResponse}

    def clean_response(self):
        super().clean_response()
        self.response_data = (tuple(i.values()) for i in self.response_data)
        self.extra_response_data = ['序号', '身份证号', '自付金额', '支付日期', '参保情况', '是否参加公务员医疗补助', '备注', '是否共济缴费', '姓名','乡镇', '村', '手机号', '人员属性']

class InsuredDataStatisticDownload(InsuredDataStatistic):

    response_type_dict = {'GET': ExcelResponse}

    def clean_response(self):
        super().clean_response()
        self.response_data = [tuple(self.response_data.values())]
        self.extra_response_data = ['总（人）', '参加居民医保（人）', '未参加居民医保（人）', '享受参保资助（人）', '自付金额（元）', '资助金额（元）']