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
    allowed_parameter = {
        "GET": {
            'year': ("enum", None), 'name': (str, 20), "id_number": (str, 18), "person_type": ("enum", None),
            "pay_place": ("enum", None), "hospital_level": ("enum", None),
            "evidence_type": ("enum", None), "cure_type": ("enum", None), "settle_date": ("date", None),
            "page": (int, None), "pay_exists": ("enum", None),
            "attribute": ("enum", 'or_'), "second_attribute": ("enum", 'or_'), "poverty_state": ("enum", 'or_'),
            "town": ("enum", None), "village": ("enum", None)
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
    
    def deal_pay_exists(self):
        pay_exists_list = self.parameter_dict.pop('pay_exists', None)
        if pay_exists_list:
            if isinstance(pay_exists_list, list):
                self.query = self.query.filter(or_(*self.get_query_parameter(self.get_deal_dict(pay_exists_list))))
            else:
                self.query = self.query.filter(*self.get_query_parameter(self.get_deal_dict(pay_exists_list, False)))


class SettleDataList(BaseList, SettleData):

    def make_response(self):
        self.deal_pay_exists()
        super().make_response()



class SettleDataStatistic(SettleData):

    def make_response(self):
        self.query = self.query.with_entities(func.count(self.model.id), func.count(distinct(self.model.id_number)), func.sum(self.model.all_expense), func.sum(self.model.inner_expense), func.sum(self.model.overall_pay), func.sum(self.model.large_pay), func.sum(self.model.big_pay), func.sum(self.model.rescue_pay),
                                                func.sum(self.model.civil_pay), func.sum(self.model.other_pay), func.sum(self.model.all_pay), func.sum(self.model.cash_pay), func.sum(self.model.account_pay), func.sum(self.model.together_pay))
        self.deal_pay_exists()
        self.parameter_dict.pop('page', None)
        super().make_response()
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
        self.response = OK(result_dict)

class SettleDataListDownload(SettleDataList):

    is_page = False
    response_type = 'list_response'

    def make_response(self):
        super().make_response()
        self.response_data.insert(0, ['序号', 'id', '结算ID', '就诊ID', '个人编号', '人员姓名', '证件号码', '人员类别', '支付地点类别', '定点医药机构编号', '定点医药机构名称', '医院等级', '定点医保归属区划', '开始日期', '结束日期', '结算日期', '就诊凭证类型', '总费用', '全自费金额', '超限价自费费用', '先行自付金额', '范围内费用', '起付线', '统筹基金支出', '大额医疗支出金额', '大病保险支出', '医疗救助支出', '公务员医疗补助', '其他基金支付', '基金支付总额', '个人现金支付', '个人账户支付', '账户共济支付金额', '病种名称', '医疗类别', '人员属性', '其他属性', '贫困状态', '乡镇', '村'])
        self.response = ExcelResponse(self.response_data)

class SettleDataStatisticDownload(SettleDataStatistic):

    def make_response(self):
        super().make_response()
        data_group_list = [['人次', '人数', '总费用（元）', '范围内费用（元）', '统筹基金支出（元）', '大额医疗支出（元）', '大病保险支出（元）', '医疗救助支出（元）', '公务员医疗补助（元）', '其他基金支付（元）', '基金支付总额（元）', '个人现金支付（元）', '个人账户支付（元）', '账户共济支付金额（元）']]
        data_group_list.append([*self.response_data.values()])
        self.response = ExcelResponse(data_group_list)