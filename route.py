from view.insured_data import InsuredDataList, InsuredDataStatistic, InsuredDataListDownload, InsuredDataStatisticDownload
from view.enumerate_data import EnumerateData
from view.insured_rate import InsuredRate, SpecialInsuredRate
from view.login import Login
from view.settle_data import SettleDataList, SettleDataStatistic, SettleDataListDownload, SettleDataStatisticDownload, SettleDataMerge, SettleDataMergeDownload
from view.check_data import StaffList, CheckDataList, StaffListDownload, CheckDataListDownload, CheckAttachment
from view.notify_data import NotifyData
from view.user import Password
from view.civil_pay import CivilPayList, CivilPayListDownload
route_dict = {
    InsuredDataList: "/api/user/<int:user_id>/insured_data/list",
    InsuredDataStatistic: "/api/user/<int:user_id>/insured_data/statistic",
    InsuredDataListDownload: "/api/user/<int:user_id>/insured_data/list/download",
    InsuredDataStatisticDownload: "/api/user/<int:user_id>/insured_data/statistic/download",
    EnumerateData: "/api/enumerate_data",
    Login: '/api/login',
    SettleDataList: '/api/user/<int:user_id>/settle_data/list',
    SettleDataStatistic: '/api/user/<int:user_id>/settle_data/statistic',
    SettleDataListDownload: '/api/user/<int:user_id>/settle_data/list/download',
    SettleDataStatisticDownload: '/api/user/<int:user_id>/settle_data/statistic/download',
    Password: '/api/user/<int:user_id>/password',
    InsuredRate: '/api/user/<int:user_id>/insured_rate/',
    SpecialInsuredRate: '/api/user/<int:user_id>/special_insured_rate',
    SettleDataMerge: '/api/user/<int:user_id>/settle_data/merge',
    SettleDataMergeDownload: '/api/user/<int:user_id>/settle_data/merge/download',
    StaffList: '/api/user/<int:user_id>/staff/list',
    StaffListDownload: '/api/user/<int:user_id>/staff/list/download',
    CheckDataList: '/api/user/<int:user_id>/check_data/list',
    CheckDataListDownload: '/api/user/<int:user_id>/check_data/list/download',
    CheckAttachment: '/api/user/<int:user_id>/check_attachment',
    NotifyData: '/api/notify_data',
    CivilPayList: '/api/user/<int:user_id>/civil_pay/list',
    CivilPayListDownload: '/api/user/<int:user_id>/civil_pay/list/download',
}