from .base import Base, BaseList
from model import model_dict
from flask import session
from sqlalchemy.sql import func, distinct
from response import OK, ExcelResponse
from config import EnumerateData
from sqlalchemy import or_

class SettleData(Base):

    methods = ['get']
    model_name = "settle_data"
    join_model_name = 'person'
    entities_dict = {'model': ['id', 'settle_id', 'cure_id', 'self_number', 'id_number', 'person_type', 'pay_place', 'hospital_id', 'hospital_name', 'hospital_level', 'hospital_place', 'start_date', 'end_date', 'settle_date', 'evidence_type', 'all_expense', 'self_expense', 'over_expense', 'first_expense', 'inner_expense', 'start_pay', 'overall_pay', 'large_pay', 'big_pay', 'rescue_pay', 'civil_pay', 'other_pay', 'all_pay', 'cash_pay', 'account_pay', 'together_pay', 'illness_name', 'cure_type'],
                     'join_model': ['name', 'civil_attribute', 'poverty_state', 'orphan_attribute', 'disable_attribute',
                                    'treat_attribute', 'accident_attribute', 'town', 'village',
                                    'phone_number']}
    allowed_parameter = {
        "GET": {'name': (str, 20, "person", False), "civil_attribute": ("enum", 'or_', "person", False), "orphan_attribute": ("enum", 'or_', "person", False),
            "disable_attribute": ("enum", 'or_', "person", False), "treat_attribute": ("enum", 'or_', "person", False),"accident_attribute": ("enum", 'or_', "person", False),
            "poverty_state": ("enum", 'or_', "person", False), "town": ("enum", None, "person", False), "village": ("enum", None, "person", False),'year': ("enum", None, '', True),
            "page": (int, None, '', False), "person_type": ("enum", None, 'settle_data', False), "pay_place": ("enum", None, 'settle_data', False), "hospital_level": ("enum", None, 'settle_data', False),
            "evidence_type": ("enum", None, 'settle_data', False), "cure_type": ("enum", None, 'settle_data', False), "settle_date": ("date", None, 'settle_data', False), "pay_exists": ("enum", None, 'settle_data', False)
        }
    }

    @staticmethod
    def get_deal_dict(pay_exists_list, is_list=True):
        deal_dict = {}
        if not is_list:
            pay_exists_list = [pay_exists_list]
        for pay_exists in pay_exists_list:
            pay_exists_key = EnumerateData.pay_exists_dict[pay_exists]
            deal_dict[f'{pay_exists_key}!'] = 0
        return deal_dict
    
    def extra_make_response(self):
        pay_exists_list = self.parameter_dict.get(self.model_name, {}).pop('pay_exists', None)
        if pay_exists_list:
            if isinstance(pay_exists_list, list):
                self.query = self.query.filter(or_(*self.get_query_parameter(self.model, self.get_deal_dict(pay_exists_list))))
            else:
                self.query = self.query.filter(*self.get_query_parameter(self.model, self.get_deal_dict(pay_exists_list, False)))

    def clean_response(self):
        super().clean_response()
        for data_group in self.response_data:
            for key in ('all_expense', 'self_expense', 'over_expense', 'first_expense', 'inner_expense', 'start_pay', 'overall_pay', 'large_pay', 'big_pay', 'rescue_pay', 'civil_pay', 'other_pay', 'all_pay', 'cash_pay', 'account_pay', 'together_pay'):
                data_group[key] = self.to_float(data_group[key])
            for key in ('start_date', 'end_date', 'settle_date'):
                data_group[key] = self.to_string_date(data_group[key])
            data_group['attribute'] = self.merge_attribute(data_group)

class SettleDataList(BaseList, SettleData):

    pass


class SettleDataStatistic(SettleData):

    def make_response(self):
        self.query = self.query.with_entities(func.count(self.model.id), func.count(distinct(self.model.id_number)), func.sum(self.model.all_expense), func.sum(self.model.inner_expense), func.sum(self.model.overall_pay), func.sum(self.model.large_pay), func.sum(self.model.big_pay), func.sum(self.model.rescue_pay),
                                                func.sum(self.model.civil_pay), func.sum(self.model.other_pay), func.sum(self.model.all_pay), func.sum(self.model.cash_pay), func.sum(self.model.account_pay), func.sum(self.model.together_pay))
        self.parameter_dict.pop('page', None)
        super().make_response()

    def clean_response(self):
        result = self.query.first()
        result_dict = {}
        for key, value in zip(
                ['time_count', 'number_count', 'all_expense', 'inner_expense', 'overall_pay', 'large_pay', 'big_pay',
                 'rescue_pay', 'civil_pay', 'other_pay', 'all_pay', 'cash_pay', 'account_pay', 'together_pay'], result):
            if not value:
                value = 0
            if key in ['time_count', 'number_count']:
                result_dict[key] = value
            else:
                result_dict[key] = round(float(value), 2)
        self.response_data = result_dict

class SettleDataListDownload(SettleDataList):

    is_page = False
    response_type_dict = {'GET': ExcelResponse}

    def clean_response(self):
        super().clean_response()
        self.response_data = (tuple(i.values()) for i in self.response_data)
        self.extra_response_data = ['序号', 'id', '结算ID', '就诊ID', '个人编号', '证件号码', '人员类别', '支付地点类别', '定点医药机构编号', '定点医药机构名称', '医院等级', '定点医保归属区划', '开始日期', '结束日期', '结算日期', '就诊凭证类型', '总费用', '全自费金额', '超限价自费费用', '先行自付金额', '范围内费用', '起付线', '统筹基金支出', '大额医疗支出金额', '大病保险支出', '医疗救助支出', '公务员医疗补助', '其他基金支付', '基金支付总额', '个人现金支付', '个人账户支付', '账户共济支付金额', '病种名称', '医疗类别', '人员姓名', '乡镇', '村', '手机号', '人员属性']

class SettleDataStatisticDownload(SettleDataStatistic):

    response_type_dict = {'GET': ExcelResponse}

    def clean_response(self):
        super().clean_response()
        self.response_data = [tuple(self.response_data.values())]
        self.extra_response_data = ['人次', '人数', '总费用（元）', '范围内费用（元）', '统筹基金支出（元）', '大额医疗支出（元）', '大病保险支出（元）', '医疗救助支出（元）', '公务员医疗补助（元）', '其他基金支付（元）', '基金支付总额（元）', '个人现金支付（元）', '个人账户支付（元）', '账户共济支付金额（元）']