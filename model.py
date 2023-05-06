from extension import db
from sqlalchemy.dialects.mysql import DOUBLE
from config import EnumerateData

def clean_illness_name(illness_name):
    return illness_name.replace('�?', '').replace('\x00', '') if illness_name else ''

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


class InsuredData2022(db.Model):
    __tablename__ = "insured_data_2022"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    self_number = db.Column(db.String(30))
    id_number = db.Column(db.String(18), unique=True)
    own_expense = db.Column(db.Integer)
    pay_date = db.Column(db.DateTime)
    insured_state = db.Column(db.Enum(*EnumerateData.insured_state))
    is_civil = db.Column(db.Boolean)
    remark = db.Column(db.String(50))
    is_account_pay = db.Column(db.Boolean)


class InsuredData2023(db.Model):
    __tablename__ = "insured_data_2023"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    self_number = db.Column(db.String(30))
    id_number = db.Column(db.String(18), unique=True)
    own_expense = db.Column(db.Integer)
    pay_date = db.Column(db.DateTime)
    insured_state = db.Column(db.Enum(*EnumerateData.insured_state))
    is_civil = db.Column(db.Boolean)
    remark = db.Column(db.String(50))
    is_account_pay = db.Column(db.Boolean)


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

    def dict_response(self):
        return {
            "id": self.id,
            "phone_number": self.phone_number,
            'qq': self.qq,
            "name" : self.name,
            "town" : self.town,
            "identity": self.identity,
            "authority": EnumerateData.authority[self.identity],
            'is_available': self.is_available,
        }

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
    hospital_name = db.Column(db.String(50))
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
    hospital_name = db.Column(db.String(50))
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

model_dict = {
    "person": Person,
    "insured_data_2022": InsuredData2022,
    "insured_data_2023": InsuredData2023,
    'user': User,
    'settle_data_2022': SettleData2022,
    'settle_data_2023': SettleData2023,
    'staff': Staff,
    'check_data': CheckData,
}