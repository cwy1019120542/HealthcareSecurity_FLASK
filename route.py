from view.insured_data import InsuredData
from view.enumerate_data import EnumerateData
from view.login import Login
from view.settle_data import SettleDataStatistic
from view.user import Password
route_dict = {
    InsuredData: "/api/user/<int:user_id>/insured_data/list",
    EnumerateData: "/api/enumerate_data",
    Login: '/api/login',
    SettleDataStatistic: '/api/user/<int:user_id>/settle_data/statistic',
    Password: '/api/user/<int:user_id>/password',
}