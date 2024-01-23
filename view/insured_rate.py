from .base import Base
from response import ExcelResponse
from sqlalchemy.sql import func
from config import StaticData, EnumerateData

class InsuredRate(Base):

    methods = ['get']
    model_name = "insured_data"
    join_model_name = 'person'
    allowed_parameter = {
        "GET": {
            "pay_date": ("combine_date", None, 'insured_data', False, None), 'year': ("enum", None, '', True, None)}
    }

    def make_get_query(self):
        self.query = self.query.with_entities(self.join_model.town, func.count(self.model.id)).filter(self.model.own_expense!=None).group_by(self.join_model.town)
        super().make_get_query()

    def clean_get_response(self):
        result_list = self.query.all()
        self.response_data = []
        town_list = [i[0] for i in result_list]
        if None in town_list:
            none_number = result_list.pop(town_list.index(None))[1]
            other_count = 0
            if '其他' in town_list:
                other_index = town_list.index('其他')
                other_count = result_list[other_index][1]
                result_list.pop(other_index)
            result_list.append(('其他', other_count+none_number))
        for town, data_count in result_list:
            target = StaticData.town_target_dict[self.year].get(town, 0)
            town_dict = {'number': '', 'town': town, 'target': target, 'data_count': data_count, 'percent': self.to_float((data_count, target), 4)}
            self.response_data.append(town_dict)
        self.response_data.sort(key=lambda x:x['percent'], reverse=True)
        all_target = 0
        all_count = 0
        for data_index, data in enumerate(self.response_data, 1):
            data['number'] = data_index
            data['percent'] = self.to_percent(data['percent'])
            all_target +=  data['target']
            all_count += data['data_count']
            if data['town'] == '其他':
                data['target'] = '——'
                data['percent'] = '——'
        self.response_data.append({'number': '', 'town': '合计', 'target': all_target, 'data_count': all_count, 'percent': self.to_percent(self.to_float((all_count, all_target), 4))})

class SpecialInsuredRate(Base):

    methods = ['get']
    model_name = "insured_data"
    join_model_name = 'person'
    allowed_parameter = {
        "GET": {
            "pay_date": ("combine_date", None, 'insured_data', False, None),
            "civil_attribute": ("enum", 'or_', "person", False, None), "orphan_attribute": ("enum", 'or_', "person", False, None),
            "disable_attribute": ("enum", 'or_', "person", False, None), "treat_attribute": ("enum", 'or_', "person", False, None),
            "accident_attribute": ("enum", 'or_', "person", False, None), "poverty_state": ("enum", 'or_', "person", False, None),
            'year': ("enum", None, '', True, None)}
    }

    def make_get_query(self):
        self.query = self.query.with_entities(self.join_model.town, self.model.insured_state, func.count(self.model.id)).group_by(self.join_model.town, self.model.insured_state)
        super().make_get_query()

    def clean_get_response(self):
        result_list = self.query.all()
        result_dict = {}
        self.response_data = []
        for town in EnumerateData.town:
            result_dict[town] = {'number': '', 'town': town, 'target': 0}
            for insured_state in EnumerateData.insured_state:
                result_dict[town][insured_state] = 0
            result_dict[town]['data_count'] = 0
            result_dict[town]['percent'] = 0
        for result in result_list:
            town, insured_state, data_count = result
            result_dict[town][insured_state] = data_count
        for town, town_dict in result_dict.items():
            target = 0
            for insured_state in EnumerateData.insured_state:
                target += town_dict.setdefault(insured_state, 0)
            town_dict['target'] = target
            town_dict['data_count'] = target-town_dict['其他']
            town_dict['percent'] = self.to_float((town_dict['data_count'], target), 4)
            self.response_data.append(town_dict)
        self.response_data.sort(key=lambda x: x['percent'], reverse=True)
        all_count_dict = {'number': '', 'town': '合计', 'target': 0}
        for insured_state in EnumerateData.insured_state:
            all_count_dict[insured_state] = 0
        all_count_dict['data_count'] = 0
        all_count_dict['percent'] = 0
        target = 0
        for data_index, data in enumerate(self.response_data, 1):
            data['number'] = data_index
            data['percent'] = self.to_percent(data['percent'])
            for insured_state in EnumerateData.insured_state:
                all_count_dict[insured_state] += data[insured_state]
                target += data[insured_state]
        all_count_dict['target'] = target
        all_count_dict['data_count'] = target-all_count_dict['其他']
        all_count_dict['percent'] = self.to_percent(self.to_float((all_count_dict['data_count'], target), 4))
        self.response_data.append(all_count_dict)

class InsuredRateDownload(InsuredRate):
    response_type_dict = {'GET': ExcelResponse}

    def clean_get_response(self):
        super().clean_get_response()
        self.response_data = (tuple(i.values()) for i in self.response_data)
        self.extra_response_data = ['序号', '乡镇', '任务数', '完成数', '完成率']

class SpecialInsuredRateDownload(SpecialInsuredRate):
    response_type_dict = {'GET': ExcelResponse}

    def clean_get_response(self):
        super().clean_get_response()
        self.response_data = (tuple(i.values()) for i in self.response_data)
        self.extra_response_data = ['序号', '乡镇', '任务数', '本地居民', '本地职工(在职)', '本地职工(退休)', '异地居民', '异地职工', '参军', '服刑', '死亡', '失联', '动态新增', '自愿放弃', '其他原因', '完成数', '完成率']
