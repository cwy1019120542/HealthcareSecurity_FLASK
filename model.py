from extension import db
from sqlalchemy.dialects.mysql import DOUBLE
from config import EnumerateData

def to_string_date(date):
    return date.strftime('%Y-%m-%d %H:%M:%S') if date else None

def to_float(data):
    return round(float(data), 2) if data else 0

def clean_illness_name(illness_name):
    return illness_name.replace('�?', '').replace('\x00', '') if illness_name else ''

class InsuredData2019(db.Model):
    __tablename__ = "insured_data_2019"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20))
    id_number = db.Column(db.String(18), unique=True)
    own_expense = db.Column(db.Float)
    pay_date = db.Column(db.DateTime)
    insured_state = db.Column(db.Enum(*EnumerateData.insured_state))
    attribute = db.Column(db.Enum(*EnumerateData.attribute))
    second_attribute = db.Column(db.Enum(*EnumerateData.second_attribute))
    poverty_state = db.Column(db.Enum(*EnumerateData.poverty_state))
    town = db.Column(db.Enum(*EnumerateData.town))
    village = db.Column(db.Enum(*EnumerateData.village))
    phone_number = db.Column(db.String(20))
    remark = db.Column(db.String(100))

    def dict_response(self, number):
        return {
            "number": number,
            "id": self.id,
            "name" : self.name,
            "id_number" : self.id_number,
            "own_expense": self.own_expense,
            "pay_date": to_string_date(self.pay_date),
            "insured_state" : self.insured_state,
            "attribute" : self.attribute,
            "second_attribute": self.second_attribute,
            "poverty_state" : self.poverty_state,
            "town" : self.town,
            "village" : self.village,
            "phone_number" : self.phone_number,
            "remark": self.remark,
        }

    def list_response(self, number):
        return [number, self.id, self.name, self.id_number, self.own_expense, to_string_date(self.pay_date), self.insured_state, self.attribute, self.second_attribute, self.poverty_state, self.town, self.village, self.phone_number, self.remark]

class InsuredData2020(db.Model):
    __tablename__ = "insured_data_2020"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20))
    id_number = db.Column(db.String(18), unique=True)
    own_expense = db.Column(db.Float)
    pay_date = db.Column(db.DateTime)
    insured_state = db.Column(db.Enum(*EnumerateData.insured_state))
    attribute = db.Column(db.Enum(*EnumerateData.attribute))
    second_attribute = db.Column(db.Enum(*EnumerateData.second_attribute))
    poverty_state = db.Column(db.Enum(*EnumerateData.poverty_state))
    town = db.Column(db.Enum(*EnumerateData.town))
    village = db.Column(db.Enum(*EnumerateData.village))
    phone_number = db.Column(db.String(20))
    remark = db.Column(db.String(100))

    def dict_response(self, number):
        return {
            "number": number,
            "id": self.id,
            "name": self.name,
            "id_number": self.id_number,
            "own_expense": self.own_expense,
            "pay_date": to_string_date(self.pay_date),
            "insured_state": self.insured_state,
            "attribute": self.attribute,
            "second_attribute": self.second_attribute,
            "poverty_state": self.poverty_state,
            "town": self.town,
            "village": self.village,
            "phone_number": self.phone_number,
            "remark": self.remark,
        }

    def list_response(self, number):
        return [number, self.id, self.name, self.id_number, self.own_expense, to_string_date(self.pay_date),
                self.insured_state, self.attribute, self.second_attribute, self.poverty_state, self.town, self.village,
                self.phone_number, self.remark]


class InsuredData2021(db.Model):
    __tablename__ = "insured_data_2021"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20))
    id_number = db.Column(db.String(18), unique=True)
    own_expense = db.Column(db.Float)
    pay_date = db.Column(db.DateTime)
    insured_state = db.Column(db.Enum(*EnumerateData.insured_state))
    attribute = db.Column(db.Enum(*EnumerateData.attribute))
    second_attribute = db.Column(db.Enum(*EnumerateData.second_attribute))
    poverty_state = db.Column(db.Enum(*EnumerateData.poverty_state))
    town = db.Column(db.Enum(*EnumerateData.town))
    village = db.Column(db.Enum(*EnumerateData.village))
    phone_number = db.Column(db.String(20))
    remark = db.Column(db.String(100))

    def dict_response(self, number):
        return {
            "number": number,
            "id": self.id,
            "name": self.name,
            "id_number": self.id_number,
            "own_expense": self.own_expense,
            "pay_date": to_string_date(self.pay_date),
            "insured_state": self.insured_state,
            "attribute": self.attribute,
            "second_attribute": self.second_attribute,
            "poverty_state": self.poverty_state,
            "town": self.town,
            "village": self.village,
            "phone_number": self.phone_number,
            "remark": self.remark,
        }

    def list_response(self, number):
        return [number, self.id, self.name, self.id_number, self.own_expense, to_string_date(self.pay_date),
                self.insured_state, self.attribute, self.second_attribute, self.poverty_state, self.town, self.village,
                self.phone_number, self.remark]


