from .base import BaseList
from response import ExcelResponse, OK
from sqlalchemy.sql import func
from model import model_dict
from flask import abort

class Staff(BaseList):
    is_year = False
    methods = ['get']
    model_name = "staff"
    extra_model_name = 'check_data'
    entities_dict = {'model': ['name', 'id_number', 'work_number', 'department', 'position', 'education', 'phone_number', 'enter_date'], 'extra_model': ['data_count', 'get_point', 'lost_point']}
    allowed_parameter = {
        "GET": {
            "id_number": ('str', None, 'staff', False, 18), "work_number": ('str', None, 'staff', False, 5),
            'name': ('str', None, "staff", False, 20), "department": ("enum", None, "staff", False, None),
            "position": ("enum", None, "staff", False, None), "education": ("enum", None, "staff", False, None),
            'year': ("enum", None, 'check_data', True, None),
            "page": ('int', None, '', False, None)}
    }


    def clean_get_response(self):
        super().clean_get_response()
        point_data_dict = {i[0]: i for i in self.extra_query.with_entities(self.extra_model.id_number, func.count(self.extra_model.id).label('data_count'), func.sum(self.extra_model.get_point).label('get_point'), func.sum(self.extra_model.lost_point).label('lost_point')).filter(*self.get_query_parameter(self.extra_model, self.parameter_dict[self.extra_model_name])).group_by(self.extra_model.id_number).all()}
        for data_group in self.response_data:
            data_group['enter_date'] = self.to_string_date(data_group['enter_date'], False)
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
            "id_number": ('str', None, 'check_data', True, 18),
            "operate_type": ("enum", None, "check_data", False, None), "check_type": ("enum", None, "check_data", False, None), "check_source": ("enum", None, "check_data", False, None),
            "check_date": ("combine_date", None, "check_data", False, None),
            'year': ("enum", None, 'check_data', True, None),
            "page": ('int', None, '', False, None)},
        "POST": {
            "id_number": ('str', None, 'check_data', True, 18),
            "operate_type": ("enum", None, "check_data", True, None),
            "check_type": ("enum", None, "check_data", True, None),
            "check_source": ("enum", None, "check_data", True, None),
            "get_point": ("float", None, "check_data", True, None),
            "lost_point": ("float", None, "check_data", True, None),
            "check_date": ("date", None, "check_data", True, None),
            "remark": ('str', None, 'check_data', False, 50),
            "attachment_id": ('str', None, 'check_data', False, 50),
            'year': ("enum", None, 'check_data', True, None),
        }
    }

    def clean_get_response(self):
        super().clean_get_response()
        for data_group in self.response_data:
            data_group['check_date'] = self.to_string_date(data_group['check_date'], False)
            data_group['operate_date'] = self.to_string_date(data_group['operate_date'])

    def make_post_query(self):
        if not self.join_model.query.filter(self.join_model.id_number==self.parameter_dict[self.model_name]['id_number']).first():
            abort(400)
        super().make_post_query()