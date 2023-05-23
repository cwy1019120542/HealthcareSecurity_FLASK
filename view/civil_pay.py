from .base import Base
from response import ExcelResponse, OK
from sqlalchemy.sql import func
from model import model_dict
from flask import abort
from config import Config

class CivilPayList(Base):

    methods = ['get']
    model_name = 'settle_data'
    entities_dict = {'model': ['id', 'settle_id', 'cure_id', 'self_number', 'name', 'id_number', 'person_type', 'hospital_id', 'hospital_name', 'hospital_level', 'hospital_place', 'start_date', 'end_date', 'settle_date', 'evidence_type', 'all_expense', 'self_expense', 'over_expense', 'first_expense', 'inner_expense', 'start_pay', 'overall_pay', 'large_pay', 'big_pay', 'rescue_pay', 'civil_pay', 'other_pay', 'all_pay', 'cash_pay', 'account_pay', 'together_pay', 'illness_name', 'cure_type', 'overall_percent', 'is_centre', 'operator', 'town', 'village', 'remark']}
    allowed_parameter = {'GET': {'id_number': ('str', None, "settle_data", True, 18), 'year': ("enum", None, '', True, None), "settle_date": ("combine_date", None, 'settle_data', False, None)}}
    decimal_field_list = (
    'all_expense', 'self_expense', 'over_expense', 'first_expense', 'inner_expense', 'start_pay', 'overall_pay',
    'large_pay', 'big_pay', 'rescue_pay', 'civil_pay', 'other_pay', 'all_pay', 'cash_pay', 'account_pay',
    'together_pay', 'overall_percent')

    def make_get_query(self):
        self.parameter_dict[self.model_name]['cure_type'] = ['双通道购药', '普通住院', '无法确定他方责任的意外伤害（外伤住院）', '转外诊治住院', '急诊转住院', '单病种住院', '日间手术', '同病同保障住院', '床日费用住院', '门诊慢性病', '门诊特殊病', '计划生育住院', '门诊单病种', '日间病床', '无他方责任意外伤害住院', '分疗程间断住院治疗']
        super().make_get_query()

    def clean_get_response(self):
        super().clean_get_response()
        start_civil_pay = 400
        start_inner_pay = 5000
        all_inner_pay = 0
        all_out_pay = 0
        all_all_expense = 0
        all_inner_expense = 0
        all_all_pay = 0
        all_overall_pay = 0
        all_large_pay = 0
        all_cash_pay = 0
        all_account_pay = 0
        for data_index, data_group in enumerate(self.response_data, 1):
            data_group['number'] = data_index
            for key in self.decimal_field_list:
                data_group[key] = self.to_float(data_group[key])
            for key in ('start_date', 'end_date', 'settle_date'):
                data_group[key] = self.to_string_date(data_group[key])
            all_expense = data_group['all_expense']
            all_all_expense += all_expense
            first_expense = data_group['first_expense']
            inner_expense = data_group['inner_expense']
            all_inner_expense += inner_expense
            start_pay = data_group['start_pay']
            all_pay = data_group['all_pay']
            all_all_pay += all_pay
            overall_pay = data_group['overall_pay']
            all_overall_pay += overall_pay
            large_pay = data_group['large_pay']
            all_large_pay += large_pay
            overall_large_pay = overall_pay + large_pay
            cash_pay = data_group['cash_pay']
            all_cash_pay += cash_pay
            account_pay = data_group['account_pay']
            all_account_pay += account_pay
            cure_type = data_group['cure_type']
            overall_percent = data_group['overall_percent']
            base_expense = all_expense - start_pay
            base_inner_expense = inner_expense - start_pay
            civil_inner_expense = inner_expense - all_pay
            civil_out_expense = all_expense - inner_expense
            system_overall_pay = (inner_expense - start_pay) * overall_percent
            if cure_type in ('门诊慢性病', '门诊特殊病'):
                civil_pay_type = '慢特病'
            else:
                if overall_percent:
                    if abs(system_overall_pay - overall_large_pay) < 0.01:
                        civil_pay_type = '正常住院'
                    elif system_overall_pay - overall_large_pay > 0.01:
                        if base_expense * 0.69 <= base_inner_expense:
                            civil_pay_type = '正常住院(超封顶线)'
                        else:
                            civil_pay_type = '保底报销(超封顶线)?'
                    else:
                        civil_pay_type = '保底报销'
                else:
                    if base_expense <= 0:
                        if all_expense * 0.69 <= inner_expense:
                            civil_pay_type = '正常住院(未达起付线)'
                        else:
                            civil_pay_type = '保底报销(未达起付线)?'
                    else:
                        if overall_large_pay / base_expense > 0.45:
                            civil_pay_type = '正常住院(统筹基金支出比例错误)'
                        else:
                            civil_pay_type = '保底报销(统筹基金支出比例错误)'
            if civil_inner_expense <= 0:
                civil_inner_expense = 0
                civil_out_expense = cash_pay + account_pay
                civil_pay_type += '(基金总支付大于范围内费用)'
            else:
                if '慢特病' in civil_pay_type:
                    civil_out_expense = first_expense
                elif '保底报销' in civil_pay_type:
                    civil_inner_expense = 0
            data_group['start_civil_pay'] = self.to_float(start_civil_pay)
            data_group['start_inner_pay'] = self.to_float(start_inner_pay)
            civil_inner_expense -= start_civil_pay
            if civil_inner_expense <= 0:
                civil_inner_pay = 0
                start_civil_pay = -civil_inner_expense
            else:
                start_civil_pay = 0
                civil_inner_expense -= start_inner_pay
                if civil_inner_expense <= 0:
                    civil_inner_pay = (civil_inner_expense + start_inner_pay) * 0.75
                    start_inner_pay = -civil_inner_expense
                else:
                    civil_inner_pay = civil_inner_expense * 0.85 + start_inner_pay * 0.75
                    start_inner_pay = 0
            civil_out_expense -= start_civil_pay
            if civil_out_expense <= 0:
                civil_out_pay = 0
                start_civil_pay = -civil_out_expense
            else:
                civil_out_pay = civil_out_expense * 0.5
                start_civil_pay = 0
            data_group['civil_pay_type'] = civil_pay_type
            data_group['civil_inner_pay'] = self.to_float(civil_inner_pay)
            data_group['civil_out_pay'] = self.to_float(civil_out_pay)
            data_group['civil_all_pay'] = data_group['civil_inner_pay'] + data_group['civil_out_pay']
            all_inner_pay += data_group['civil_inner_pay']
            all_out_pay += data_group['civil_out_pay']
        all_civil_pay = all_inner_pay + all_out_pay
        self.response_data.append({'name': '合计', 'civil_all_pay': self.to_float(all_civil_pay), 'civil_inner_pay': self.to_float(all_inner_pay), 'civil_out_pay': self.to_float(all_out_pay),
                                   'all_expense': self.to_float(all_all_expense), 'inner_expense': self.to_float(all_inner_expense), 'all_pay': self.to_float(all_all_pay), 'overall_pay': self.to_float(all_overall_pay), 'large_pay': self.to_float(all_large_pay), 'cash_pay': self.to_float(all_cash_pay), 'account_pay': self.to_float(all_account_pay)})

class CivilPayListDownload(CivilPayList):

    response_type_dict = {'GET': ExcelResponse}

    def clean_get_response(self):
        super().clean_get_response()
        self.response_data = (tuple(i.values()) for i in self.response_data)
        self.extra_response_data = ['id', '结算ID', '就诊ID', '个人编号', '人员姓名', '证件号码', '人员类别', '定点医药机构编号', '定点医药机构名称', '医院等级',
                                    '医药机构地点类别', '开始日期', '结束日期', '结算日期', '就诊凭证类型', '总费用', '全自费金额', '超限价自费费用', '先行自付金额',
                                    '范围内费用', '起付线', '统筹基金支出', '大额医疗支出金额', '大病保险支出', '医疗救助支出', '公务员医疗补助', '其他基金支付',
                                    '基金支付总额', '个人现金支付', '个人账户支付', '账户共济支付金额', '病种名称', '医疗类别', '统筹基金支付比例', '中心报销',
                                    '经办人员', '乡镇', '村', '备注', '公务员医疗补助起付线', '公务员医疗补助范围内分段额度', '公务员医疗补助拨付类型', '公务员医疗补助范围内拨付', '公务员医疗补助范围外拨付', '公务员医疗补助总拨付']