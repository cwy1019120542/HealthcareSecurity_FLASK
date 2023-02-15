from .base import Base
from flask import session, abort
from model import model_dict
from response import OK
from config import EnumerateData

class Login(Base):

    methods = ['post']
    model_name = "user"
    entities_dict = {'model': ['id', 'name', 'phone_number', 'qq', 'town', 'identity', 'is_available']}
    allowed_parameter = {
        "POST": {
            "phone_number": (str, 20, 'user', True), "password": (str, 20, 'user', True)
        }
    }
    is_year = False
    is_authentication = False
    has_entities = True

    def make_query(self):
        super().make_query()
        self.response_data = self.query.all()
        if not self.response_data or not self.response_data[0].is_available:
            abort(401)

    def clean_response(self):
        super().clean_response()
        self.response_data = self.response_data[0]
        self.response_data['authority'] = EnumerateData.authority[self.response_data['identity']]
        for key, value in self.response_data.items():
            session[key] = value