class InsuredData2022(db.Model):
    __tablename__ = "insured_data_2022"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20))
    id_number = db.Column(db.String(18), unique=True)
    own_expense = db.Column(db.Float)
    pay_date = db.Column(db.DateTime)
    insured_state = db.Column(db.Enum(*EnumerateData.insured_state))
    attribute = db.Column(db.Enum(*EnumerateData.attribute))
    second_attribute = db.Column(db.Enum(*EnumerateData.second_attribute))
    poverty_state = db.Column(db.Enum(*EnumerateData.poverty_state))
    town = db.Column(db.Enum(*EnumerateData.town))
    village = db.Column(db.Enum(*EnumerateData.village))
    phone_number = db.Column(db.String(20))
    remark = db.Column(db.String(100))

    def dict_response(self, number):
        return {
            "number": number,
            "id": self.id,
            "name": self.name,
            "id_number": self.id_number,
            "own_expense": self.own_expense,
            "pay_date": to_string_date(self.pay_date),
            "insured_state": self.insured_state,
            "attribute": self.attribute,
            "second_attribute": self.second_attribute,
            "poverty_state": self.poverty_state,
            "town": self.town,
            "village": self.village,
            "phone_number": self.phone_number,
            "remark": self.remark,
        }

    def list_response(self, number):
        return [number, self.id, self.name, self.id_number, self.own_expense, to_string_date(self.pay_date),
                self.insured_state, self.attribute, self.second_attribute, self.poverty_state, self.town, self.village,
                self.phone_number, self.remark]


class InsuredData2023(db.Model):
    __tablename__ = "insured_data_2023"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20))
    id_number = db.Column(db.String(18), unique=True)
    own_expense = db.Column(db.Float)
    pay_date = db.Column(db.DateTime)
    insured_state = db.Column(db.Enum(*EnumerateData.insured_state))
    attribute = db.Column(db.Enum(*EnumerateData.attribute))
    second_attribute = db.Column(db.Enum(*EnumerateData.second_attribute))
    poverty_state = db.Column(db.Enum(*EnumerateData.poverty_state))
    town = db.Column(db.Enum(*EnumerateData.town))
    village = db.Column(db.Enum(*EnumerateData.village))
    phone_number = db.Column(db.String(20))
    remark = db.Column(db.String(100))

    def dict_response(self, number):
        return {
            "number": number,
            "id": self.id,
            "name": self.name,
            "id_number": self.id_number,
            "own_expense": self.own_expense,
            "pay_date": to_string_date(self.pay_date),
            "insured_state": self.insured_state,
            "attribute": self.attribute,
            "second_attribute": self.second_attribute,
            "poverty_state": self.poverty_state,
            "town": self.town,
            "village": self.village,
            "phone_number": self.phone_number,
            "remark": self.remark,
        }

    def list_response(self, number):
        return [number, self.id, self.name, self.id_number, self.own_expense, to_string_date(self.pay_date),
                self.insured_state, self.attribute, self.second_attribute, self.poverty_state, self.town, self.village,
                self.phone_number, self.remark]


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

