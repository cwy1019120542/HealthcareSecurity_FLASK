from flask import views
from config import EnumerateData as ED
from response import OK

class EnumerateData(views.MethodView):

    allowed_parameter = {
        "GET": {},
    }

    def get(self):
        return OK(ED.dict_response())
