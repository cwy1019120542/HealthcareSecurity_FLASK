from .base import BaseList
from flask import session

class InsuredDataList(BaseList):

    methods = ['get']
    model_name = "insured_data"
    allowed_parameter = {
        "GET": {'year': ("enum", None), 'name': (str, 20), "id_number": (str, 18),"is_insured": (bool, None), "own_expense": ("enum", None), "pay_date": ("date", None),
                "insured_state": ("enum", None), "attribute": ("enum", 'or_'),"second_attribute": ("enum", 'or_'), "poverty_state": ("enum", 'or_'),
                "town": ("enum", None), "village": ("enum", None), "page": (int, None)},
    }

