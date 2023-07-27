import os
from calendar import monthrange
from model import model_dict
from flask import views, request, abort, session, send_file
from response import OK
from datetime import datetime, timedelta
from config import EnumerateData, Config
from sqlalchemy import or_
from werkzeug.datastructures import FileStorage
from uuid import uuid1
from extension import db

class Base(views.MethodView):

    model_name = None
    join_model_name = None
    extra_model_name = None
    allowed_parameter = {}
    is_authentication = True
    is_year = True
    is_page = False
    entities_dict = {'model': [], 'join_model': []}
    response_type_dict = {'GET': OK, 'POST': OK, 'PUT': OK, 'DELETE': OK}
    method_dict = {"GET": "args", "POST": "form", "PUT": "form"}
    operator_dict = {}

    def __init__(self, *args, **kwargs):
        self.parameter_dict = {}
        self.model = None
        self.method = None
        self.join_model = model_dict.get(self.join_model_name)
        self.extra_model = model_dict.get(self.extra_model_name)
        self.extra_query = None
        self.query = None
        self.user_id = None
        self.response_type = None
        self.response_data = {}
        self.extra_response_data = {}
        self.response = None
        self.year = None
        super().__init__(*args, **kwargs)

    @staticmethod
    def merge_attribute(data_group, key_list=('civil_attribute', 'poverty_state', 'orphan_attribute', 'disable_attribute', 'treat_attribute', 'accident_attribute')):
        value_list = []
        for key in key_list:
            value = data_group.pop(key)
            if value:
                value_list.append(value)
        return ', '.join(value_list)

    @staticmethod
    def to_float(data, number=2):
        if isinstance(data, tuple):
            data = data[0] / data[1] if data[1] else 0
        data = round(float(data), number) if data else 0
        return data

    @staticmethod
    def fill_field(data_group, field_list):
        for field in field_list:
            data_group[field] = ''


    @staticmethod
    def to_percent(data):
        return f'{round(data * 100, 2)}%' if data else '0%'

    @staticmethod
    def to_string_date(date, has_time=True):
        if has_time:
            format_str = '%Y-%m-%d %H:%M:%S'
        else:
            format_str = '%Y-%m-%d'
        return date.strftime(format_str) if date else None

    @staticmethod
    def bool_to_string(data):
        return '是' if data else '否'

    def generate_parameter_dict(self, model_name, key, value, relation):
        parameter_dict = self.parameter_dict
        if model_name:
            self.parameter_dict.setdefault(model_name, {})
            parameter_dict = self.parameter_dict[model_name]
        if relation:
            parameter_dict.setdefault(relation, {})[key] = value
        else:
            parameter_dict[key] = value

    @staticmethod
    def clean_enum(value, *args, **kwargs):
        value_split = value.split('|')
        for value_single in value_split:
            if value_single not in getattr(EnumerateData, kwargs['key']):
                abort(400)
        return value_split if len(value_split) > 1 else value_split[0]

    @staticmethod
    def clean_list(value, *args, **kwargs):
        value_split = value.split('|')
        return value_split if len(value_split) > 1 else value_split[0]

    @staticmethod
    def clean_combine_date(value, *args, **kwargs):
        value_split = value.split('|')
        if len(value_split) < 2:
            abort(400)
        value_split[0] = f'{value_split[0]} 00:00:00'
        value_split[1] = f'{value_split[1]} 23:59:59'
        return [datetime.strptime(i, '%Y-%m-%d %H:%M:%S') for i in value_split]

    @staticmethod
    def clean_date(value, *args, **kwargs):
        return datetime.strptime(value, '%Y-%m-%d')

    @staticmethod
    def clean_bool(value, *args, **kwargs):
        return True if value != '否' else False

    @staticmethod
    def clean_int(value, *args, **kwargs):
        if str(value).isdigit():
            value = int(value)
            if kwargs['max_value'] and value > kwargs['max_value']:
                abort(400)
            return value
        else:
            abort(400)

    @staticmethod
    def clean_str(value, *args, **kwargs):
        if not isinstance(value, str) or len(value) > kwargs['max_value']:
            abort(400)
        return value

    @staticmethod
    def clean_file(value, *args, **kwargs):
        if not isinstance(value, FileStorage):
            abort(400)
        return value

    @staticmethod
    def clean_float(value, *args, **kwargs):
        try:
            value = float(value)
        except:
            abort(400)
        else:
            return value

    def make_operator_query(self):
        for init_field, operator_group in self.operator_dict.items():
            operator_field, operator_value_field, model_type = operator_group
            model_name = getattr(self, f'{model_type}_name')
            model = getattr(self, model_type)
            operator = self.parameter_dict.get(model_name, {}).pop(operator_field, None)
            if operator_value_field:
                field = self.parameter_dict.get(model_name, {}).pop(init_field, None)
                operator_value = self.parameter_dict.get(model_name, {}).pop(operator_value_field, None)
            else:
                field = init_field
                operator_value = self.parameter_dict.get(model_name, {}).pop(field, None)
            if field and operator and operator_value != None:
                self.query = self.query.filter(getattr(getattr(model, field), operator)(operator_value))

    def filter_parameter(self):
        flask_parameter_dict = getattr(request, self.method_dict[self.method])
        request_parameter_dict = dict(flask_parameter_dict) if flask_parameter_dict else {}
        allowed_parameter_dict = self.allowed_parameter[self.method]
        must_parameter_list = [i for i, j in allowed_parameter_dict.items() if j[3]]
        for must_parameter in must_parameter_list:
            if must_parameter not in request_parameter_dict or not request_parameter_dict[must_parameter]:
                abort(400)
        for key, value in request_parameter_dict.items():
            if key not in allowed_parameter_dict or not value:
                continue
            value_type, relation, model_name, is_must, max_value = allowed_parameter_dict[key]
            self.generate_parameter_dict(model_name, key, getattr(self, f'clean_{value_type}')(value, key=key, max_value=max_value), relation)
        session_town = session.get('town')
        if 'town' in allowed_parameter_dict and session_town and self.is_authentication:
            if 'town' not in self.parameter_dict['person'] or self.parameter_dict['person']['town']!=session_town:
                abort(400)

    def authentication(self):
        if "id" not in session or self.user_id != session["id"]:
            abort(401)
        if self.model_name not in session['authority'] and '*' not in session['authority']:
            abort(403)

    def get_query_parameter(self, model, parameter_dict):
        filter_parameter_list = []
        for key, value in parameter_dict.items():
            if isinstance(value, list):
                if isinstance(value[0], datetime):
                    filter_parameter = getattr(model, key).between(value[0], value[1])
                else:
                    filter_parameter = getattr(model, key).in_(value)
            else:
                filter_parameter = getattr(model, key) == value
            filter_parameter_list.append(filter_parameter)
        return filter_parameter_list

    def make_get_query(self):
        main_parameter_dict = self.parameter_dict.get(self.model_name)
        join_parameter_dict = self.parameter_dict.get(self.join_model_name)
        for model, parameter_dict in ((self.model, main_parameter_dict), (self.join_model, join_parameter_dict)):
            if not parameter_dict or not model:
                continue
            or_dict = parameter_dict.pop('or_', None)
            if or_dict:
                self.query = self.query.filter(or_(*self.get_query_parameter(model, or_dict)))
            self.query = self.query.filter(*self.get_query_parameter(model, parameter_dict))

    def make_post_query(self):
        data_dict = self.parameter_dict[self.model_name]
        data_dict['operator'] = model_dict['user'].query.filter_by(id=self.user_id).first().name
        data_dict['operate_date'] = datetime.now()
        db.session.add(self.model(**data_dict))
        db.session.commit()

    def clean_post_response(self):
        pass

    def make_put_query(self):
        pass

    def clean_put_response(self):
        pass

    def make_delete_query(self):
        pass

    def clean_delete_response(self):
        pass


    def deal_request(self, user_id):
        self.method = request.method
        self.user_id = user_id
        self.response_type = self.response_type_dict[self.method]
        if self.is_authentication:
            self.authentication()
        self.filter_parameter()
        if self.is_year:
            self.year = self.parameter_dict.get('year', Config.DEFAULT_YEAR)
            self.model = model_dict[f'{self.model_name}_{self.year}']
        elif self.model_name:
            self.model = model_dict.get(self.model_name)
        if self.model:
            self.query = self.model.query
        if self.join_model_name:
            self.query = self.query.outerjoin(self.join_model, self.model.id_number==self.join_model.id_number)
        if self.entities_dict['model']:
            self.query = self.query.with_entities(*(getattr(self.model, i) for i in self.entities_dict.get('model', [])), *(getattr(self.join_model, i) for i in self.entities_dict.get('join_model', [])))
        if self.extra_model:
            self.extra_query = self.extra_model.query
        self.make_operator_query()
        getattr(self, f'make_{self.method.lower()}_query')()
        getattr(self, f'clean_{self.method.lower()}_response')()

    def clean_get_response(self):
        self.response_data = self.query.all()
        response_data = []
        offset = self.extra_response_data.get('offset')
        for data_index, data_group in enumerate(self.response_data, 1):
            data_dict = {}
            if offset!=None:
                data_dict['number'] = offset + data_index
            for key in data_group.keys():
                data_dict[key] = getattr(data_group, key)
            response_data.append(data_dict)
        self.response_data = response_data

    def get(self, user_id=None):
        self.deal_request(user_id)
        return self.response_type(self.response_data, self.extra_response_data) if self.response_type else self.response_data

    def post(self, user_id=None):
        self.deal_request(user_id)
        return self.response_type(self.response_data, self.extra_response_data)

    def put(self, user_id=None):
        self.deal_request(user_id)
        return self.response_type(self.response_data, self.extra_response_data)

    def delete(self, user_id=None):
        self.deal_request(user_id)
        return self.response_type(self.response_data, self.extra_response_data)


