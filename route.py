from view.insured_data import InsuredDataList
from view.enumerate_data import EnumerateData
from view.login import Login
from view.settle_data import SettleDataList
from view.settle_data import SettleDataStatistic
from view.user import Password
route_dict = {
    InsuredDataList: "/api/user/<int:user_id>/insured_data/list",
    EnumerateData: "/api/enumerate_data",
    Login: '/api/login',
    SettleDataList: '/api/user/<int:user_id>/settle_data/list',
    SettleDataStatistic: '/api/user/<int:user_id>/settle_data/statistic',
    Password: '/api/user/<int:user_id>/password',
}