import os
from datetime import timedelta, datetime

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
    Access_Control_Allow_Origin = '*'
    PERMANENT_SESSION_LIFETIME = timedelta(days=3)
    SESSION_COOKIE_NAME = "HealthcareSecurity"
    DEFAULT_YEAR = '2023'

class EnumerateData:
    civil_attribute = ('农村特困供养', '城市特困供养', '农村低保', '城市低保', '低保边缘户')
    poverty_state = ('监测户', '稳定脱贫人口', '致贫返贫人口', '贫困人口')
    orphan_attribute = ('孤儿', '事实无人抚养儿童')
    disable_attribute = ('重度残疾人',)
    treat_attribute = ('重点优抚对象',)
    accident_attribute = ('肇事肇祸精神病人',)
    attribute_gather_dict = {
        '应保尽保人群': ('农村特困供养', '城市特困供养', '农村低保', '城市低保', '监测户', '稳定脱贫人口', '致贫返贫人口', '孤儿', '事实无人抚养儿童', '肇事肇祸精神病人'),
        '参保资助人群': ('农村特困供养', '城市特困供养', '农村低保', '城市低保', '监测户', '致贫返贫人口', '孤儿', '事实无人抚养儿童', '重度残疾人', '重点优抚对象')
    }
    attribute_gather = tuple(attribute_gather_dict.keys())
    insured_state = ('本地居民', '本地职工', '异地居民', '异地职工', '死亡', '失联', '参军', '服刑', '其他')
    town_village_dict = {
        '梅城镇': ('七里村', '万岭村', '东关社区', '凤凰村', '利民村', '北街村', '北街社区', '双塘村', '太平村', '平桥村', '彭岭村', '彰法山社区', '新桃园社区', '模范村', '河庄村', '河湾村', '潘铺村', '舒苑社区', '蔬菜村', '高集村', '龙井社区', '其他'),
        '源潭镇': ('三妙村', '三河村', '东畈村', '东红村', '光辉村', '友爱村', '双峰居委会', '双林村', '叶典村', '斗塘村', '杨泗村', '棋盘村', '永济村', '源潭村', '田墩村', '赵冲村', '路口村', '其他', '长和村', '其他'),
        '余井镇': ('余井村', '天圣村', '天明村', '岭头居委会', '建军村', '文治村', '松岭村', '柴阁村', '田乐村', '程祠村', '糖岭村', '进士村', '马道村', '黄岭村', '其他'),
        '王河镇': ('中河村', '丰收村', '先进村', '光明村', '天崇村', '庆丰村', '新发村', '永和村', '河镇村', '王河村', '皖潜村', '程家井村', '红光村', '薛家岗村', '其他', '长友村', '龙湖村', '其他'),
        '黄铺镇': ('云峰村', '古井村', '古墩村', '和平村', '张河村', '望虎村', '桃铺村', '槐树村', '湖墩村', '莲花村', '金龙村', '陈桥村', '鲍岭村', '黄铺村', '其他'),
        '槎水镇': ('万全村', '中畈村', '乐明村', '后冲村', '方冲村', '木岗村', '槎水村', '油坊村', '滨河居委会', '皂河村', '逆水村', '金波村', '龙关村', '其他'),
        '水吼镇': ('三里村', '割肚村', '和平村', '天堂村', '天柱村', '梅寨村', '横中村', '水吼村', '程湾村', '风光村', '马潭村', '驾雾村', '高峰村', '黄龛村', '其他'),
        '官庄镇': ('乐平村', '光华村', '升旗村', '坛畈村', '孔士村', '官庄村', '常青居委会', '平峰村', '戈元村', '日光村', '杨庄村', '水贵村', '西岭村', '金城村', '其他'),
        '油坝乡': ('东店村', '其他', '唐埠村', '崔仓村', '张祠村', '桑树村', '油坝村', '其他'),
        '塔畈乡': ('体元村', '倪河村', '冯冲村', '双畈村', '周祠村', '塔畈村', '彭河村', '新安村', '杏花村', '板仓村', '西河村', '其他'),
        '黄泥镇': ('黄泥街居委会', '付祠村', '前进村', '文昌村', '胜利村', '金湖村', '龙坦村', '其他'),
        '龙潭乡': ('万涧村', '暗冲村', '杜埠村', '湖田村', '漆铺村', '白寨村', '谢河村', '龙湾村', '龙潭村', '其他'),
        '痘姆乡': ('仙驾村', '吴塘村', '孙塝村', '求知村', '红星村', '鞔鼓村', '其他'),
        '黄柏镇': ('叶河村', '大水村', '昆仑村', '袁桂村', '陆河村', '黄柏村', '其他'),
        '天柱山镇': ('天寺村', '林庄村', '河西村', '白水村', '茶庄村', '风景村', '其他'),
        '开发区': ('三合村', '八一村', '古塔村', '其他'),
        '五庙乡': ('吴桥村', '新建村', '新田村', '杨畈村', '程冲村', '红光村', '其他'),
        '其他': ('其他', ),}
    town = tuple(town_village_dict.keys())
    village = tuple(set(j for i in town_village_dict.values() for j in i))
    authority = {'管理员': ('*', ), '医保局': ('insured_data', 'settle_data'), '政府': ('insured_data')}
    identity = tuple(authority.keys())
    person_type = ('居民', '职工')
    hospital_place = ('本地', '市内异地', '省内异地', '跨省异地')
    hospital_level = ('三级特等', '三级甲等', '三级乙等', '三级丙等', '二级甲等', '二级乙等', '二级丙等', '一级甲等', '一级乙等', '一级丙等', '无等级', '其他')
    evidence_type = ('居民身份证', '社会保障卡', '医保电子凭证', '终端扫脸', '其他')
    year = ('2022', '2023')
    hospital_community_dict = {
        '市立医院': ('黄柏镇', '槎水镇', '源潭镇', '余井镇', '梅城镇', '官庄镇', '塔畈乡', '龙潭乡'),
        '中医院': ('水吼镇', '黄铺镇', '王河镇', '油坝乡', '黄泥镇', '五庙乡', '痘姆乡', '天柱山镇', '开发区')
    }
    hospital_community = tuple(hospital_community_dict.keys())
    cure_type_dict = {
        '住院': ('普通住院', '无法确定他方责任的意外伤害（外伤住院）', '转外诊治住院', '急诊转住院', '单病种住院', '日间手术', '生育住院', '同病同保障住院', '床日费用住院', '计划生育住院', '日间病床', '无他方责任意外伤害住院', '分疗程间断住院治疗'),
        '慢特病': ('门诊慢性病', '门诊特殊病', '双通道购药', '门诊单病种'),
        '门诊': ('普通门诊', '两病门诊', '生育门诊（产前检查）', '计生生育门诊', '大额普通门诊'),
        '其他': ('药店购药', '残疾人辅助器具', '18周岁以下苯丙酮尿症', '18周岁以下四氢生物蝶呤缺乏症', '18周岁以下苯丙酮尿症以及四氢生物蝶呤缺乏症', '其他')
    }
    cure_type = tuple(j for i in cure_type_dict.values() for j in i)
    cure_type_gather = tuple(cure_type_dict.keys())
    pay_type_dict = {'统筹基金': 'overall_pay', '大额医疗': 'large_pay', '大病保险': 'big_pay', '医疗救助': 'rescue_pay', '公务员医疗补助': 'civil_pay', '其他基金': 'other_pay', '基金支付总额': 'all_pay', '个人现金': 'cash_pay', '个人账户': 'account_pay', '账户共济': 'together_pay'}
    pay_type_label = tuple(pay_type_dict.keys())
    pay_type = tuple(pay_type_dict.values())
    pay_type_operator_dict = {'大于': '__gt__', '小于': '__lt__', '等于': '__eq__'}
    pay_type_operator_label = tuple(pay_type_operator_dict.keys())
    pay_type_operator = tuple(pay_type_operator_dict.values())

    @classmethod
    def dict_response(cls):
        return {
            "attribute_dict": {
                'civil_attribute': cls.civil_attribute,
                'poverty_state': cls.poverty_state,
                'orphan_attribute': cls.orphan_attribute,
                'disable_attribute': cls.disable_attribute,
                'treat_attribute': cls.treat_attribute,
                'accident_attribute': cls.accident_attribute,
            },
            "insured_state": cls.insured_state,
            "town_village_dict": cls.town_village_dict,
            'town': cls.town,
            'village': cls.village,
            'person_type': cls.person_type,
            'hospital_place': cls.hospital_place,
            'hospital_level': cls.hospital_level,
            'evidence_type': cls.evidence_type,
            'cure_type_dict': cls.cure_type_dict,
            'cure_type': cls.cure_type,
            'year': cls.year,
            'hospital_community_dict': cls.hospital_community_dict,
            'hospital_community': cls.hospital_community,
            'default_year': Config.DEFAULT_YEAR,
            'pay_type_dict': cls.pay_type_dict,
            'pay_type_label': cls.pay_type_label,
            'cure_type_gather': cls.cure_type_gather,
            'attribute_gather_dict': cls.attribute_gather_dict,
            'attribute_gather': cls.attribute_gather,
            'pay_type_operator_dict': cls.pay_type_operator_dict,
            'pay_type_operator_label': cls.pay_type_operator_label,
        }

class StaticData:
    own_expense_standard_dict = {'2019': 250, '2020': 250, '2021': 280, '2022': 320, '2023': 350}
    town_target_dict = {
        '2022': {'王河镇': 51666, '黄铺镇': 46684, '梅城镇': 74255, '官庄镇': 27433, '油坝乡': 19668, '塔畈乡': 19343, '黄柏镇': 14159, '天柱山镇': 12440, '黄泥镇': 19209, '源潭镇': 60820, '龙潭乡': 18516, '痘姆乡': 17630, '余井镇': 54932, '五庙乡': 10174, '槎水镇': 31963, '开发区': 11898, '水吼镇': 30404},
        '2023': {'槎水镇': 30993, '痘姆乡': 17129, '水吼镇': 29477, '官庄镇': 26445, '黄柏镇': 13470, '塔畈乡': 18773, '天柱山镇': 12244, '王河镇': 49752, '五庙乡': 9746, '油坝乡': 18946, '开发区': 11448, '龙潭乡': 17870, '余井镇': 52951, '梅城镇': 72615, '源潭镇': 59217, '黄铺镇': 45276, '黄泥镇': 18587},
    }
