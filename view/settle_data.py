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
    entities_dict = {'model': ['id', 'settle_id', 'cure_id', 'self_number', 'id_number', 'person_type', 'hospital_id', 'hospital_name', 'hospital_level', 'hospital_place', 'start_date', 'end_date', 'settle_date', 'evidence_type', 'all_expense', 'self_expense', 'over_expense', 'first_expense', 'inner_expense', 'start_pay', 'overall_pay', 'large_pay', 'big_pay', 'rescue_pay', 'civil_pay', 'other_pay', 'all_pay', 'cash_pay', 'account_pay', 'together_pay', 'illness_name', 'cure_type', 'overall_percent', 'is_centre', 'operator', 'remark', 'illness_number', 'is_mid_settle', 'is_use_account', 'is_valid', 'is_refund', 'overyear_refund'],
                     'join_model': ['name', 'civil_attribute', 'poverty_state', 'orphan_attribute', 'disable_attribute',
                                    'treat_attribute', 'accident_attribute', 'phone_number', 'town', 'village']}
    allowed_parameter = {
        "GET": {'name': ('str', None, "person", False, 20), 'id_number': ('str', None, "person", False, 18), "civil_attribute": ("enum", 'or_', "person", False, None), "orphan_attribute": ("enum", 'or_', "person", False, None),
            "disable_attribute": ("enum", 'or_', "person", False, None), "treat_attribute": ("enum", 'or_', "person", False, None),"accident_attribute": ("enum", 'or_', "person", False, None),
            "poverty_state": ("enum", 'or_', "person", False, None), "town": ("enum", None, "person", False, None), "village": ("enum", None, "person", False, None),'year': ("enum", None, '', True, None),
            "page": ('int', None, '', False, None), "person_type": ("enum", None, 'settle_data', False, None), "hospital_place": ("enum", None, 'settle_data', False, None), "hospital_level": ("enum", None, 'settle_data', False, None), 'is_centre': ('bool', None, 'settle_data', False, None),
            "evidence_type": ("enum", None, 'settle_data', False, None), "cure_type": ("enum", None, 'settle_data', False, None), "settle_date": ("combine_date", None, 'settle_data', False, None),
            "pay_type": ("enum", None, 'settle_data', False, None), "pay_type_operator": ("enum", None, 'settle_data', False, None), "pay_type_value": ('int', None, 'settle_data', False, None), "hospital_name": ('str', None, "settle_data", False, 80), "hospital_id": ('list', None, "settle_data", False, None), 'is_mid_settle': ('bool', None, 'settle_data', False, None), 'is_use_account': ('bool', None, 'settle_data', False, None), 'overyear_refund': ("enum", None, 'settle_data', False, None), 'is_refund': ('bool', None, 'settle_data', False, None), 'is_valid': ('bool', None, 'settle_data', False, None), "limit": ('int', None, '', False, 1000), 'illness_name': ('str', None, "settle_data", False, 70),
        }
    }
    decimal_field_list = ('all_expense', 'self_expense', 'over_expense', 'first_expense', 'inner_expense', 'start_pay', 'overall_pay', 'large_pay', 'big_pay', 'rescue_pay', 'civil_pay', 'other_pay', 'all_pay', 'cash_pay', 'account_pay', 'together_pay', 'overall_percent')
    operator_dict = {'pay_type': ('pay_type_operator', 'pay_type_value', 'model')}
    fuzzy_field = ('name', 'illness_name', 'hospital_name')

class SettleDataList(BaseList, SettleData):

    def clean_get_response(self):
        super().clean_get_response()
        for data_group in self.response_data:
            for key in self.decimal_field_list:
                data_group[key] = self.to_float(data_group[key])
            for key in ('start_date', 'end_date', 'settle_date'):
                data_group[key] = self.to_string_date(data_group[key])
            data_group['attribute'] = self.merge_attribute(data_group)
            for key in ('is_centre', 'is_mid_settle', 'is_use_account', 'is_valid', 'is_refund'):
                data_group[key] = self.bool_to_string(data_group[key])




