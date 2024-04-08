from extension import db
from sqlalchemy.dialects.mysql import DOUBLE
from config import EnumerateData

class Person(db.Model):
    __tablename__ = "person"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20))
    id_number = db.Column(db.String(18), unique=True)
    civil_attribute = db.Column(db.Enum(*EnumerateData.civil_attribute))
    orphan_attribute = db.Column(db.Enum(*EnumerateData.orphan_attribute))
    disable_attribute = db.Column(db.Enum(*EnumerateData.disable_attribute))
    treat_attribute = db.Column(db.Enum(*EnumerateData.treat_attribute))
    accident_attribute = db.Column(db.Enum(*EnumerateData.accident_attribute))
    poverty_state = db.Column(db.Enum(*EnumerateData.poverty_state))
    town = db.Column(db.Enum(*EnumerateData.town))
    village = db.Column(db.Enum(*EnumerateData.village))
    phone_number = db.Column(db.String(20))
    family_number = db.Column(db.String(20))
    birthday = db.Column(db.Date)
    sex = db.Column(db.Enum(*EnumerateData.sex))

class InsuredData2019(db.Model):
    __tablename__ = "insured_data_2019"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    resident_self_number = db.Column(db.String(30))
    worker_self_number = db.Column(db.String(30))
    name = db.Column(db.String(20))
    id_number = db.Column(db.String(18), unique=True)
    own_expense = db.Column(db.Integer)
    pay_date = db.Column(db.DateTime)
    insured_state = db.Column(db.Enum(*EnumerateData.insured_state))
    is_civil = db.Column(db.Boolean)
    remark = db.Column(db.String(50))
    is_account_pay = db.Column(db.Boolean)
    town = db.Column(db.Enum(*EnumerateData.town))
    village = db.Column(db.Enum(*EnumerateData.village))

class InsuredData2020(db.Model):
    __tablename__ = "insured_data_2020"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    resident_self_number = db.Column(db.String(30))
    worker_self_number = db.Column(db.String(30))
    name = db.Column(db.String(20))
    id_number = db.Column(db.String(18), unique=True)
    own_expense = db.Column(db.Integer)
    pay_date = db.Column(db.DateTime)
    insured_state = db.Column(db.Enum(*EnumerateData.insured_state))
    is_civil = db.Column(db.Boolean)
    remark = db.Column(db.String(50))
    is_account_pay = db.Column(db.Boolean)
    town = db.Column(db.Enum(*EnumerateData.town))
    village = db.Column(db.Enum(*EnumerateData.village))

class InsuredData2021(db.Model):
    __tablename__ = "insured_data_2021"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    resident_self_number = db.Column(db.String(30))
    worker_self_number = db.Column(db.String(30))
    name = db.Column(db.String(20))
    id_number = db.Column(db.String(18), unique=True)
    own_expense = db.Column(db.Integer)
    pay_date = db.Column(db.DateTime)
    insured_state = db.Column(db.Enum(*EnumerateData.insured_state))
    is_civil = db.Column(db.Boolean)
    remark = db.Column(db.String(50))
    is_account_pay = db.Column(db.Boolean)
    town = db.Column(db.Enum(*EnumerateData.town))
    village = db.Column(db.Enum(*EnumerateData.village))

class InsuredData2022(db.Model):
    __tablename__ = "insured_data_2022"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    resident_self_number = db.Column(db.String(30))
    worker_self_number = db.Column(db.String(30))
    name = db.Column(db.String(20))
    id_number = db.Column(db.String(18), unique=True)
    own_expense = db.Column(db.Integer)
    pay_date = db.Column(db.DateTime)
    insured_state = db.Column(db.Enum(*EnumerateData.insured_state))
    is_civil = db.Column(db.Boolean)
    remark = db.Column(db.String(50))
    is_account_pay = db.Column(db.Boolean)
    town = db.Column(db.Enum(*EnumerateData.town))
    village = db.Column(db.Enum(*EnumerateData.village))


