from config import EnumerateData as ED
from .base import Base

class EnumerateData(Base):
    allowed_parameter = {"GET": {
            "enumerate_field": ("enum", None, '', True, None)}}
    is_authentication = False
    is_year = False

    def make_get_query(self):
        pass

    def clean_get_response(self):
        enumerate_field = self.parameter_dict["enumerate_field"]
        if isinstance(enumerate_field, str):
            enumerate_field = [enumerate_field]
        for key in enumerate_field:
            self.response_data[key] = getattr(ED, key)
