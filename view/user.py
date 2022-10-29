from .base import Base
from model import model_dict
from extension import db
from response import OK
from flask import abort

class Password(Base):
    methods = ['put']
    model_name = "user"
    authority_name = 'user'
    allowed_parameter = {
        "PUT": {'old_password': (str, 20), 'new_password': (str, 20)},
    }

    def put(self, user_id):
        self.authentication(user_id, self.authority_name)
        parameter_dict = self.filter_parameter()
        model = model_dict[self.model_name]
        user = model.query.filter_by(id=user_id).first()
        if not user or user.password != parameter_dict['old_password']:
            abort(400)
        user.password = parameter_dict['new_password']
        db.session.commit()
        return OK(user.data_response())