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

    def post(self):
        parameter_dict = self.filter_parameter(False)
        model = model_dict['user']
        phone_number = parameter_dict['phone_number']
        password = parameter_dict['password']
        user = model.query.filter_by(phone_number=phone_number).first()
        if not user or user.password != password or not user.is_available:
            abort(401)
        data = user.data_response()
        for key, value in data.items():
            session[key] = value
        return OK(data)