class SettleData2019(db.Model):
    __tablename__ = "settle_data_2019"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    settle_id = db.Column(db.String(30))
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

    def dict_response(self, number):
        return {"number": number, "id": self.id, "settle_id": self.settle_id, "cure_id": self.cure_id,
                "self_number": self.self_number, "name": self.name, "id_number": self.id_number,
                "person_type": self.person_type, "pay_place": self.pay_place, "hospital_id": self.hospital_id,
                "hospital_name": self.hospital_name, "hospital_level": self.hospital_level,
                "hospital_place": self.hospital_place, "start_date": to_string_date(self.start_date),
                "end_date": to_string_date(self.end_date), "settle_date": to_string_date(self.settle_date),
                "evidence_type": self.evidence_type, "all_expense": to_float(self.all_expense),
                "self_expense": to_float(self.self_expense),
                "over_expense": to_float(self.over_expense), "first_expense": to_float(self.first_expense),
                "inner_expense": to_float(self.inner_expense), "start_pay": to_float(self.start_pay),
                "overall_pay": to_float(self.overall_pay),
                "large_pay": to_float(self.large_pay), "big_pay": to_float(self.big_pay),
                "rescue_pay": to_float(self.rescue_pay),
                "civil_pay": to_float(self.civil_pay), "other_pay": to_float(self.other_pay),
                "all_pay": to_float(self.all_pay),
                "cash_pay": to_float(self.cash_pay), "account_pay": to_float(self.account_pay),
                "together_pay": to_float(self.together_pay),
                "illness_name": clean_illness_name(self.illness_name), "cure_type": self.cure_type, "attribute": self.attribute,
                "second_attribute": self.second_attribute, "poverty_state": self.poverty_state, "town": self.town,
                "village": self.village}

    def list_response(self, number):
        return [number, self.id, self.settle_id, self.cure_id, self.self_number, self.name, self.id_number, self.person_type, self.pay_place, self.hospital_id, self.hospital_name,
                self.hospital_level, self.hospital_place, to_string_date(self.start_date), to_string_date(self.end_date), to_string_date(self.settle_date), self.evidence_type, to_float(self.all_expense), to_float(self.self_expense),
                to_float(self.over_expense), to_float(self.first_expense), to_float(self.inner_expense), to_float(self.start_pay), to_float(self.overall_pay), to_float(self.large_pay), to_float(self.big_pay), to_float(self.rescue_pay), to_float(self.civil_pay),
                to_float(self.other_pay), to_float(self.all_pay), to_float(self.cash_pay), to_float(self.account_pay), to_float(self.together_pay), clean_illness_name(self.illness_name), self.cure_type, self.attribute, self.second_attribute,
                self.poverty_state, self.town, self.village]


class SettleData2020(db.Model):
    __tablename__ = "settle_data_2020"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    settle_id = db.Column(db.String(30))
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

    def dict_response(self, number):
        return {"number": number, "id": self.id, "settle_id": self.settle_id, "cure_id": self.cure_id,
                "self_number": self.self_number, "name": self.name, "id_number": self.id_number,
                "person_type": self.person_type, "pay_place": self.pay_place, "hospital_id": self.hospital_id,
                "hospital_name": self.hospital_name, "hospital_level": self.hospital_level,
                "hospital_place": self.hospital_place, "start_date": to_string_date(self.start_date),
                "end_date": to_string_date(self.end_date), "settle_date": to_string_date(self.settle_date),
                "evidence_type": self.evidence_type, "all_expense": to_float(self.all_expense),
                "self_expense": to_float(self.self_expense),
                "over_expense": to_float(self.over_expense), "first_expense": to_float(self.first_expense),
                "inner_expense": to_float(self.inner_expense), "start_pay": to_float(self.start_pay),
                "overall_pay": to_float(self.overall_pay),
                "large_pay": to_float(self.large_pay), "big_pay": to_float(self.big_pay),
                "rescue_pay": to_float(self.rescue_pay),
                "civil_pay": to_float(self.civil_pay), "other_pay": to_float(self.other_pay),
                "all_pay": to_float(self.all_pay),
                "cash_pay": to_float(self.cash_pay), "account_pay": to_float(self.account_pay),
                "together_pay": to_float(self.together_pay),
                "illness_name": clean_illness_name(self.illness_name), "cure_type": self.cure_type, "attribute": self.attribute,
                "second_attribute": self.second_attribute, "poverty_state": self.poverty_state, "town": self.town,
                "village": self.village}

    def list_response(self, number):
        return [number, self.id, self.settle_id, self.cure_id, self.self_number, self.name, self.id_number,
                self.person_type, self.pay_place, self.hospital_id, self.hospital_name,
                self.hospital_level, self.hospital_place, to_string_date(self.start_date),
                to_string_date(self.end_date), to_string_date(self.settle_date), self.evidence_type,
                to_float(self.all_expense), to_float(self.self_expense),
                to_float(self.over_expense), to_float(self.first_expense), to_float(self.inner_expense),
                to_float(self.start_pay), to_float(self.overall_pay), to_float(self.large_pay), to_float(self.big_pay),
                to_float(self.rescue_pay), to_float(self.civil_pay),
                to_float(self.other_pay), to_float(self.all_pay), to_float(self.cash_pay), to_float(self.account_pay),
                to_float(self.together_pay), clean_illness_name(self.illness_name), self.cure_type, self.attribute, self.second_attribute,
                self.poverty_state, self.town, self.village]

