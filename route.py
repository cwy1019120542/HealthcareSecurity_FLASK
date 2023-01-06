from view.insured_data import InsuredDataList, InsuredDataStatistic, InsuredDataListDownload, InsuredDataStatisticDownload
from view.enumerate_data import EnumerateData
from view.login import Login
from view.settle_data import SettleDataList, SettleDataStatistic, SettleDataListDownload, SettleDataStatisticDownload
from view.user import Password
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
}