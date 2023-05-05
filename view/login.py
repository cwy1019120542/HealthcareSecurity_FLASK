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
            "phone_number": ('str', None, 'user', True, 20), "password": ('str', None, 'user', True, 20)
        }
    }
    is_year = False
    is_authentication = False

    def make_post_query(self):
        super(Login, self).make_get_query()

    def clean_post_response(self):
        super().clean_get_response()
        if not self.response_data or not self.response_data[0]['is_available']:
            abort(401)
        self.response_data = self.response_data[0]
        self.response_data['authority'] = EnumerateData.authority[self.response_data['identity']]
        for key, value in self.response_data.items():
            session[key] = value