class InsuredData2023(db.Model):
    __tablename__ = "insured_data_2023"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    resident_self_number = db.Column(db.String(30))
    worker_self_number = db.Column(db.String(30))
    name = db.Column(db.String(20))
    id_number = db.Column(db.String(18), unique=True)
    own_expense = db.Column(db.Integer)
    pay_date = db.Column(db.DateTime)
    insured_state = db.Column(db.Enum(*EnumerateData.insured_state))
    is_civil = db.Column(db.Boolean)
    remark = db.Column(db.String(50))
    is_account_pay = db.Column(db.Boolean)
    town = db.Column(db.Enum(*EnumerateData.town))
    village = db.Column(db.Enum(*EnumerateData.village))

class InsuredData2024(db.Model):
    __tablename__ = "insured_data_2024"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    resident_self_number = db.Column(db.String(30))
    worker_self_number = db.Column(db.String(30))
    name = db.Column(db.String(20))
    id_number = db.Column(db.String(18), unique=True)
    own_expense = db.Column(db.Integer)
    pay_date = db.Column(db.DateTime)
    insured_state = db.Column(db.Enum(*EnumerateData.insured_state))
    is_civil = db.Column(db.Boolean)
    remark = db.Column(db.String(50))
    is_account_pay = db.Column(db.Boolean)
    town = db.Column(db.Enum(*EnumerateData.town))
    village = db.Column(db.Enum(*EnumerateData.village))

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20))
    phone_number = db.Column(db.String(20), unique=True)
    qq = db.Column(db.String(20))
    town = db.Column(db.Enum(*EnumerateData.town))
    password = db.Column(db.String(20))
    identity = db.Column(db.Enum(*EnumerateData.identity))
    is_available = db.Column(db.Boolean)

class SettleData2019(db.Model):
    __tablename__ = "settle_data_2019"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    settle_id = db.Column(db.String(30))
    cure_id = db.Column(db.String(30))
    self_number = db.Column(db.String(30))
    name = db.Column(db.String(20))
    id_number = db.Column(db.String(18))
    person_type = db.Column(db.Enum(*EnumerateData.person_type))
    hospital_id = db.Column(db.String(20))
    hospital_name = db.Column(db.String(80))
    hospital_level = db.Column(db.Enum(*EnumerateData.hospital_level))
    hospital_place = db.Column(db.Enum(*EnumerateData.hospital_place))
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    settle_date = db.Column(db.DateTime)
    evidence_type = db.Column(db.Enum(*EnumerateData.evidence_type))
    all_expense = db.Column(DOUBLE)
    self_expense = db.Column(DOUBLE)
    over_expense = db.Column(DOUBLE)
    first_expense = db.Column(DOUBLE)
    inner_expense = db.Column(DOUBLE)
    start_pay = db.Column(DOUBLE)
    overall_pay = db.Column(DOUBLE)
    large_pay = db.Column(DOUBLE)
    big_pay = db.Column(DOUBLE)
    rescue_pay = db.Column(DOUBLE)
    civil_pay = db.Column(DOUBLE)
    other_pay = db.Column(DOUBLE)
    all_pay = db.Column(DOUBLE)
    cash_pay = db.Column(DOUBLE)
    account_pay = db.Column(DOUBLE)
    together_pay = db.Column(DOUBLE)
    illness_name = db.Column(db.String(70))
    cure_type = db.Column(db.Enum(*EnumerateData.cure_type))
    overall_percent = db.Column(DOUBLE)
    is_centre = db.Column(db.Boolean)
    operator = db.Column(db.String(20))
    remark = db.Column(db.String(50))
    town = db.Column(db.Enum(*EnumerateData.town))
    village = db.Column(db.Enum(*EnumerateData.village))
    illness_number = db.Column(db.String(30))
    is_mid_settle = db.Column(db.Boolean)
    is_use_account = db.Column(db.Boolean)
    is_valid = db.Column(db.Boolean)
    is_refund = db.Column(db.Boolean)
    overyear_refund = db.Column(db.Enum(*EnumerateData.overyear_refund))
    in_department = db.Column(db.String(50))
    out_department = db.Column(db.String(50))
    in_bed = db.Column(db.String(30))
    illness_bed = db.Column(db.String(30))
    out_bed = db.Column(db.String(30))
    in_diagnose = db.Column(db.String(70))
    doctor_id = db.Column(db.String(30))
    doctor_name = db.Column(db.String(30))
    out_diagnose_id = db.Column(db.String(30))
    out_diagnose = db.Column(db.String(70))
    in_id = db.Column(db.String(30))

