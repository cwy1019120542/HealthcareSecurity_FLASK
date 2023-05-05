from .base import Base
from model import model_dict
from extension import db
from response import OK
from flask import abort

class Password(Base):

    methods = ['put']
    model_name = "user"
    allowed_parameter = {
        "PUT": {'old_password': ('str', None, 'user', True, 20), 'new_password': ('str', None, 'user', True, 20)},
    }
    is_year = False

    def make_put_query(self):
        pass

    def clean_put_response(self):
        user = self.query.filter_by(id=self.user_id).first()
        if not user or user.password != self.parameter_dict[self.model_name]['old_password']:
            abort(400)
        user.password = self.parameter_dict[self.model_name]['new_password']
        db.session.commit()