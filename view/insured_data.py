from .base import BaseList, Base
from flask import session
from response import ExcelResponse, OK
from config import EnumerateData
from sqlalchemy.sql import func

class InsuredData(Base):

    methods = ['get']
    model_name = "insured_data"
    allowed_parameter = {
        "GET": {'year': ("enum", None), 'name': (str, 20), "id_number": (str, 18), "is_insured": (bool, None),
                "own_expense": ("enum", None), "pay_date": ("date", None),
                "insured_state": ("enum", None), "attribute": ("enum", 'or_'), "second_attribute": ("enum", 'or_'),
                "poverty_state": ("enum", 'or_'),
                "town": ("enum", None), "village": ("enum", None), "page": (int, None)},
    }


class InsuredDataList(InsuredData, BaseList):

    pass

class InsuredDataStatistic(InsuredData):

    def make_response(self):
        own_expense_standard = EnumerateData.own_expense_standard_dict[self.year]
        self.query = self.query.with_entities(func.count(self.model.id), self.model.own_expense)
        self.parameter_dict.pop('page', None)
        super().make_response()
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
        self.response = OK(result_dict)



class InsuredDataListDownload(InsuredDataList):

    is_page = False
    response_type = 'list_response'

    def make_response(self):
        super().make_response()
        self.response_data.insert(0, ['序号', 'id', '姓名', '身份证号', '自付金额', '支付日期', '参保情况', '人员属性', '其他属性', '贫困状态', '乡镇', '村', '手机号', '备注'])
        self.response = ExcelResponse(self.response_data)

class InsuredDataStatisticDownload(InsuredDataStatistic):

    def make_response(self):
        super().make_response()
        data_group_list = [['总（人）', '参加居民医保（人）', '未参加居民医保（人）', '享受参保资助（人）', '自付金额（元）', '资助金额（元）']]
        data_group_list.append([*self.response_data.values()])
        self.response = ExcelResponse(data_group_list)