class SettleData2020(db.Model):
    __tablename__ = "settle_data_2020"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    settle_id = db.Column(db.String(30))
    cure_id = db.Column(db.String(30))
    self_number = db.Column(db.String(30))
    name = db.Column(db.String(20))
    id_number = db.Column(db.String(18))
    person_type = db.Column(db.Enum(*EnumerateData.person_type))
    hospital_id = db.Column(db.String(20))
    hospital_name = db.Column(db.String(80))
    hospital_level = db.Column(db.Enum(*EnumerateData.hospital_level))
    hospital_place = db.Column(db.Enum(*EnumerateData.hospital_place))
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    settle_date = db.Column(db.DateTime)
    evidence_type = db.Column(db.Enum(*EnumerateData.evidence_type))
    all_expense = db.Column(DOUBLE)
    self_expense = db.Column(DOUBLE)
    over_expense = db.Column(DOUBLE)
    first_expense = db.Column(DOUBLE)
    inner_expense = db.Column(DOUBLE)
    start_pay = db.Column(DOUBLE)
    overall_pay = db.Column(DOUBLE)
    large_pay = db.Column(DOUBLE)
    big_pay = db.Column(DOUBLE)
    rescue_pay = db.Column(DOUBLE)
    civil_pay = db.Column(DOUBLE)
    other_pay = db.Column(DOUBLE)
    all_pay = db.Column(DOUBLE)
    cash_pay = db.Column(DOUBLE)
    account_pay = db.Column(DOUBLE)
    together_pay = db.Column(DOUBLE)
    illness_name = db.Column(db.String(70))
    cure_type = db.Column(db.Enum(*EnumerateData.cure_type))
    overall_percent = db.Column(DOUBLE)
    is_centre = db.Column(db.Boolean)
    operator = db.Column(db.String(20))
    remark = db.Column(db.String(50))
    town = db.Column(db.Enum(*EnumerateData.town))
    village = db.Column(db.Enum(*EnumerateData.village))
    illness_number = db.Column(db.String(30))
    is_mid_settle = db.Column(db.Boolean)
    is_use_account = db.Column(db.Boolean)
    is_valid = db.Column(db.Boolean)
    is_refund = db.Column(db.Boolean)
    overyear_refund = db.Column(db.Enum(*EnumerateData.overyear_refund))
    in_department = db.Column(db.String(30))
    out_department = db.Column(db.String(30))
    in_bed = db.Column(db.String(30))
    illness_bed = db.Column(db.String(30))
    out_bed = db.Column(db.String(30))
    in_diagnose = db.Column(db.String(70))
    doctor_id = db.Column(db.String(30))
    doctor_name = db.Column(db.String(30))
    out_diagnose_id = db.Column(db.String(30))
    out_diagnose = db.Column(db.String(70))
    in_id = db.Column(db.String(30))

class SettleData2021(db.Model):
    __tablename__ = "settle_data_2021"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    settle_id = db.Column(db.String(30))
    cure_id = db.Column(db.String(30))
    self_number = db.Column(db.String(30))
    name = db.Column(db.String(20))
    id_number = db.Column(db.String(18))
    person_type = db.Column(db.Enum(*EnumerateData.person_type))
    hospital_id = db.Column(db.String(20))
    hospital_name = db.Column(db.String(80))
    hospital_level = db.Column(db.Enum(*EnumerateData.hospital_level))
    hospital_place = db.Column(db.Enum(*EnumerateData.hospital_place))
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    settle_date = db.Column(db.DateTime)
    evidence_type = db.Column(db.Enum(*EnumerateData.evidence_type))
    all_expense = db.Column(DOUBLE)
    self_expense = db.Column(DOUBLE)
    over_expense = db.Column(DOUBLE)
    first_expense = db.Column(DOUBLE)
    inner_expense = db.Column(DOUBLE)
    start_pay = db.Column(DOUBLE)
    overall_pay = db.Column(DOUBLE)
    large_pay = db.Column(DOUBLE)
    big_pay = db.Column(DOUBLE)
    rescue_pay = db.Column(DOUBLE)
    civil_pay = db.Column(DOUBLE)
    other_pay = db.Column(DOUBLE)
    all_pay = db.Column(DOUBLE)
    cash_pay = db.Column(DOUBLE)
    account_pay = db.Column(DOUBLE)
    together_pay = db.Column(DOUBLE)
    illness_name = db.Column(db.String(70))
    cure_type = db.Column(db.Enum(*EnumerateData.cure_type))
    overall_percent = db.Column(DOUBLE)
    is_centre = db.Column(db.Boolean)
    operator = db.Column(db.String(20))
    remark = db.Column(db.String(50))
    town = db.Column(db.Enum(*EnumerateData.town))
    village = db.Column(db.Enum(*EnumerateData.village))
    illness_number = db.Column(db.String(30))
    is_mid_settle = db.Column(db.Boolean)
    is_use_account = db.Column(db.Boolean)
    is_valid = db.Column(db.Boolean)
    is_refund = db.Column(db.Boolean)
    overyear_refund = db.Column(db.Enum(*EnumerateData.overyear_refund))
    in_department = db.Column(db.String(30))
    out_department = db.Column(db.String(30))
    in_bed = db.Column(db.String(30))
    illness_bed = db.Column(db.String(30))
    out_bed = db.Column(db.String(30))
    in_diagnose = db.Column(db.String(70))
    doctor_id = db.Column(db.String(30))
    doctor_name = db.Column(db.String(30))
    out_diagnose_id = db.Column(db.String(30))
    out_diagnose = db.Column(db.String(70))
    in_id = db.Column(db.String(30))

