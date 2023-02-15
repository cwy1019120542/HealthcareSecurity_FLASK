from .base import Base
from sqlalchemy.sql import func
from config import StaticData

class InsuredRate(Base):

    methods = ['get']
    model_name = "insured_data"
    join_model_name = 'person'
    allowed_parameter = {
        "GET": {
            "pay_date": ("date", None, 'insured_data', False),
            "town": ("enum", None, "person", False), "village": ("enum", None, "person", False),
            'year': ("enum", None, '', True)}
    }

    def make_query(self):
        self.query = self.query.with_entities(self.join_model.town, func.count(self.model.id)).group_by(self.join_model.town)
        super().make_query()

    def clean_response(self):
        result_list = self.query.all()
        self.response_data = []
        for town, data_count in result_list:
            target = StaticData[year][town]
            percent = data_count / target


class InsuredRateMust(Base):

    methods = ['get']
    model_name = "insured_data"
    join_model_name = 'person'
    allowed_parameter = {
        "GET": {
            "pay_date": ("date", None, 'insured_data', False),
            "civil_attribute": ("enum", 'or_', "person", False), "orphan_attribute": ("enum", 'or_', "person", False),
            "disable_attribute": ("enum", 'or_', "person", False), "treat_attribute": ("enum", 'or_', "person", False),
            "accident_attribute": ("enum", 'or_', "person", False), "poverty_state": ("enum", 'or_', "person", False),
            "town": ("enum", None, "person", False), "village": ("enum", None, "person", False),
            'year': ("enum", None, '', True)}
    }

    def make_query(self):
        self.query = self.query.with_entities(self.join_model.town, self.model.insured_state, func.count(self.model.id)).group_by(self.join_model.town, self.model.insured_state)
        super().make_query()

    def clean_response(self):
        result = self.query.all()
        print(result)