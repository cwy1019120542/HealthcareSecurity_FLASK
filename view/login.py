from .base import Base
from flask import session, abort
from model import model_dict
from response import OK

class Login(Base):

    methods = ['post']
    model_name = "user"
    allowed_parameter = {
        "POST": {
            "phone_number": (str, 20), "password": (str, 20)
        }
    }
    is_year = False
    is_authentication = False

    def make_response(self):
        super().make_response()
        user = self.query.first()
        if not user or not user.is_available:
            abort(401)
        data = user.data_response()
        for key, value in data.items():
            session[key] = value
        self.response = OK(data)