class BaseList(Base):

    is_page = True

    def clean_get_response(self):
        page = self.parameter_dict.get("page", 1)
        limit = self.parameter_dict.get("limit", 10)
        offset = (page - 1) * limit
        data_count = self.query.count()
        self.extra_response_data = {'data_count': data_count, 'page': page, 'limit': limit, 'offset': offset}
        if self.is_page:
            self.query = self.query.offset(offset).limit(limit)
        else:
            if data_count > 50000:
                abort(413)
        super().clean_get_response()

class Attachment(Base):

    methods = ['get', 'post']
    allowed_parameter = {
        'GET': {'attachment_id': ('str', None, '', True, 50)},
        'POST': {'attachment': ('file', None, '', True, None)},
    }
    method_dict = {"GET": "args", "POST": "files"}
    is_year = False
    response_type_dict = {'GET': '', 'POST': OK}
    base_dir = ''

    def make_post_query(self):
        pass

    def clean_post_response(self):
        attachment = self.parameter_dict['attachment']
        attachment_id = f'{uuid1()}{os.path.splitext(attachment.filename)[-1]}'
        attachment.save(os.path.join(self.base_dir, attachment_id))
        self.response_data['attachment_id'] = attachment_id

    def make_get_query(self):
        pass

    def clean_get_response(self):
        attachment_id = self.parameter_dict['attachment_id']
        file_path = os.path.join(self.base_dir, attachment_id)
        if not os.path.exists(file_path):
            abort(404)
        self.response_data = send_file(file_path)
        self.response_data.headers['file_name'] = attachment_id