class SettleData2022(db.Model):
    __tablename__ = "settle_data_2022"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    settle_id = db.Column(db.String(30))
    cure_id = db.Column(db.String(30))
    self_number = db.Column(db.String(30))
    name = db.Column(db.String(20))
    id_number = db.Column(db.String(18))
    person_type = db.Column(db.Enum(*EnumerateData.person_type))
    hospital_id = db.Column(db.String(20))
    hospital_name = db.Column(db.String(80))
    hospital_level = db.Column(db.Enum(*EnumerateData.hospital_level))
    hospital_place = db.Column(db.Enum(*EnumerateData.hospital_place))
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    settle_date = db.Column(db.DateTime)
    evidence_type = db.Column(db.Enum(*EnumerateData.evidence_type))
    all_expense = db.Column(DOUBLE)
    self_expense = db.Column(DOUBLE)
    over_expense = db.Column(DOUBLE)
    first_expense = db.Column(DOUBLE)
    inner_expense = db.Column(DOUBLE)
    start_pay = db.Column(DOUBLE)
    overall_pay = db.Column(DOUBLE)
    large_pay = db.Column(DOUBLE)
    big_pay = db.Column(DOUBLE)
    rescue_pay = db.Column(DOUBLE)
    civil_pay = db.Column(DOUBLE)
    other_pay = db.Column(DOUBLE)
    all_pay = db.Column(DOUBLE)
    cash_pay = db.Column(DOUBLE)
    account_pay = db.Column(DOUBLE)
    together_pay = db.Column(DOUBLE)
    illness_name = db.Column(db.String(70))
    cure_type = db.Column(db.Enum(*EnumerateData.cure_type))
    overall_percent = db.Column(DOUBLE)
    is_centre = db.Column(db.Boolean)
    operator = db.Column(db.String(20))
    remark = db.Column(db.String(50))
    town = db.Column(db.Enum(*EnumerateData.town))
    village = db.Column(db.Enum(*EnumerateData.village))
    illness_number = db.Column(db.String(30))
    is_mid_settle = db.Column(db.Boolean)
    is_use_account = db.Column(db.Boolean)
    is_valid = db.Column(db.Boolean)
    is_refund = db.Column(db.Boolean)
    overyear_refund = db.Column(db.Enum(*EnumerateData.overyear_refund))
    in_department = db.Column(db.String(30))
    out_department = db.Column(db.String(30))
    in_bed = db.Column(db.String(30))
    illness_bed = db.Column(db.String(30))
    out_bed = db.Column(db.String(30))
    in_diagnose = db.Column(db.String(70))
    doctor_id = db.Column(db.String(30))
    doctor_name = db.Column(db.String(30))
    out_diagnose_id = db.Column(db.String(30))
    out_diagnose = db.Column(db.String(70))
    in_id = db.Column(db.String(30))

