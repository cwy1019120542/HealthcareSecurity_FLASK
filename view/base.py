from calendar import monthrange
from model import model_dict
from flask import views, request, abort, session
from response import OKPage, OK
from datetime import datetime, timedelta
from config import EnumerateData, Config
from sqlalchemy import or_

class Base(views.MethodView):

    model_name = None
    allowed_parameter = {}
    is_authentication = True
    is_year = True

    def __init__(self, *args, **kwargs):
        self.parameter_dict = {}
        self.model = None
        self.query = None
        self.user_id = None
        self.response = OK({})
        self.response_data = {}
        self.year = None
        super().__init__(*args, **kwargs)

    def filter_parameter(self):
        method_dict = {"GET": "args", "POST": "form", "PUT": "form"}
        method = request.method
        flask_parameter_dict = getattr(request, method_dict[method])
        request_parameter_dict = dict(flask_parameter_dict) if flask_parameter_dict else {}
        if 'year' not in request_parameter_dict:
            request_parameter_dict['year'] = Config.DEFAULT_YEAR
        allowed_parameter_dict = self.allowed_parameter[method]
        if method == "POST":
            for key in allowed_parameter_dict.keys():
                if key not in request_parameter_dict:
                    abort(400)
        special_filter_dict = {'or_': {}}
        parameter_dict = {}
        for key, value in request_parameter_dict.items():
            if key not in allowed_parameter_dict or not value:
                continue
            value_type, remark = allowed_parameter_dict[key]
            if value_type == "enum":
                value_split = value.split('_')
                for value_single in value_split:
                    if value_single not in getattr(EnumerateData, key):
                        abort(400)
                value_split = value_split if len(value_split) > 1 else value_split[0]
                if remark:
                    special_filter_dict[remark][key] = value_split
                else:
                    parameter_dict[key] = value_split
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
                else:
                    if remark and len(value) > remark:
                        abort(400)
                    parameter_dict[key] = value
        session_town = session.get('town')
        if session_town and self.is_authentication:
            if 'town' not in parameter_dict or parameter_dict['town']!=session_town:
                abort(400)
        parameter_dict.update(special_filter_dict)
        self.parameter_dict = parameter_dict

    def authentication(self):
        if "id" not in session or self.user_id != session["id"]:
            abort(401)
        if self.model_name not in session['authority'] and '*' not in session['authority']:
            abort(403)

    def get_file_name(self):
        file_name_list = []
        print(self.parameter_dict)
        for key1, value1 in self.parameter_dict.items():
            if isinstance(value1, dict):
                for key2, value2 in value1.items():
                    if isinstance(value2, list):
                        file_name_list.append('_'.join(values2))
                    else:
                        file_name_list.append(value2)
            else:
                if isinstance(value1, list):
                    file_name_list.append('_'.join(value1))
                else:
                    file_name_list.append(value1)
        return '、'.join(file_name_list)

    def get_query_parameter(self, parameter_dict):
        filter_parameter_list = []
        for key, value in parameter_dict.items():
            if isinstance(value, list):
                if isinstance(value[0], datetime):
                    filter_parameter = getattr(self.model, key).between(value[0], value[1])
                else:
                    filter_parameter = getattr(self.model, key).in_(value)
            else:
                if key.endswith('!'):
                    filter_parameter = getattr(self.model, key.strip('!')) != value
                else:
                    filter_parameter = getattr(self.model, key) == value
            filter_parameter_list.append(filter_parameter)
        return filter_parameter_list

    def make_response(self):
        or_dict = self.parameter_dict.pop('or_')
        if or_dict:
            self.query = self.query.filter(or_(*self.get_query_parameter(or_dict)))
        self.query = self.query.filter(*self.get_query_parameter(self.parameter_dict))

    def deal_request(self, user_id):
        self.user_id = user_id
        if self.is_authentication:
            self.authentication()
        self.filter_parameter()
        if self.is_year:
            self.year = self.parameter_dict.pop('year')
            self.model = model_dict[f'{self.model_name}_{self.year}']
        else:
            self.model = model_dict[self.model_name]
        self.query = self.model.query
        self.make_response()

    def get(self, user_id=None):
        self.deal_request(user_id)
        return self.response

    def post(self, user_id=None):
        self.deal_request(user_id)
        return self.response

    def put(self, user_id=None):
        self.deal_request(user_id)
        return self.response

    def delete(self, user_id=None):
        self.deal_request(user_id)
        return self.response


class BaseList(Base):

    is_page = True
    response_type = 'dict_response'

    def make_response(self):
        page = self.parameter_dict.pop("page", 1)
        limit = self.parameter_dict.pop("limit", 7)
        super().make_response()
        offset = (page - 1) * limit
        data_count = self.query.count()
        if self.is_page:
            self.query = self.query.offset(offset).limit(limit)
        else:
            if data_count > 50000:
                abort(400)
        self.response_data = [getattr(i, self.response_type)(i_index) for i_index, i in enumerate(self.query.all(), offset + 1)]
        self.response = OKPage(self.response_data, data_count, page, limit)



