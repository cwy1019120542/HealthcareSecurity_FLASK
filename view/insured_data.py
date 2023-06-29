from .base import BaseList, Base
from flask import session
from response import ExcelResponse, OK
from config import StaticData
from sqlalchemy.sql import func

class InsuredData(Base):

    methods = ['get']
    model_name = "insured_data"
    join_model_name = 'person'
    entities_dict = {'model': ['id_number', 'own_expense', 'pay_date', 'insured_state', 'is_civil', 'remark', 'is_account_pay'], 'join_model': ['name', 'civil_attribute', 'poverty_state', 'orphan_attribute', 'disable_attribute', 'treat_attribute', 'accident_attribute', 'town', 'village', 'phone_number', 'family_number']}
    allowed_parameter = {
        "GET": {
            "id_number": ('str', None, 'person', False, 18), "family_number": ('str', None, 'person', False, 20), "pay_type_operator": ("enum", None, 'insured_data', False, None), "own_expense": ('int', None, 'insured_data', False, None), "pay_date": ("combine_date", None, 'insured_data', False, None), "insured_state": ("enum", None, 'insured_data', False, None), "is_civil": ('bool', None, 'insured_data', False, None), "is_account_pay": ('bool', None, 'insured_data', False, None),'name': ('str', None, "person", False, 20),
            "civil_attribute": ("enum", 'or_', "person", False, None), "orphan_attribute": ("enum", 'or_', "person", False, None), "disable_attribute": ("enum", 'or_', "person", False, None), "treat_attribute": ("enum", 'or_', "person", False, None),
            "accident_attribute": ("enum", 'or_', "person", False, None), "poverty_state": ("enum", 'or_', "person", False, None), "town": ("enum", None, "person", False, None), "village": ("enum", None, "person", False, None),'year': ("enum", None, '', True, None),
            "page": ('int', None, '', False, None)}
    }

    def make_get_query(self):
        pay_type_operator = self.parameter_dict.get(self.model_name, {}).pop('pay_type_operator', None)
        own_expense = self.parameter_dict.get(self.model_name, {}).pop('own_expense', None)
        if pay_type_operator and own_expense != None:
            self.query = self.query.filter(getattr(self.model.own_expense, pay_type_operator)(own_expense))
        super().make_get_query()


class InsuredDataList(BaseList, InsuredData):

    def clean_get_response(self):
        super().clean_get_response()
        for data_group in self.response_data:
            data_group['pay_date'] = self.to_string_date(data_group['pay_date'])
            data_group['attribute'] = self.merge_attribute(data_group)
            data_group['is_civil'] = self.bool_to_string(data_group['is_civil'])
            data_group['is_account_pay'] = self.bool_to_string(data_group['is_account_pay'])

class InsuredDataStatistic(InsuredData):

    def make_get_query(self):
        self.query = self.query.with_entities(func.count(self.model.id), self.model.own_expense)
        super().make_get_query()

    def clean_get_response(self):
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

    def clean_get_response(self):
        super().clean_get_response()
        self.response_data = (tuple(i.values()) for i in self.response_data)
        self.extra_response_data = ['序号', '身份证号', '自付金额', '支付日期', '参保情况', '是否参加公务员医疗补助', '备注', '是否共济缴费', '姓名','乡镇', '村', '手机号', '户号', '人员属性']

class InsuredDataStatisticDownload(InsuredDataStatistic):

    response_type_dict = {'GET': ExcelResponse}

    def clean_get_response(self):
        super().clean_get_response()
        self.response_data = [tuple(self.response_data.values())]
        self.extra_response_data = ['总（人）', '参加居民医保（人）', '未参加居民医保（人）', '享受参保资助（人）', '自付金额（元）', '资助金额（元）']