class SettleData2023(db.Model):
    __tablename__ = "settle_data_2023"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    settle_id = db.Column(db.String(30))
    cure_id = db.Column(db.String(30))
    self_number = db.Column(db.String(30))
    name = db.Column(db.String(20))
    id_number = db.Column(db.String(18))
    person_type = db.Column(db.Enum(*EnumerateData.person_type))
    hospital_id = db.Column(db.String(20))
    hospital_name = db.Column(db.String(80))
    hospital_level = db.Column(db.Enum(*EnumerateData.hospital_level))
    hospital_place = db.Column(db.Enum(*EnumerateData.hospital_place))
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    settle_date = db.Column(db.DateTime)
    evidence_type = db.Column(db.Enum(*EnumerateData.evidence_type))
    all_expense = db.Column(DOUBLE)
    self_expense = db.Column(DOUBLE)
    over_expense = db.Column(DOUBLE)
    first_expense = db.Column(DOUBLE)
    inner_expense = db.Column(DOUBLE)
    start_pay = db.Column(DOUBLE)
    overall_pay = db.Column(DOUBLE)
    large_pay = db.Column(DOUBLE)
    big_pay = db.Column(DOUBLE)
    rescue_pay = db.Column(DOUBLE)
    civil_pay = db.Column(DOUBLE)
    other_pay = db.Column(DOUBLE)
    all_pay = db.Column(DOUBLE)
    cash_pay = db.Column(DOUBLE)
    account_pay = db.Column(DOUBLE)
    together_pay = db.Column(DOUBLE)
    illness_name = db.Column(db.String(70))
    cure_type = db.Column(db.Enum(*EnumerateData.cure_type))
    overall_percent = db.Column(DOUBLE)
    is_centre = db.Column(db.Boolean)
    operator = db.Column(db.String(20))
    remark = db.Column(db.String(50))
    town = db.Column(db.Enum(*EnumerateData.town))
    village = db.Column(db.Enum(*EnumerateData.village))
    illness_number = db.Column(db.String(30))
    is_mid_settle = db.Column(db.Boolean)
    is_use_account = db.Column(db.Boolean)
    is_valid = db.Column(db.Boolean)
    is_refund = db.Column(db.Boolean)
    overyear_refund = db.Column(db.Enum(*EnumerateData.overyear_refund))
    in_department = db.Column(db.String(30))
    out_department = db.Column(db.String(30))
    in_bed = db.Column(db.String(30))
    illness_bed = db.Column(db.String(30))
    out_bed = db.Column(db.String(30))
    in_diagnose = db.Column(db.String(70))
    doctor_id = db.Column(db.String(30))
    doctor_name = db.Column(db.String(30))
    out_diagnose_id = db.Column(db.String(30))
    out_diagnose = db.Column(db.String(70))
    in_id = db.Column(db.String(30))

class SettleData2024(db.Model):
    __tablename__ = "settle_data_2024"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    settle_id = db.Column(db.String(30))
    cure_id = db.Column(db.String(30))
    self_number = db.Column(db.String(30))
    name = db.Column(db.String(20))
    id_number = db.Column(db.String(18))
    person_type = db.Column(db.Enum(*EnumerateData.person_type))
    hospital_id = db.Column(db.String(20))
    hospital_name = db.Column(db.String(80))
    hospital_level = db.Column(db.Enum(*EnumerateData.hospital_level))
    hospital_place = db.Column(db.Enum(*EnumerateData.hospital_place))
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    settle_date = db.Column(db.DateTime)
    evidence_type = db.Column(db.Enum(*EnumerateData.evidence_type))
    all_expense = db.Column(DOUBLE)
    self_expense = db.Column(DOUBLE)
    over_expense = db.Column(DOUBLE)
    first_expense = db.Column(DOUBLE)
    inner_expense = db.Column(DOUBLE)
    start_pay = db.Column(DOUBLE)
    overall_pay = db.Column(DOUBLE)
    large_pay = db.Column(DOUBLE)
    big_pay = db.Column(DOUBLE)
    rescue_pay = db.Column(DOUBLE)
    civil_pay = db.Column(DOUBLE)
    other_pay = db.Column(DOUBLE)
    all_pay = db.Column(DOUBLE)
    cash_pay = db.Column(DOUBLE)
    account_pay = db.Column(DOUBLE)
    together_pay = db.Column(DOUBLE)
    illness_name = db.Column(db.String(70))
    cure_type = db.Column(db.Enum(*EnumerateData.cure_type))
    overall_percent = db.Column(DOUBLE)
    is_centre = db.Column(db.Boolean)
    operator = db.Column(db.String(20))
    remark = db.Column(db.String(50))
    town = db.Column(db.Enum(*EnumerateData.town))
    village = db.Column(db.Enum(*EnumerateData.village))
    illness_number = db.Column(db.String(30))
    is_mid_settle = db.Column(db.Boolean)
    is_use_account = db.Column(db.Boolean)
    is_valid = db.Column(db.Boolean)
    is_refund = db.Column(db.Boolean)
    overyear_refund = db.Column(db.Enum(*EnumerateData.overyear_refund))
    in_department = db.Column(db.String(30))
    out_department = db.Column(db.String(30))
    in_bed = db.Column(db.String(30))
    illness_bed = db.Column(db.String(30))
    out_bed = db.Column(db.String(30))
    in_diagnose = db.Column(db.String(70))
    doctor_id = db.Column(db.String(30))
    doctor_name = db.Column(db.String(30))
    out_diagnose_id = db.Column(db.String(30))
    out_diagnose = db.Column(db.String(70))
    in_id = db.Column(db.String(30))