class SettleData2021(db.Model):
    __tablename__ = "settle_data_2021"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    settle_id = db.Column(db.String(30))
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

    def dict_response(self, number):
        return {"number": number, "id": self.id, "settle_id": self.settle_id, "cure_id": self.cure_id,
                "self_number": self.self_number, "name": self.name, "id_number": self.id_number,
                "person_type": self.person_type, "pay_place": self.pay_place, "hospital_id": self.hospital_id,
                "hospital_name": self.hospital_name, "hospital_level": self.hospital_level,
                "hospital_place": self.hospital_place, "start_date": to_string_date(self.start_date),
                "end_date": to_string_date(self.end_date), "settle_date": to_string_date(self.settle_date),
                "evidence_type": self.evidence_type, "all_expense": to_float(self.all_expense),
                "self_expense": to_float(self.self_expense),
                "over_expense": to_float(self.over_expense), "first_expense": to_float(self.first_expense),
                "inner_expense": to_float(self.inner_expense), "start_pay": to_float(self.start_pay),
                "overall_pay": to_float(self.overall_pay),
                "large_pay": to_float(self.large_pay), "big_pay": to_float(self.big_pay),
                "rescue_pay": to_float(self.rescue_pay),
                "civil_pay": to_float(self.civil_pay), "other_pay": to_float(self.other_pay),
                "all_pay": to_float(self.all_pay),
                "cash_pay": to_float(self.cash_pay), "account_pay": to_float(self.account_pay),
                "together_pay": to_float(self.together_pay),
                "illness_name": clean_illness_name(self.illness_name), "cure_type": self.cure_type, "attribute": self.attribute,
                "second_attribute": self.second_attribute, "poverty_state": self.poverty_state, "town": self.town,
                "village": self.village}

    def list_response(self, number):
        return [number, self.id, self.settle_id, self.cure_id, self.self_number, self.name, self.id_number,
                self.person_type, self.pay_place, self.hospital_id, self.hospital_name,
                self.hospital_level, self.hospital_place, to_string_date(self.start_date),
                to_string_date(self.end_date), to_string_date(self.settle_date), self.evidence_type,
                to_float(self.all_expense), to_float(self.self_expense),
                to_float(self.over_expense), to_float(self.first_expense), to_float(self.inner_expense),
                to_float(self.start_pay), to_float(self.overall_pay), to_float(self.large_pay), to_float(self.big_pay),
                to_float(self.rescue_pay), to_float(self.civil_pay),
                to_float(self.other_pay), to_float(self.all_pay), to_float(self.cash_pay), to_float(self.account_pay),
                to_float(self.together_pay), clean_illness_name(self.illness_name), self.cure_type, self.attribute, self.second_attribute,
                self.poverty_state, self.town, self.village]

class SettleData2022(db.Model):
    __tablename__ = "settle_data_2022"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    settle_id = db.Column(db.String(30))
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

    def dict_response(self, number):
        return {"number": number, "id": self.id, "settle_id": self.settle_id, "cure_id": self.cure_id,
                "self_number": self.self_number, "name": self.name, "id_number": self.id_number,
                "person_type": self.person_type, "pay_place": self.pay_place, "hospital_id": self.hospital_id,
                "hospital_name": self.hospital_name, "hospital_level": self.hospital_level,
                "hospital_place": self.hospital_place, "start_date": to_string_date(self.start_date),
                "end_date": to_string_date(self.end_date), "settle_date": to_string_date(self.settle_date),
                "evidence_type": self.evidence_type, "all_expense": to_float(self.all_expense),
                "self_expense": to_float(self.self_expense),
                "over_expense": to_float(self.over_expense), "first_expense": to_float(self.first_expense),
                "inner_expense": to_float(self.inner_expense), "start_pay": to_float(self.start_pay),
                "overall_pay": to_float(self.overall_pay),
                "large_pay": to_float(self.large_pay), "big_pay": to_float(self.big_pay),
                "rescue_pay": to_float(self.rescue_pay),
                "civil_pay": to_float(self.civil_pay), "other_pay": to_float(self.other_pay),
                "all_pay": to_float(self.all_pay),
                "cash_pay": to_float(self.cash_pay), "account_pay": to_float(self.account_pay),
                "together_pay": to_float(self.together_pay),
                "illness_name": clean_illness_name(self.illness_name), "cure_type": self.cure_type, "attribute": self.attribute,
                "second_attribute": self.second_attribute, "poverty_state": self.poverty_state, "town": self.town,
                "village": self.village}

    def list_response(self, number):
        return [number, self.id, self.settle_id, self.cure_id, self.self_number, self.name, self.id_number,
                self.person_type, self.pay_place, self.hospital_id, self.hospital_name,
                self.hospital_level, self.hospital_place, to_string_date(self.start_date),
                to_string_date(self.end_date), to_string_date(self.settle_date), self.evidence_type,
                to_float(self.all_expense), to_float(self.self_expense),
                to_float(self.over_expense), to_float(self.first_expense), to_float(self.inner_expense),
                to_float(self.start_pay), to_float(self.overall_pay), to_float(self.large_pay), to_float(self.big_pay),
                to_float(self.rescue_pay), to_float(self.civil_pay),
                to_float(self.other_pay), to_float(self.all_pay), to_float(self.cash_pay), to_float(self.account_pay),
                to_float(self.together_pay), clean_illness_name(self.illness_name), self.cure_type, self.attribute, self.second_attribute,
                self.poverty_state, self.town, self.village]


