from .base import Base, BaseList
from model import model_dict
from flask import session
from sqlalchemy.sql import func, distinct
from response import OK
from config import EnumerateData
from sqlalchemy import or_

class SettleData(Base):

    methods = ['get']
    model_name = "settle_data"
    allowed_parameter = {
        "GET": {
            'year': ("enum", None), 'name': (str, 20), "id_number": (str, 18), "person_type": ("enum", None),
            "pay_place": ("enum", None), "hospital_level": ("enum", None),
            "evidence_type": ("enum", None), "cure_type": ("enum", None), "settle_date": ("date", None),
            "page": (int, None), "pay_exists": ("enum", None),
            "attribute": ("enum", 'or_'), "second_attribute": ("enum", 'or_'), "poverty_state": ("enum", 'or_'),
            "town": ("enum", None), "village": ("enum", None)
        }
    }

    @staticmethod
    def get_deal_dict(pay_exists_list, is_list=True):
        deal_dict = {}
        if not is_list:
            pay_exists_list = [pay_exists_list]
        for pay_exists in pay_exists_list:
            pay_exists_key = EnumerateData.pay_exists_dict[pay_exists]
            deal_dict[f'{pay_exists_key}!'] = 0
        return deal_dict
    
    def deal_pay_exists(self):
        pay_exists_list = self.parameter_dict.pop('pay_exists', None)
        if pay_exists_list:
            if isinstance(pay_exists_list, list):
                self.query = self.query.filter(or_(*self.get_query_parameter(self.get_deal_dict(pay_exists_list))))
            else:
                self.query = self.query.filter(*self.get_query_parameter(self.get_deal_dict(pay_exists_list, False)))


class SettleDataList(BaseList, SettleData):

    def make_response(self):
        self.deal_pay_exists()
        super().make_response()



class SettleDataStatistic(SettleData):

    def make_response(self):
        self.query = self.query.with_entities(func.count(self.model.id), func.count(distinct(self.model.id_number)), func.sum(self.model.all_expense), func.sum(self.model.inner_expense), func.sum(self.model.overall_pay), func.sum(self.model.large_pay), func.sum(self.model.big_pay), func.sum(self.model.rescue_pay),
                                                func.sum(self.model.civil_pay), func.sum(self.model.other_pay), func.sum(self.model.all_pay), func.sum(self.model.cash_pay), func.sum(self.model.account_pay), func.sum(self.model.together_pay))
        self.deal_pay_exists()
        super().make_response()
        result = self.query.first()
        result_dict = {}
        for key, value in zip(
                ['time_count', 'number_count', 'all_expense', 'inner_expense', 'overall_pay', 'large_pay', 'big_pay',
                 'rescue_pay', 'civil_pay', 'other_pay', 'all_pay', 'cash_pay', 'account_pay', 'together_pay'], result):
            if not value:
                value = 0
            if key in ['time_count', 'number_count']:
                result_dict[key] = value
            else:
                result_dict[key] = round(float(value), 2)
        self.response = OK(result_dict)
