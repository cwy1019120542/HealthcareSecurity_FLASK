from .base import Base
from model import model_dict
from flask import session
from sqlalchemy.sql import func, distinct
from response import OK

class SettleDataStatistic(Base):

    methods = ['get']
    authority_name = "settle_data_statistic"
    allowed_parameter = {
        "GET": {
            'year': ("enum", None), "person_type": ("enum", None), "pay_place": ("enum", None), "hospital_level": ("enum", None),
            "evidence_type": ("enum", None), "cure_type": ("enum", None), "settle_date": ("date", None),
            "attribute": ("enum", None), "second_attribute": ("enum", None), "poverty_state": ("enum", None), "town": ("enum", None), "village": ("enum", None)
        }
    }

    def get(self, user_id):
        self.authentication(user_id, self.authority_name)
        parameter_dict = self.filter_parameter()
        year = parameter_dict.pop('year')
        model = model_dict[f'settle_data_{year}']
        query = model.query.with_entities(func.count(model.id), func.count(distinct(model.id_number)), func.sum(model.all_expense), func.sum(model.inner_expense), func.sum(model.overall_pay), func.sum(model.large_pay), func.sum(model.big_pay), func.sum(model.rescue_pay),
                                                func.sum(model.civil_pay), func.sum(model.other_pay), func.sum(model.all_pay), func.sum(model.cash_pay), func.sum(model.account_pay), func.sum(model.together_pay))
        query = self.model_query(model, parameter_dict, query)
        result = query.first()
        result_dict = {}
        for key, value in zip(['time_count', 'number_count', 'all_expense', 'inner_expense', 'overall_pay', 'large_pay', 'big_pay', 'rescue_pay', 'civil_pay', 'other_pay', 'all_pay', 'cash_pay', 'account_pay', 'together_pay'], result):
            if not value:
                value = 0
            if key in ['time_count', 'number_count']:
                result_dict[key] = value
            else:
                result_dict[key] = round(float(value), 2)
        return OK(result_dict)