class Staff(db.Model):
    __tablename__ = "staff"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20))
    id_number = db.Column(db.String(20), unique=True)
    work_number = db.Column(db.String(5), unique=True)
    department = db.Column(db.Enum(*EnumerateData.department))
    position = db.Column(db.Enum(*EnumerateData.position))
    education = db.Column(db.Enum(*EnumerateData.education))
    phone_number = db.Column(db.String(20))
    enter_date = db.Column(db.Date)
    is_available = db.Column(db.Boolean)

class CheckData(db.Model):
    __tablename__ = "check_data"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    year = db.Column(db.Enum(*EnumerateData.year))
    id_number = db.Column(db.String(20))
    operate_type = db.Column(db.Enum(*EnumerateData.operate_type))
    check_type =  db.Column(db.Enum(*EnumerateData.check_type))
    check_source = db.Column(db.Enum(*EnumerateData.check_source))
    get_point = db.Column(db.Float, default=0)
    lost_point = db.Column(db.Float, default=0)
    check_date = db.Column(db.Date)
    remark = db.Column(db.String(50))
    operator = db.Column(db.String(20))
    operate_date = db.Column(db.DateTime)
    attachment_id = db.Column(db.String(50))

class NumberData(db.Model):
    __tablename__ = "number_data"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    self_number = db.Column(db.String(30), unique=True)
    id_number = db.Column(db.String(18))

class NotifyData(db.Model):
    __tablename__ = "notify_data"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(10))
    content = db.Column(db.String(50))
    is_available = db.Column(db.Boolean)
    operate_date = db.Column(db.Date)

class ChronicIllness(db.Model):
    __tablename__ = "chronic_illness"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_number = db.Column(db.String(18))
    illness_name = db.Column(db.String(20))
    illness_number = db.Column(db.String(30))
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    hospital_id = db.Column(db.String(20))
    hospital_name = db.Column(db.String(80))
    hospital_place = db.Column(db.Enum(*EnumerateData.hospital_place))
    person_type_simple = db.Column(db.Enum(*EnumerateData.person_type_simple))
    illness_type = db.Column(db.Enum(*EnumerateData.illness_type))
    identify_date = db.Column(db.Date)
    apply_date = db.Column(db.Date)
    operator = db.Column(db.String(20))
    operate_date = db.Column(db.DateTime)
    is_valid = db.Column(db.Boolean)
    apply_source = db.Column(db.Enum(*EnumerateData.apply_source))

model_dict = {
    "person": Person,
    "insured_data_2019": InsuredData2019,
    "insured_data_2020": InsuredData2020,
    "insured_data_2021": InsuredData2021,
    "insured_data_2022": InsuredData2022,
    "insured_data_2023": InsuredData2023,
    "insured_data_2024": InsuredData2024,
    'user': User,
    'settle_data_2019': SettleData2019,
    'settle_data_2020': SettleData2020,
    'settle_data_2021': SettleData2021,
    'settle_data_2022': SettleData2022,
    'settle_data_2023': SettleData2023,
    'settle_data_2024': SettleData2024,
    'staff': Staff,
    'check_data': CheckData,
    'notify_data': NotifyData,
    'chronic_illness': ChronicIllness,
}