class SettleData2023(db.Model):
    __tablename__ = "settle_data_2023"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    settle_id = db.Column(db.String(30))
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

    def dict_response(self, number):
        return {"number": number, "id": self.id, "settle_id": self.settle_id, "cure_id": self.cure_id,
                "self_number": self.self_number, "name": self.name, "id_number": self.id_number,
                "person_type": self.person_type, "pay_place": self.pay_place, "hospital_id": self.hospital_id,
                "hospital_name": self.hospital_name, "hospital_level": self.hospital_level,
                "hospital_place": self.hospital_place, "start_date": to_string_date(self.start_date),
                "end_date": to_string_date(self.end_date), "settle_date": to_string_date(self.settle_date),
                "evidence_type": self.evidence_type, "all_expense": to_float(self.all_expense),
                "self_expense": to_float(self.self_expense),
                "over_expense": to_float(self.over_expense), "first_expense": to_float(self.first_expense),
                "inner_expense": to_float(self.inner_expense), "start_pay": to_float(self.start_pay),
                "overall_pay": to_float(self.overall_pay),
                "large_pay": to_float(self.large_pay), "big_pay": to_float(self.big_pay),
                "rescue_pay": to_float(self.rescue_pay),
                "civil_pay": to_float(self.civil_pay), "other_pay": to_float(self.other_pay),
                "all_pay": to_float(self.all_pay),
                "cash_pay": to_float(self.cash_pay), "account_pay": to_float(self.account_pay),
                "together_pay": to_float(self.together_pay),
                "illness_name": clean_illness_name(self.illness_name), "cure_type": self.cure_type, "attribute": self.attribute,
                "second_attribute": self.second_attribute, "poverty_state": self.poverty_state, "town": self.town,
                "village": self.village}

    def list_response(self, number):
        return [number, self.id, self.settle_id, self.cure_id, self.self_number, self.name, self.id_number,
                self.person_type, self.pay_place, self.hospital_id, self.hospital_name,
                self.hospital_level, self.hospital_place, to_string_date(self.start_date),
                to_string_date(self.end_date), to_string_date(self.settle_date), self.evidence_type,
                to_float(self.all_expense), to_float(self.self_expense),
                to_float(self.over_expense), to_float(self.first_expense), to_float(self.inner_expense),
                to_float(self.start_pay), to_float(self.overall_pay), to_float(self.large_pay), to_float(self.big_pay),
                to_float(self.rescue_pay), to_float(self.civil_pay),
                to_float(self.other_pay), to_float(self.all_pay), to_float(self.cash_pay), to_float(self.account_pay),
                to_float(self.together_pay), clean_illness_name(self.illness_name), self.cure_type, self.attribute, self.second_attribute,
                self.poverty_state, self.town, self.village]


model_dict = {
    "insured_data_2019": InsuredData2019,
    "insured_data_2020": InsuredData2020,
    "insured_data_2021": InsuredData2021,
    "insured_data_2022": InsuredData2022,
    "insured_data_2023": InsuredData2023,
    'user': User,
    'settle_data_2019': SettleData2019,
    'settle_data_2020': SettleData2020,
    'settle_data_2021': SettleData2021,
    'settle_data_2022': SettleData2022,
    'settle_data_2023': SettleData2023,
}