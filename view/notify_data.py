from .base import BaseList, Attachment
from response import ExcelResponse, OK
from sqlalchemy.sql import func
from model import model_dict
from flask import abort
from config import Config

class NotifyData(BaseList):

    methods = ['get']
    model_name = 'notify_data'
    is_year = False
    entities_dict = {'model': ['id', 'title', 'content', 'is_available']}
    allowed_parameter = {'GET': {}}
    is_authentication = False

    def make_get_query(self):
        self.parameter_dict[self.model_name] = {'is_available': 1}
        super().make_get_query()