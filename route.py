from view.insured_data import InsuredDataList, InsuredDataStatistic, InsuredDataListDownload, InsuredDataStatisticDownload
from view.enumerate_data import EnumerateData
from view.insured_rate import InsuredRate, SpecialInsuredRate
from view.login import Login
from view.settle_data import SettleDataList, SettleDataStatistic, SettleDataListDownload, SettleDataStatisticDownload, SettleDataMerge, SettleDataMergeDownload
from view.check_data import Staff, CheckData
from view.user import Password
from view.base import BaseFile
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
    Staff: '/api/user/<int:user_id>/staff/list',
    CheckData: '/api/user/<int:user_id>/check_data/list',
    BaseFile: '/api/user/<int:user_id>/attachment',
}