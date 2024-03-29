from view.insured_data import InsuredDataList, InsuredDataStatistic, InsuredDataListDownload, InsuredDataStatisticDownload
from view.enumerate_data import EnumerateData
from view.insured_rate import InsuredRate, SpecialInsuredRate, InsuredRateDownload, SpecialInsuredRateDownload
from view.login import Login
from view.settle_data import SettleDataList, SettleDataStatistic, SettleDataListDownload, SettleDataStatisticDownload, SettleDataMerge, SettleDataMergeDownload
from view.check_data import StaffList, CheckDataList, StaffListDownload, CheckDataListDownload, CheckAttachment
from view.notify_data import NotifyData
from view.user import Password
from view.civil_pay import CivilPayList, CivilPayListDownload
from view.open_data import OpenDataHospitalListDownload, OpenDataPayListDownload, OpenDataRescueListDownload
from view.settle_rate import SettleRate, SettleRateDownload
from view.chronic_illness import ChronicIllnessList, ChronicIllnessStatistic, ChronicIllnessListDownload, ChronicIllnessStatisticDownload, ChronicIllnessCard
from view.evidence_rate import EvidenceRate, EvidenceRateDownload
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
    InsuredRateDownload: '/api/user/<int:user_id>/insured_rate/download',
    SpecialInsuredRate: '/api/user/<int:user_id>/special_insured_rate',
    SpecialInsuredRateDownload: '/api/user/<int:user_id>/special_insured_rate/download',
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
    OpenDataHospitalListDownload: '/api/user/<int:user_id>/open_data/hospital/list/download',
    OpenDataPayListDownload: '/api/user/<int:user_id>/open_data/pay/list/download',
    OpenDataRescueListDownload: '/api/user/<int:user_id>/open_data/rescue/list/download',
    SettleRate: '/api/user/<int:user_id>/settle_rate',
    SettleRateDownload: '/api/user/<int:user_id>/settle_rate/download',
    ChronicIllnessList: '/api/user/<int:user_id>/chronic_illness/list',
    ChronicIllnessStatistic: '/api/user/<int:user_id>/chronic_illness/statistic',
    ChronicIllnessListDownload: '/api/user/<int:user_id>/chronic_illness/list/download',
    ChronicIllnessStatisticDownload: '/api/user/<int:user_id>/chronic_illness/statistic/download',
    ChronicIllnessCard: '/api/user/<int:user_id>/chronic_illness/card',
    EvidenceRate: '/api/user/<int:user_id>/evidence_rate',
    EvidenceRateDownload: '/api/user/<int:user_id>/evidence_rate/download',
}