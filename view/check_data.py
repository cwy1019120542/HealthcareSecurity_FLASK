from .base import BaseList
from response import ExcelResponse, OK
from sqlalchemy.sql import func
from model import model_dict

class Staff(BaseList):
    is_year = False
    methods = ['get']
    model_name = "staff"
    extra_model_name = 'check_data'
    entities_dict = {'model': ['name', 'id_number', 'work_number', 'department', 'position', 'education', 'phone_number', 'enter_date'], 'extra_model': ['data_count', 'get_point', 'lost_point']}
    allowed_parameter = {
        "GET": {
            "id_number": (str, 18, 'staff', False), "work_number": (int, None, 'staff', False),
            'name': (str, 20, "staff", False), "department": ("enum", None, "staff", False),
            "position": ("enum", None, "staff", False), "education": ("enum", None, "staff", False),
            'year': ("enum", None, 'check_data', True),
            "page": (int, None, '', False)}
    }


    def clean_response(self):
        super().clean_response()
        point_data_dict = {i[0]: i for i in self.extra_query.with_entities(self.extra_model.id_number, func.count(self.extra_model.id).label('data_count'), func.sum(self.extra_model.get_point).label('get_point'), func.sum(self.extra_model.lost_point).label('lost_point')).filter(*self.get_query_parameter(self.extra_model, self.parameter_dict[self.extra_model_name])).group_by(self.extra_model.id_number).all()}
        for data_group in self.response_data:
            data_group['enter_date'] = self.to_string_date(data_group['enter_date'])
            id_number = data_group['id_number']
            if id_number in point_data_dict:
                for field in self.entities_dict['extra_model']:
                    data_group[field] = point_data_dict[id_number][field]
            else:
                for field in self.entities_dict['extra_model']:
                    data_group[field] = 0
            data_group['point'] = 100 + data_group['get_point'] - data_group['lost_point']

class CheckData(BaseList):
    is_year = False
    methods = ['get', 'post']
    model_name = "check_data"
    join_model_name = 'staff'
    entities_dict = {'model': ['id_number', 'operate_type', 'check_type', 'check_source', 'get_point', 'lost_point', 'check_date', 'remark', 'operator', 'operate_date', 'attachment_id'], 'join_model': ['name']}
    allowed_parameter = {
        "GET": {
            "id_number": (str, 18, 'check_data', True),
            "operate_type": ("enum", None, "check_data", False), "check_type": ("enum", None, "check_data", False), "check_source": ("enum", None, "check_data", False),
            "check_date": ("date", None, "check_data", False),
            'year': ("enum", None, 'check_data', True),
            "page": (int, None, '', False)}
    }

    def clean_response(self):
        super().clean_response()
        for data_group in self.response_data:
            data_group['check_date'] = self.to_string_date(data_group['check_date'])
            data_group['operate_date'] = self.to_string_date(data_group['operate_date'])

class CheckAttachment(BaseList):

    methods = ['get', 'post']
    allowed_parameter = {
        'GET': {'attachment_id': (str, 50, '', True)},
        'POST': {'check_attachment': ('file', None, '', True)},
    }