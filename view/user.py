from .base import Base
from model import model_dict
from extension import db
from response import OK
from flask import abort

class Password(Base):

    methods = ['put']
    model_name = "user"
    allowed_parameter = {
        "PUT": {'old_password': (str, 20), 'new_password': (str, 20)},
    }
    is_year = False

    def make_response(self):
        user = self.query.filter_by(id=self.user_id).first()
        if not user or user.password != self.parameter_dict['old_password']:
            abort(400)
        user.password = self.parameter_dict['new_password']
        db.session.commit()
        self.response = user.data_response()