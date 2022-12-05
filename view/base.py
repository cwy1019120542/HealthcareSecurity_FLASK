from calendar import monthrange
from model import model_dict
from flask import views, request, abort, session
from response import OKPage
from datetime import datetime, timedelta
from config import EnumerateData, Config

class Base(views.MethodView):

    model_name = None
    allowed_parameter = {}

    def __init__(self, *args, **kwargs):
        self.parameter_dict = {}
        self.model = None

    @classmethod
    def filter_parameter(cls, is_check_town=True):
        method_dict = {"GET": "args", "POST": "form", "PUT": "form"}
        method = request.method
        flask_parameter_dict = getattr(request, method_dict[method])
        parameter_dict = dict(flask_parameter_dict) if flask_parameter_dict else {}
        if 'year' not in parameter_dict:
            parameter_dict['year'] = Config.DEFAULT_YEAR
        allowed_parameter_dict = cls.allowed_parameter[method]
        if method == "POST":
            for key in allowed_parameter_dict.keys():
                if key not in parameter_dict:
                    abort(400)
        for key, value in list(parameter_dict.items()):
            if key not in allowed_parameter_dict or not value:
                parameter_dict.pop(key)
                continue
            value_type, value_len = allowed_parameter_dict[key]
            if value_type == "enum":
                value_split = value.split('_')
                for value_single in value_split:
                    if value_single not in getattr(EnumerateData, key):
                        abort(400)
                parameter_dict[key] = value_split if len(value_split) > 1 else value_split[0]
            elif value_type == 'date':
                value_split = value.split('_')
                if len(value_split) < 2:
                    abort(400)
                start_date = datetime.strptime(f'{value_split[0]}-01 00:00:00', '%Y-%m-%d %H:%M:%S')
                end_date_year, end_date_month = value_split[1].split('-')
                end_date_str = f'{value_split[1]}-{monthrange(int(end_date_year), int(end_date_month))[1]} 23:59:59'
                end_date = datetime.strptime(end_date_str, '%Y-%m-%d %H:%M:%S')
                parameter_dict[key] = [start_date, end_date]
            else:
                if not isinstance(value, value_type):
                    if value_type == bool:
                        parameter_dict[key] = True if value != 0 else False
                    elif value_type == int:
                        if str(value).isdigit():
                            parameter_dict[key] = int(value)
                        else:
                            abort(400)
                    else:
                        abort(400)
                if value_len and len(value) > value_len:
                    abort(400)
        session_town = session.get('town')
        if session_town and is_check_town:
            if 'town' not in parameter_dict or parameter_dict['town']!=session_town:
                abort(400)
        return dict(parameter_dict)

    @classmethod
    def authentication(cls, user_id, resource):
        if "id" not in session or user_id != session["id"]:
            abort(401)
        if resource not in session['authority'] and '*' not in session['authority']:
            abort(403)

    @staticmethod
    def model_query(model, parameter_dict, query=None):
        query = model.query if not query else query
        for key, value in parameter_dict.items():
            if isinstance(value, list):
                if isinstance(value[0], datetime):
                    query = query.filter(getattr(model, key).between(value[0], value[1]))
                else:
                    query = query.filter(getattr(model, key).in_(value))
            else:
                query = query.filter(getattr(model, key)==value)
        return query

    def get(self):
        parameter_dict = self.filter_parameter()
        page = parameter_dict.pop("page", 1)
        limit = parameter_dict.pop("limit", 7)
        year = parameter_dict.pop('year')
        model = model_dict[f'{self.model_name}_{year}']
        offset = (page - 1) * limit
        query = self.model_query(model, parameter_dict)
        data_count = query.count()
        data_list = [i.data_response(i_index) for i_index, i in enumerate(query.offset(offset).limit(limit).all(), offset+1)]
        return OKPage(data_list, data_count, page, limit)




