from .base import Base
from flask import session

class InsuredData(Base):

    methods = ['get']
    model_name = "insured_data"
    authority_name = "insured_data_list"
    allowed_parameter = {
        "GET": {'year': ("enum", None), "id_number": (str, 18),"is_insured": (bool, None), "own_expense": ("enum", None), "insured_state": ("enum", None),
                "insured_area": ("enum", None), "attribute": ("enum", None),"second_attribute": ("enum", None), "poverty_state": ("enum", None),
                "town": ("enum", None), "village": ("enum", None), "page": (int, None)},
    }

    def get(self, user_id):
        self.authentication(user_id, self.authority_name)
        return super().get()

