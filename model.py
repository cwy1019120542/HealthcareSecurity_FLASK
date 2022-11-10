from extension import db
from sqlalchemy.dialects.mysql import DOUBLE
from config import EnumerateData

class InsuredData2021(db.Model):
    __tablename__ = "insured_data_2021"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20))
    id_number = db.Column(db.String(18), unique=True)
    own_expense = db.Column(db.Float)
    pay_date = db.Column(db.DateTime)
    insured_state = db.Column(db.Enum(*EnumerateData.insured_state))
    insured_area = db.Column(db.Enum(*EnumerateData.insured_area))
    attribute = db.Column(db.Enum(*EnumerateData.attribute))
    second_attribute = db.Column(db.Enum(*EnumerateData.second_attribute))
    poverty_state = db.Column(db.Enum(*EnumerateData.poverty_state))
    town = db.Column(db.Enum(*EnumerateData.town))
    village = db.Column(db.Enum(*EnumerateData.village))
    phone_number = db.Column(db.String(20))
    source = db.Column(db.Enum(*EnumerateData.source))
    update_date = db.Column(db.DateTime)
    update_user = db.Column(db.String(20))
    remark = db.Column(db.String(100))

    def data_response(self, number):
        return {
            "number": number,
            "id": self.id,
            "name" : self.name,
            "id_number" : self.id_number,
            "own_expense": self.own_expense,
            "insured_state" : self.insured_state,
            "insured_area" : self.insured_area,
            "attribute" : self.attribute,
            "second_attribute": self.second_attribute,
            "poverty_state" : self.poverty_state,
            "town" : self.town,
            "village" : self.village,
            "phone_number" : self.phone_number,
            "update_date" : self.update_date.strftime("%Y-%m-%d") if self.update_date else '',
            "update_user" : self.update_user
        }

class InsuredData2022(db.Model):
    __tablename__ = "insured_data_2022"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20))
    id_number = db.Column(db.String(18), unique=True)
    own_expense = db.Column(db.Float)
    pay_date = db.Column(db.DateTime)
    insured_state = db.Column(db.Enum(*EnumerateData.insured_state))
    insured_area = db.Column(db.Enum(*EnumerateData.insured_area))
    attribute = db.Column(db.Enum(*EnumerateData.attribute))
    second_attribute = db.Column(db.Enum(*EnumerateData.second_attribute))
    poverty_state = db.Column(db.Enum(*EnumerateData.poverty_state))
    town = db.Column(db.Enum(*EnumerateData.town))
    village = db.Column(db.Enum(*EnumerateData.village))
    phone_number = db.Column(db.String(20))
    source = db.Column(db.Enum(*EnumerateData.source))
    update_date = db.Column(db.DateTime)
    update_user = db.Column(db.String(20))
    remark = db.Column(db.String(100))

    def data_response(self, number):
        return {
            "number": number,
            "id": self.id,
            "name" : self.name,
            "id_number" : self.id_number,
            "own_expense": self.own_expense,
            "insured_state" : self.insured_state,
            "insured_area" : self.insured_area,
            "attribute" : self.attribute,
            "second_attribute": self.second_attribute,
            "poverty_state" : self.poverty_state,
            "town" : self.town,
            "village" : self.village,
            "phone_number" : self.phone_number,
            "update_date" : self.update_date.strftime("%Y-%m-%d") if self.update_date else '',
            "update_user" : self.update_user
        }

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20))
    phone_number = db.Column(db.String(20))
    town = db.Column(db.Enum(*EnumerateData.town))
    village = db.Column(db.Enum(*EnumerateData.village))
    password = db.Column(db.String(20))
    identity = db.Column(db.Enum(*EnumerateData.identity))

    def data_response(self):
        return {
            "id": self.id,
            "phone_number": self.phone_number,
            "name" : self.name,
            "town" : self.town,
            "village": self.village,
            "identity": self.identity,
            "authority": EnumerateData.authority[self.identity]
        }

class SettleData2021(db.Model):
    __tablename__ = "settle_data_2021"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    settle_id = db.Column(db.String(30), unique=True)
    cure_id = db.Column(db.String(30))
    self_number = db.Column(db.String(30))
    name = db.Column(db.String(20))
    id_number = db.Column(db.String(18))
    person_type = db.Column(db.Enum(*EnumerateData.person_type))
    pay_place = db.Column(db.Enum(*EnumerateData.pay_place))
    hospital_id = db.Column(db.String(20))
    hospital_name = db.Column(db.String(50))
    hospital_level = db.Column(db.Enum(*EnumerateData.hospital_level))
    hospital_place = db.Column(db.String(6))
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
    attribute = db.Column(db.Enum(*EnumerateData.attribute))
    second_attribute = db.Column(db.Enum(*EnumerateData.second_attribute))
    poverty_state = db.Column(db.Enum(*EnumerateData.poverty_state))
    town = db.Column(db.Enum(*EnumerateData.town))
    village = db.Column(db.Enum(*EnumerateData.village))

class SettleData2022(db.Model):
    __tablename__ = "settle_data_2022"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    settle_id = db.Column(db.String(30), unique=True)
    cure_id = db.Column(db.String(30))
    self_number = db.Column(db.String(30))
    name = db.Column(db.String(20))
    id_number = db.Column(db.String(18))
    person_type = db.Column(db.Enum(*EnumerateData.person_type))
    pay_place = db.Column(db.Enum(*EnumerateData.pay_place))
    hospital_id = db.Column(db.String(20))
    hospital_name = db.Column(db.String(50))
    hospital_level = db.Column(db.Enum(*EnumerateData.hospital_level))
    hospital_place = db.Column(db.String(6))
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
    attribute = db.Column(db.Enum(*EnumerateData.attribute))
    second_attribute = db.Column(db.Enum(*EnumerateData.second_attribute))
    poverty_state = db.Column(db.Enum(*EnumerateData.poverty_state))
    town = db.Column(db.Enum(*EnumerateData.town))
    village = db.Column(db.Enum(*EnumerateData.village))

model_dict = {
    "insured_data_2021": InsuredData2021,
    "insured_data_2022": InsuredData2022,
    'user': User,
    'settle_data_2021': SettleData2021,
    'settle_data_2022': SettleData2022,
}