class SettleDataMerge(BaseList, SettleData):

    operator_dict = {}

    def make_get_query(self):
        self.query = self.query.with_entities(func.count(self.model.id).label('data_count'), self.model.id_number, *(getattr(self.join_model, i) for i in self.entities_dict['join_model']), *(func.sum(getattr(self.model, i)).label(i) for i in self.decimal_field_list)).group_by(self.model.id_number)
        pay_type = self.parameter_dict.get(self.model_name, {}).pop('pay_type', None)
        pay_type_operator = self.parameter_dict.get(self.model_name, {}).pop('pay_type_operator', None)
        pay_type_value = self.parameter_dict.get(self.model_name, {}).pop('pay_type_value', None)
        BaseList.make_get_query(self)
        if pay_type and pay_type_operator and pay_type_value != None:
            self.query = self.query.having(getattr(func.sum(getattr(self.model, pay_type)), pay_type_operator)(pay_type_value))

    def clean_get_response(self):
        BaseList.clean_get_response(self)
        for data_group in self.response_data:
            for key in self.decimal_field_list:
                data_group[key] = self.to_float(data_group[key])
            data_group['attribute'] = self.merge_attribute(data_group)
            self.fill_field(data_group, ('id', 'settle_id', 'cure_id', 'self_number', 'person_type', 'hospital_id', 'hospital_name', 'hospital_level', 'hospital_place', 'start_date', 'end_date', 'settle_date', 'evidence_type', 'illness_name', 'cure_type', 'overall_percent', 'is_centre', 'operator', 'remark', 'illness_number', 'is_mid_settle', 'is_use_account', 'is_valid', 'is_refund', 'overyear_refund'))

class SettleDataStatistic(SettleData):

    def make_get_query(self):
        self.query = self.query.with_entities(func.count(self.model.id), func.count(distinct(self.model.id_number)), func.sum(self.model.all_expense), func.sum(self.model.inner_expense), func.sum(self.model.overall_pay), func.sum(self.model.large_pay), func.sum(self.model.big_pay), func.sum(self.model.rescue_pay),
                                                func.sum(self.model.civil_pay), func.sum(self.model.other_pay), func.sum(self.model.all_pay), func.sum(self.model.cash_pay), func.sum(self.model.account_pay), func.sum(self.model.together_pay))
        super().make_get_query()

    def clean_get_response(self):
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

    def clean_get_response(self):
        super().clean_get_response()
        self.response_data = (tuple(i.values()) for i in self.response_data)
        self.extra_response_data = ['序号', 'id', '结算ID', '就诊ID', '个人编号', '证件号码', '人员类别', '定点医药机构编号', '定点医药机构名称', '医院等级', '医药机构地点类别', '开始日期', '结束日期', '结算日期', '就诊凭证类型', '总费用', '全自费金额', '超限价自费费用', '先行自付金额', '范围内费用', '起付线', '统筹基金支出', '大额医疗支出金额', '大病保险支出', '医疗救助支出', '公务员医疗补助', '其他基金支付', '基金支付总额', '个人现金支付', '个人账户支付', '账户共济支付金额', '病种名称', '医疗类别', '统筹基金支付比例', '中心报销', '经办人员', '备注', '疾病编码', '是否中途结算', '是否使用账户', '是否有效', '是否冲销', '跨年冲销', '人员姓名', '手机号', '乡镇', '村', '人员属性']

class SettleDataStatisticDownload(SettleDataStatistic):

    response_type_dict = {'GET': ExcelResponse}

    def clean_get_response(self):
        super().clean_get_response()
        self.response_data = [tuple(self.response_data.values())]
        self.extra_response_data = ['人次', '人数', '总费用（元）', '范围内费用（元）', '统筹基金支出（元）', '大额医疗支出（元）', '大病保险支出（元）', '医疗救助支出（元）', '公务员医疗补助（元）', '其他基金支付（元）', '基金支付总额（元）', '个人现金支付（元）', '个人账户支付（元）', '账户共济支付金额（元）']

class SettleDataMergeDownload(SettleDataMerge):

    is_page = False
    response_type_dict = {'GET': ExcelResponse}

    def clean_get_response(self):
        super().clean_get_response()
        self.response_data = (tuple(i.values()) for i in self.response_data)
        self.extra_response_data = ['序号', '笔数', '证件号码', '人员姓名', '手机号', '乡镇', '村', '总费用', '全自费金额', '超限价自费费用', '先行自付金额', '范围内费用', '起付线', '统筹基金支出', '大额医疗支出金额', '大病保险支出', '医疗救助支出', '公务员医疗补助', '其他基金支付', '基金支付总额', '个人现金支付', '个人账户支付', '账户共济支付金额', '统筹基金支付比例', '人员属性', 'id', '结算ID', '就诊ID', '个人编号', '人员类别', '定点医药机构编号', '定点医药机构名称', '医院等级', '医药机构地点类别', '开始日期', '结束日期', '结算日期', '就诊凭证类型', '病种名称', '医疗类别', '中心报销', '经办人员', '备注', '疾病编码', '是否中途结算', '是否使用账户', '是否有效', '是否冲销', '跨年冲销']