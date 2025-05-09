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
    DEFAULT_YEAR = "2025"
    MAX_CONTENT_LENGTH = 10 * 1024 * 1024
    CHECK_ATTACHMENT_DIR = os.getenv('CHECK_ATTACHMENT_DIR')
    CHRONIC_ILLNESS_CARD_DIR =  os.getenv('CHRONIC_ILLNESS_CARD_DIR')

class EnumerateData:
    attribute_dict = {
        'civil_attribute': ('农村特困', '城市特困', '农村低保', '城市低保', '低保边缘家庭人员', '因病致贫家庭重病患者'),
        'poverty_state': ('监测户', '稳定脱贫人口', '致贫返贫人口', '贫困人口'),
        'orphan_attribute': ('孤儿', '事实无人抚养儿童'),
        'disable_attribute': ('重度残疾人',),
        'treat_attribute': ('重点优抚对象',),
        'accident_attribute': ('肇事肇祸精神病人',),
    }
    civil_attribute = attribute_dict['civil_attribute']
    poverty_state = attribute_dict['poverty_state']
    orphan_attribute = attribute_dict['orphan_attribute']
    disable_attribute = attribute_dict['disable_attribute']
    treat_attribute = attribute_dict['treat_attribute']
    accident_attribute = attribute_dict['accident_attribute']
    attribute_gather_dict = {
        '应保尽保人群': ('农村特困', '城市特困', '农村低保', '城市低保', '监测户', '稳定脱贫人口', '致贫返贫人口', '孤儿', '事实无人抚养儿童', '肇事肇祸精神病人', '低保边缘家庭人员', '因病致贫家庭重病患者'),
        '参保资助人群': ('农村特困', '城市特困', '农村低保', '城市低保', '监测户', '致贫返贫人口', '孤儿', '事实无人抚养儿童', '重度残疾人', '重点优抚对象')
    }
    attribute_gather = tuple(attribute_gather_dict.keys())
    insured_state = ('本地居民', '本地职工(在职)', '本地职工(退休)','异地居民', '异地职工', '参军', '服刑', '死亡', '失联', '动态新增', '自愿放弃', '其他')
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
    authority = {'管理员': ('*', ), '服务中心': ('user', 'insured_data', 'settle_data', 'check_data', 'staff', 'check_attachment', 'chronic_illness'), '医保局': ('user', 'insured_data', 'settle_data', 'chronic_illness'), '政府': ('chronic_illness', )}
    identity = tuple(authority.keys())
    person_type = ('居民', '在职职工', '退休职工', '离休')
    person_type_simple = ('居民', '职工')
    hospital_place = ('本地', '市内异地', '省内异地', '跨省异地')
    hospital_level = ('三级特等', '三级甲等', '三级乙等', '三级丙等', '三级无等', '二级甲等', '二级乙等', '二级丙等', '二级无等', '一级甲等', '一级乙等', '一级丙等', '一级无等', '无等级', '其他')
    evidence_type = ('医保电子凭证', '居民身份证', '社会保障卡', '终端扫码', '终端扫脸', '电子社会保障卡', '其他')
    year = ('2019', '2020', '2021', '2022', '2023', '2024', '2025')
    compare_year = ('2019', '2020', '2021', '2022', '2023', '2024', '2025')
    hospital_community_dict = {
        '市立医院': ('黄柏镇', '槎水镇', '源潭镇', '余井镇', '梅城镇', '官庄镇', '塔畈乡', '龙潭乡', '开发区', '其他'),
        '市中医院': ('水吼镇', '黄铺镇', '王河镇', '油坝乡', '黄泥镇', '五庙乡', '痘姆乡', '天柱山镇')
    }
    hospital_community = tuple(hospital_community_dict.keys())
    cure_type_dict = {
        '住院': ('普通住院', '外伤住院', '无他方责任意外伤害住院', '分疗程间断住院治疗', '单病种住院', '床日费用住院', '转外诊治住院', '急诊转住院', '自主就医住院', '18周岁以下苯丙酮尿症及四氢生物蝶呤缺乏症', '18周岁以下苯丙酮尿症', '日间病床', '罕见病住院'),
        '慢特病': ('门诊特病', '门诊慢病', '门诊单病种'),
        '门诊': ('普通门诊', '大额普通门诊', '生育门诊', '门诊两病', '门诊挂号', '新冠门诊', '残疾人辅助器具门诊', '门诊罕见病'),
        '其他': ('定点药店购药', '生育住院', '大病关怀', '计划生育手术费', '计划生育住院', '独立门诊部个人帐户支付', '其他')
    }
    cure_type = tuple(j for i in cure_type_dict.values() for j in i)
    cure_type_gather = tuple(cure_type_dict.keys())
    pay_type_dict = {'总费用': 'all_expense', '全自费金额': 'self_expense', '超限价自费费用': 'over_expense', '先行自付金额': 'first_expense', '范围内费用': 'inner_expense', '起付线': 'start_pay', '统筹基金': 'overall_pay', '大额医疗': 'large_pay', '大病保险': 'big_pay', '医疗救助': 'rescue_pay', '公务员医疗补助': 'civil_pay', '其他基金': 'other_pay', '基金支付总额': 'all_pay', '个人现金': 'cash_pay', '个人账户': 'account_pay', '账户共济': 'together_pay'}
    pay_type_label = tuple(pay_type_dict.keys())
    pay_type = tuple(pay_type_dict.values())
    pay_type_operator_dict = {'大于': '__gt__', '大于等于': '__ge__','小于': '__lt__', '小于等于': '__le__','等于': '__eq__', '不等于': '__ne__',}
    pay_type_operator_label = tuple(pay_type_operator_dict.keys())
    pay_type_operator = tuple(pay_type_operator_dict.values())
    overyear_refund = ('冲销', '被冲销')
    check_dict = {
        '加分': {
            '信息报送': {'县级': 0.5, '市级': 1, '省级': 1.5, '中央级': 2}, '获奖': {'单位': 1}, '表彰': {'群众': 1}
        },
        '扣分': {
            '未打卡/迟到/早退': {'政务服务中心': -1},
            '空岗': {'单位': -1, '政务服务中心/群众': -2, '政府热线/市委监委': -3},
            '聊天': {'单位': -1, '政务服务中心/群众': -2, '政府热线/市委监委': -3}, '吃东西': {'单位': -1, '政务服务中心/群众': -2, '政府热线/市委监委': -3},
            '玩手机': {'单位': -1, '政务服务中心/群众': -2, '政府热线/市委监委': -3}, '手机未入柜': {'单位': -1},
            '浏览非工作信息': {'单位': -1, '政务服务中心/群众': -2, '政府热线/市委监委': -3}, '不参加学习培训': {'单位': -1},
            '未按时到岗': {'单位': -0.5}, '提前就餐': {'单位': -0.5, '政务服务中心/群众': -1.5},
            '卫生不干净': {'单位': -0.5, '政务服务中心/群众': -1.5}, '未穿工作服': {'单位': -0.5, '政务服务中心/群众': -1.5},
            '因私请假超10天': {'政务服务中心': -2},
            '投诉': {'政务服务中心/群众': -2, '政府热线/市委监委': -4}, '短信评价8分以下': {'政务服务中心': -1},
            '未按时完成工作': {'单位': -2}, '业务办理出错': {'单位': -2},
            '测验低于60分': {'单位': -1}, '测验低于70分': {'单位': -0.5},
            '严重违纪': {'单位': -50}, '不服从安排': {'单位': -5},
        }
    }
    operate_type = tuple(check_dict.keys())
    check_type = []
    check_source_list = []
    for i in operate_type:
        j_list = check_dict[i].keys()
        check_type.extend(j_list)
        for k in j_list:
            check_source_list.extend(check_dict[i][k].keys())
    check_source = tuple(set(check_source_list))
    default_year = Config.DEFAULT_YEAR
    sex = ('男', '女')
    department = ('征缴股', '审核股')
    position = ('前台', '后台')
    education = ('大专', '中专', '本科')
    open_data_type_dict = {'医疗机构一站式救助汇总表': 'hospital', '城乡居民基本医疗、大病保险、医疗救助公示': 'pay', '一站式医疗救助花名册': 'rescue'}
    open_data_type = tuple(open_data_type_dict.keys())
    apply_source = ('定点医药机构', '中心经办系统', '网上经办系统', 'APP', '一体机', '医保微信公众号', '其他', '微信公众号', '省局用药保障平台', '国家医保局')
    illness_type = ('门慢门特病种', '门诊慢性病', '门诊特殊疾病', '按病种结算病种', '日间手术病种', '疾病诊断病种', '其他病种',
     '城乡居民两病', '急危重症', '城乡居民重大疾病', '特药病种', '疑难病种', '罕见病', '家庭病床病种', '两病门诊病种',
     '两病病种', '三四级手术', '重特大疾病病种', '门诊两病病种', '居民单病种', '职工单病种', '城乡居民生育病种',
     '分级诊疗病种', '重特大疾病住院病种', '重特大疾病门诊病种', '中医日间病房病种', '床日付费病种')
    hospital_name_id_dict = {'潜山县刘小军盲人医疗按摩所': 'H34088200378', '潜山市黄铺镇槐树村卫生室': 'H34088200881', '潜山市王河镇程家井村卫生室': 'H34088200989', '潜山市油坝乡油坝村卫生室': 'H34088200950', '潜山市黄铺镇古井村卫生室': 'H34088200882', '潜山市黄铺镇和平村卫生室': 'H34088200883', '潜山市塔畈乡周祠村卫生室': 'H34088201196', '张宏中医诊所': 'H34088200138', '潜山县龙潭乡暗冲村卫生室': 'H34088200990', '潜山市黄铺镇桃铺村卫生室': 'H34088200884', '潜山县梅城镇太平村卫生室': 'H34088201126', '潜山县余井镇田乐村卫生室': 'H34088200969', '潜山市天柱山镇林庄村卫生室': 'H34088200886', '潜山县龙潭乡卫生院': 'H34088200260', '潜山市塔畈乡卫生院': 'H34088200297', '潜山市立医院': 'H34088200355', '潜山市黄铺中心卫生院': 'H34088200187', '潜山现代口腔门诊部': 'H34088200471', '潜山市中医院': 'H34088200339', '潜山市黄泥镇卫生院': 'H34088200283', '潜山市天柱山镇卫生院': 'H34088200282', '潜山县付丽平口腔诊所': 'H34088200469', '潜山市五庙乡卫生院': 'H34088200313', '潜山市痘姆乡卫生院': 'H34088200431', '潜山市梅城镇卫生院': 'H34088200266', '潜山市唐宁诊所': 'H34088200308', '吴昊中医诊所': 'H34088200507', '潜山市水吼中心卫生院': 'H34088200137', '刘正中医诊所': 'H34088200273', '潜山市王河中心卫生院': 'H34088200205', '潜山市官庄镇卫生院': 'H34088200276', '潜山县余井中心卫生院': 'H34088200185', '梅城镇舒苑社区卫生服务站': 'H34088200139', '王继东中医诊所': 'H34088200251', '潜山县梅城镇东关居委会社区卫生服务站': 'H34088200219', '潜山东华医院': 'H34088200271', '潜山朝阳医院': 'H34088200432', '潜山县余井镇糖岭村卫生室': 'H34088200970', '潜山市五庙乡程冲村卫生室': 'H34088201205', '潜山市王河镇天崇村卫生室': 'H34088201006', '潜山市五庙乡杨畈村卫生室': 'H34088201206', '潜山县梅城镇模范村卫生室': 'H34088201127', '郑永红中医诊所': 'H34088200293', '钱国红诊所': 'H34088201289', '潜山县官庄镇升旗村卫生室': 'H34088201007', '潜山市黄泥镇文昌村卫生室': 'H34088201245', '潜山市源潭镇田墩村卫生室': 'H34088201111', '潜山县痘姆乡吴塘村卫生室': 'H34088201096', '潜山市杨国联中医诊所': 'H34088201838', '潜山县梅城镇双塘村卫生室': 'H34088201128', '潜山市黄铺镇陈桥村卫生室': 'H34088200885', '潜山市水吼镇水吼村卫生室': 'H34088201129', '潜山县官庄镇官庄村卫生室': 'H34088201008', '潜山市王河镇丰收村卫生室': 'H34088200991', '潜山市黄柏镇昆仑村卫生室': 'H34088201192', '潜山县余井镇马道村卫生室': 'H34088200971', '侯彭贞盲人医疗按摩所': 'H34088200319', '潜山县龙潭乡湖田村卫生室': 'H34088200992', '潜山市五庙乡吴桥村卫生室': 'H34088201207', '潜山县官庄镇孔士村卫生室': 'H34088201009', '潜山市王河镇皖潜村卫生室': 'H34088201010', '潜山市黄铺镇云峰村卫生室': 'H34088200892', '潜山市黄泥镇街道居委会卫生室': 'H34088201246', '潜山市水吼镇割肚村卫生室': 'H34088200636', '潜山县余井镇天圣村卫生室': 'H34088200972', '潜山市源潭镇东红村卫生室': 'H34088201112', '潜山市妇幼保健计划生育服务中心': 'H34088200362', '潜山市源潭镇叶典村卫生室': 'H34088201097', '潜山市黄铺镇莲花村卫生室': 'H34088200893', '保济堂中医诊所': 'H34088200290', '潜山市黄柏镇袁桂村卫生室': 'H34088201189', '潜山市黄铺镇古墩村卫生室': 'H34088200894', '潜山市第一人民医院': 'H34088200161', '潜山市王河镇光明村卫生室': 'H34088200993', '潜山市黄泥镇金湖村卫生室': 'H34088201247', '潜山市塔畈乡杏花村卫生室': 'H34088201199', '潜山市余井镇岭头居委会社区卫生服务站': 'H34088200973', '潜山市水吼镇马潭村卫生室': 'H34088200637', '汪建兵口腔诊所': 'H34088201897', '潜山市黄泥镇前进村卫生室': 'H34088201248', '潜山市黄铺镇金龙村卫生室': 'H34088200895', '潜山县龙潭乡漆铺村卫生室': 'H34088200994', '潜山市源潭镇赵冲村卫生室': 'H34088201098', '潜山市王河镇王河村卫生室': 'H34088201011', '潜山市黄泥镇龙坦村卫生室': 'H34088201249', '潜山县余井镇程祠村卫生室': 'H34088200974', '潜山市官庄镇金城村卫生室': 'H34088201012', '潜山经济开发区三合社区卫生服务站': 'H34088201099', '潜山市水吼镇风光村卫生室': 'H34088200638', '潜山市源潭镇杨泗村卫生室': 'H34088201113', '潜山县痘姆乡孙塝村卫生室': 'H34088201100', '潜山市天柱山镇风景村卫生室': 'H34088200889', '潜山市黄铺镇望虎村卫生室': 'H34088200975', '潜山县龙潭乡谢河村卫生室': 'H34088200995', '潜山县黄柏镇黄柏村卫生室': 'H34088201193', '潜山市源潭镇双林村卫生室': 'H34088201114', '潜山市张旺宏诊所': 'H34088200001', '潜山市槎水中心卫生院': 'H34088200315', '潜山市王河镇先进村卫生室': 'H34088201013', '潜山市官庄镇杨庄村卫生室': 'H34088201115', '潜山市塔畈乡倪河村卫生室': 'H34088201200', '潜山市王河镇河镇村卫生室': 'H34088200996', '潜山市余井镇黄岭村卫生室': 'H34088200976', '潜山县梅城镇七里村卫生室': 'H34088201130', '潜山市源潭镇三妙居委会卫生室': 'H34088201116', '潜山市水吼镇和平村卫生室': 'H34088200639', '潜山市天柱山镇天寺村卫生室': 'H34088200890', '潜山县龙潭乡白寨村卫生室': 'H34088200997', '潜山县梅城镇利民村卫生室': 'H34088201117', '潜山市源潭镇源潭居委会卫生室': 'H34088201118', '潜山市源潭镇双峰居委会卫生室': 'H34088201119', '潜山吴丹口腔门诊部': 'H34088201880', '潜山县余井镇文治村卫生室': 'H34088200977', '潜山经济开发区古塔社区卫生服务站': 'H34088201101', '潜山市油坝乡桑树村卫生室': 'H34088200951', '潜山县余井镇天明村卫生室': 'H34088200978', '潜山市黄泥镇傅祠村卫生室': 'H34088201261', '潜山同春医院': 'H34088200529', '潜山市水吼镇高峰村卫生室': 'H34088200640', '潜山县梅城镇凤凰村卫生室': 'H34088201131', '潜山县痘姆乡仙驾村卫生室': 'H34088200979', '潜山县黄柏镇叶河村卫生室': 'H34088201194', '潜山市王河镇薛家岗村卫生室': 'H34088201014', '潜山市源潭镇光辉村卫生室': 'H34088201102', '潜山县龙潭乡龙潭村卫生室': 'H34088201090', '潜山市源潭镇长和居委会卫生室': 'H34088201103', '潜山市油坝乡崔仓村卫生室': 'H34088200952', '潜山县余井镇余井村卫生室': 'H34088200960', '潜山市官庄镇水贵村卫生室': 'H34088201015', '平民中医诊所': 'H34088201826', '潜山市塔畈乡新安村卫生室': 'H34088201201', '潜山市天柱山镇白水村卫生室': 'H34088200887', '潜山市梅城镇河庄村卫生室': 'H34088201132', '潜山市五庙乡新田村卫生室': 'H34088201210', '潜山县余井镇松岭村卫生室': 'H34088200961', '潜山县痘姆乡鞔鼓村卫生室': 'H34088201104', '潜山市水吼镇黄龛村卫生室': 'H34088200641', '潜山百信中医门诊部': 'H34088201859', '韩久胜盲人医疗按摩所': 'H34088200467', '潜山市龙潭乡龙湾村卫生室': 'H34088201091', '潜山县官庄镇日光村卫生室': 'H34088201016', '潜山市王河镇红光村卫生室': 'H34088201017', '潜山市源潭镇东畈村卫生室': 'H34088201120', '潜山市王河镇长友村卫生室': 'H34088200998', '潜山市黄铺镇张河村卫生室': 'H34088200980', '潜山县官庄镇戈元村卫生室': 'H34088201092', '潜山市黄柏中心卫生院': 'H34088200334', '潜山市塔畈乡西河村卫生室': 'H34088201202', '潜山县余井镇柴阁村卫生室': 'H34088200962', '潜山市黄泥镇胜利村卫生室': 'H34088201262', '潜山市王河镇王河街居委会卫生室': 'H34088201018', '潜山康视眼科医院': 'H34088201861', '潜山县痘姆乡求知村卫生室': 'H34088201105', '潜山市五庙乡红光村卫生室': 'H34088201209', '潜山县官庄镇乐平村卫生室': 'H34088201093', '潜山市源潭镇永济村卫生室': 'H34088201121', '潜山市水吼镇天柱村卫生室': 'H34088200642', '潜山市塔畈乡彭河村卫生室': 'H34088201190', '潜山市黄柏镇陆河村卫生室': 'H34088201286', '潜山康润中医诊所': 'H34088201079', '潜山经济开发区八一社区卫生服务站': 'H34088201106', '潜山市塔畈乡双畈村卫生室': 'H34088201204', '潜山市源潭镇棋盘居委会卫生室': 'H34088201122', '潜山市油坝乡东店村卫生室': 'H34088200953', '潜山市塔畈乡板仓村卫生室': 'H34088201203', '潜山市五庙乡新建村卫生室': 'H34088201208', '潜山市水吼镇横中村卫生室': 'H34088200643', '潜山市王河镇中河村卫生室': 'H34088200999', '潜山市龙潭乡万涧村卫生室': 'H34088201000', '潜山市水吼镇梅寨村卫生室': 'H34088200644', '潜山市油坝乡张祠村卫生室': 'H34088200954', '潜山市梅城镇潜阳社区卫生服务中心': 'H34088200175', '潜山县梅城镇高集村卫生室': 'H34088201133', '潜山县梅城镇平桥村卫生室': 'H34088201134', '潜山县官庄镇平峰村卫生室': 'H34088201094', '潜山市王河镇龙湖村卫生室': 'H34088201001', '潜山市源潭镇三河村卫生室': 'H34088201123', '潜山市天柱山镇河西村卫生室': 'H34088200891', '潜山县梅城镇万岭村卫生室': 'H34088201135', '潜山县梅城镇河湾村卫生室': 'H34088201136', '潜山市黄铺镇湖墩村卫生室': 'H34088200981', '潜山市塔畈乡塔畈村卫生室': 'H34088201195', '潜山市黄铺镇黄铺村卫生室': 'H34088200982', '潜山市王河镇新发村卫生室': 'H34088201019', '潜山县痘姆乡红星村卫生室': 'H34088201107', '潜山市水吼镇三里村卫生室': 'H34088200645', '潜山县黄柏镇大水村卫生室': 'H34088201191', '潜山市油坝乡卫生院': 'H34088200436', '潜山市源潭镇斗塘村卫生室': 'H34088201124', '潜山市王河镇永和村卫生室': 'H34088201002', '潜山市水吼镇驾雾村卫生室': 'H34088200646', '潜山市黄铺镇鲍岭村卫生室': 'H34088200983', '潜山市源潭镇路口村卫生室': 'H34088201108', '潜山市塔畈乡体元村卫生室': 'H34088201198', '潜山市塔畈乡冯冲村卫生室': 'H34088201197', '潜山市王河镇庆丰村卫生室': 'H34088201020', '潜山市水吼镇天堂村卫生室': 'H34088200647', '潜山市槎水镇逆水村卫生室': 'H34088201501', '潜山市槎水镇木岗村卫生室': 'H34088201502', '潜山市槎水镇龙关村卫生室': 'H34088201504', '潜山市槎水镇油坊村卫生室': 'H34088201505', '潜山市槎水镇乐明村卫生室': 'H34088201506', '潜山市槎水镇中畈村卫生室': 'H34088201507', '潜山市槎水镇金波村卫生室': 'H34088201508', '潜山市槎水镇皂河村卫生室': 'H34088201522', '潜山市槎水镇方冲村卫生室': 'H34088201509', '潜山市槎水镇后冲村卫生室': 'H34088201510', '潜山市槎水镇万全村卫生室': 'H34088201511', '潜山市槎水镇槎水村卫生室': 'H34088201512', '潜山市槎水镇滨河居委会卫生室': 'H34088201503', '潜山县余井镇进士村卫生室': 'H34088200967', '潜山县官庄镇坛畈村卫生室': 'H34088201095', '潜山县龙潭乡杜埠村卫生室': 'H34088201003', '潜山市油坝乡唐埠村卫生室': 'H34088200955', '潜山市天柱山镇茶庄村卫生室': 'H34088200888', '潜山市水吼镇程湾村卫生室': 'H34088200648', '潜山县官庄镇西岭村卫生室': 'H34088201109', '潜山县梅城镇彭岭村卫生室': 'H34088201137', '潜山市官庄镇光华村卫生室': 'H34088201110', '潜山县余井镇建军村卫生室': 'H34088200968', '潜山市源潭镇友爱村卫生室': 'H34088201125', '潜山县梅城镇潘铺村卫生室': 'H34088201138', '刘巨旺口腔诊所': 'H34088201827', '潜山市本草堂中医诊所': 'H34088201830'}
    local_hospital_dict = {'潜山市立医院': [], '潜山市中医院': [],
                       '源潭镇': ['潜山市第一人民医院', '潜山市源潭镇田墩村卫生室', '潜山市源潭镇东红村卫生室', '潜山市源潭镇叶典村卫生室', '潜山市源潭镇赵冲村卫生室', '潜山市源潭镇杨泗村卫生室', '潜山市源潭镇双林村卫生室', '潜山市源潭镇三妙居委会卫生室', '潜山市源潭镇源潭居委会卫生室', '潜山市源潭镇双峰居委会卫生室', '潜山市源潭镇光辉村卫生室', '潜山市源潭镇长和居委会卫生室', '潜山市源潭镇东畈村卫生室', '潜山市源潭镇永济村卫生室', '潜山市源潭镇棋盘居委会卫生室', '潜山市源潭镇三河村卫生室', '潜山市源潭镇斗塘村卫生室', '潜山市源潭镇路口村卫生室', '潜山市源潭镇友爱村卫生室'],
                       '黄柏镇': ['潜山市黄柏中心卫生院', '潜山市黄柏镇昆仑村卫生室', '潜山市黄柏镇袁桂村卫生室', '潜山县黄柏镇黄柏村卫生室', '潜山县黄柏镇叶河村卫生室', '潜山市黄柏镇陆河村卫生室', '潜山县黄柏镇大水村卫生室'],
                       '槎水镇': ['潜山市槎水中心卫生院', '潜山市槎水镇逆水村卫生室', '潜山市槎水镇木岗村卫生室', '潜山市槎水镇龙关村卫生室', '潜山市槎水镇油坊村卫生室', '潜山市槎水镇乐明村卫生室', '潜山市槎水镇中畈村卫生室', '潜山市槎水镇金波村卫生室', '潜山市槎水镇皂河村卫生室', '潜山市槎水镇方冲村卫生室', '潜山市槎水镇后冲村卫生室', '潜山市槎水镇万全村卫生室', '潜山市槎水镇槎水村卫生室', '潜山市槎水镇滨河居委会卫生室'],
                       '余井镇': ['潜山县余井中心卫生院', '潜山县余井镇田乐村卫生室', '潜山县余井镇糖岭村卫生室', '潜山县余井镇马道村卫生室', '潜山县余井镇天圣村卫生室', '潜山市余井镇岭头居委会社区卫生服务站', '潜山县余井镇程祠村卫生室', '潜山市余井镇黄岭村卫生室', '潜山县余井镇文治村卫生室', '潜山县余井镇天明村卫生室', '潜山县余井镇余井村卫生室', '潜山县余井镇松岭村卫生室', '潜山县余井镇柴阁村卫生室', '潜山县余井镇进士村卫生室', '潜山县余井镇建军村卫生室'],
                       '梅城镇': ['潜山市梅城镇卫生院', '潜山县梅城镇太平村卫生室', '梅城镇舒苑社区卫生服务站', '潜山县梅城镇东关居委会社区卫生服务站', '潜山县梅城镇模范村卫生室', '潜山县梅城镇双塘村卫生室', '潜山县梅城镇七里村卫生室', '潜山县梅城镇利民村卫生室', '潜山县梅城镇凤凰村卫生室', '潜山市梅城镇河庄村卫生室', '潜山市梅城镇潜阳社区卫生服务中心', '潜山县梅城镇高集村卫生室', '潜山县梅城镇平桥村卫生室', '潜山县梅城镇万岭村卫生室', '潜山县梅城镇河湾村卫生室', '潜山县梅城镇彭岭村卫生室', '潜山县梅城镇潘铺村卫生室', '潜山经济开发区八一社区卫生服务站', '潜山经济开发区古塔社区卫生服务站', '潜山经济开发区三合社区卫生服务站'],
                       '官庄镇': ['潜山市官庄镇卫生院', '潜山县官庄镇升旗村卫生室', '潜山县官庄镇官庄村卫生室', '潜山县官庄镇孔士村卫生室', '潜山市官庄镇金城村卫生室', '潜山市官庄镇杨庄村卫生室', '潜山市官庄镇水贵村卫生室', '潜山县官庄镇日光村卫生室', '潜山县官庄镇戈元村卫生室', '潜山县官庄镇乐平村卫生室', '潜山县官庄镇平峰村卫生室', '潜山县官庄镇坛畈村卫生室', '潜山县官庄镇西岭村卫生室', '潜山市官庄镇光华村卫生室'],
                       '塔畈乡': ['潜山市塔畈乡卫生院', '潜山市塔畈乡周祠村卫生室', '潜山市塔畈乡杏花村卫生室', '潜山市塔畈乡倪河村卫生室', '潜山市塔畈乡新安村卫生室', '潜山市塔畈乡西河村卫生室', '潜山市塔畈乡彭河村卫生室', '潜山市塔畈乡双畈村卫生室', '潜山市塔畈乡板仓村卫生室', '潜山市塔畈乡塔畈村卫生室', '潜山市塔畈乡体元村卫生室', '潜山市塔畈乡冯冲村卫生室'],
                       '龙潭乡': ['潜山县龙潭乡卫生院', '潜山县龙潭乡暗冲村卫生室', '潜山县龙潭乡湖田村卫生室', '潜山县龙潭乡漆铺村卫生室', '潜山县龙潭乡谢河村卫生室', '潜山县龙潭乡白寨村卫生室', '潜山县龙潭乡龙潭村卫生室', '潜山市龙潭乡龙湾村卫生室', '潜山市龙潭乡万涧村卫生室', '潜山县龙潭乡杜埠村卫生室'],
                       '水吼镇': ['潜山市水吼中心卫生院', '潜山市水吼镇水吼村卫生室', '潜山市水吼镇割肚村卫生室', '潜山市水吼镇马潭村卫生室', '潜山市水吼镇风光村卫生室', '潜山市水吼镇和平村卫生室', '潜山市水吼镇高峰村卫生室', '潜山市水吼镇黄龛村卫生室', '潜山市水吼镇天柱村卫生室', '潜山市水吼镇横中村卫生室', '潜山市水吼镇梅寨村卫生室', '潜山市水吼镇三里村卫生室', '潜山市水吼镇驾雾村卫生室', '潜山市水吼镇天堂村卫生室', '潜山市水吼镇程湾村卫生室'],
                       '黄铺镇': ['潜山市黄铺中心卫生院', '潜山市黄铺镇槐树村卫生室', '潜山市黄铺镇古井村卫生室', '潜山市黄铺镇和平村卫生室', '潜山市黄铺镇桃铺村卫生室', '潜山市黄铺镇陈桥村卫生室', '潜山市黄铺镇云峰村卫生室', '潜山市黄铺镇莲花村卫生室', '潜山市黄铺镇古墩村卫生室', '潜山市黄铺镇金龙村卫生室', '潜山市黄铺镇望虎村卫生室', '潜山市黄铺镇张河村卫生室', '潜山市黄铺镇湖墩村卫生室', '潜山市黄铺镇黄铺村卫生室', '潜山市黄铺镇鲍岭村卫生室'],
                       '王河镇': ['潜山市王河中心卫生院', '潜山市王河镇程家井村卫生室', '潜山市王河镇天崇村卫生室', '潜山市王河镇丰收村卫生室', '潜山市王河镇皖潜村卫生室', '潜山市王河镇光明村卫生室', '潜山市王河镇王河村卫生室', '潜山市王河镇先进村卫生室', '潜山市王河镇河镇村卫生室', '潜山市王河镇薛家岗村卫生室', '潜山市王河镇红光村卫生室', '潜山市王河镇长友村卫生室', '潜山市王河镇王河街居委会卫生室', '潜山市王河镇中河村卫生室', '潜山市王河镇龙湖村卫生室', '潜山市王河镇新发村卫生室', '潜山市王河镇永和村卫生室', '潜山市王河镇庆丰村卫生室'],
                       '油坝乡': ['潜山市油坝乡卫生院', '潜山市油坝乡油坝村卫生室', '潜山市油坝乡桑树村卫生室', '潜山市油坝乡崔仓村卫生室', '潜山市油坝乡东店村卫生室', '潜山市油坝乡张祠村卫生室', '潜山市油坝乡唐埠村卫生室'],
                       '黄泥镇': ['潜山市黄泥镇卫生院', '潜山市黄泥镇文昌村卫生室', '潜山市黄泥镇街道居委会卫生室', '潜山市黄泥镇金湖村卫生室', '潜山市黄泥镇前进村卫生室', '潜山市黄泥镇龙坦村卫生室', '潜山市黄泥镇傅祠村卫生室', '潜山市黄泥镇胜利村卫生室'],
                       '五庙乡': ['潜山市五庙乡卫生院', '潜山市五庙乡程冲村卫生室', '潜山市五庙乡杨畈村卫生室', '潜山市五庙乡吴桥村卫生室', '潜山市五庙乡新田村卫生室', '潜山市五庙乡红光村卫生室', '潜山市五庙乡新建村卫生室'],
                       '痘姆乡': ['潜山市痘姆乡卫生院', '潜山县痘姆乡吴塘村卫生室', '潜山县痘姆乡孙塝村卫生室', '潜山县痘姆乡仙驾村卫生室', '潜山县痘姆乡鞔鼓村卫生室', '潜山县痘姆乡求知村卫生室', '潜山县痘姆乡红星村卫生室'],
                       '天柱山镇': ['潜山市天柱山镇卫生院', '潜山市天柱山镇林庄村卫生室', '潜山市天柱山镇风景村卫生室', '潜山市天柱山镇天寺村卫生室', '潜山市天柱山镇白水村卫生室', '潜山市天柱山镇河西村卫生室', '潜山市天柱山镇茶庄村卫生室'],
                       '潜山市妇幼保健计划生育服务中心': [], '潜山东华医院': [], '潜山朝阳医院': [], '潜山同春医院': [], '潜山康视眼科医院': []}
    enumerate_field = ('attribute_dict', "insured_state", "town_village_dict", 'town', 'village', 'person_type', 'hospital_place', 'cure_type_dict', 'cure_type', 'year', 'hospital_community_dict', 'hospital_community',
                  'default_year', 'pay_type_dict', 'pay_type_label', 'cure_type_gather', 'attribute_gather_dict', 'attribute_gather', 'pay_type_operator_dict', 'pay_type_operator_label',
                       'check_dict', 'operate_type', 'check_type', 'check_source', 'hospital_level', 'department', 'position', 'education', 'overyear_refund', 'open_data_type_dict', 'open_data_type', 'hospital_name_id_dict', 'local_hospital_dict', 'compare_year', 'person_type_simple', 'apply_source', 'illness_type', 'sex', 'evidence_type')
    project_type = ('床位费', '诊察费', '检查费', '化验费', '治疗费', '手术费', '护理费', '卫生材料费', '西药费', '中药饮片费', '中成药费', '一般诊疗费', '挂号费', '其他费', '特殊材料费', '血液及血液制品', '单病种除外内容', '国产材料', '集中带量', '进口材料', '康复项目', '国谈药品', '手术材料费', '中草药及中医适宜技术', '氧费', '血制品', '人工晶体', '救护车费', 'MRI费', 'CT费', '彩超费', '输氧费', '输血费', '麻醉费', '麻醉相关项目费', '其他医疗费', '单病种超标准床位费', '单病种定额标准费', '医事服务费', '材料费', '内置材料')
    list_type = ('西药中成药', '中药饮片', '自制剂', '民族药', '医疗服务项目', '医用耗材', '检查费', '中药颗粒')
    project_level = ('甲类', '乙类', '丙类', '可报丙类')


class StaticData:
    own_expense_standard_dict = {'2019': 250, '2020': 250, '2021': 280, '2022': 320, '2023': 350, '2024': 380, '2025': 400}
    town_target_dict = {
        '2020': {'王河镇': 51666, '黄铺镇': 46684, '梅城镇': 74255, '官庄镇': 27433, '油坝乡': 19668, '塔畈乡': 19343, '黄柏镇': 14159,
                 '天柱山镇': 12440, '黄泥镇': 19209, '源潭镇': 60820, '龙潭乡': 18516, '痘姆乡': 17630, '余井镇': 54932, '五庙乡': 10174,
                 '槎水镇': 31963, '开发区': 11898, '水吼镇': 30404},
        '2021': {'王河镇': 51666, '黄铺镇': 46684, '梅城镇': 74255, '官庄镇': 27433, '油坝乡': 19668, '塔畈乡': 19343, '黄柏镇': 14159,
                 '天柱山镇': 12440, '黄泥镇': 19209, '源潭镇': 60820, '龙潭乡': 18516, '痘姆乡': 17630, '余井镇': 54932, '五庙乡': 10174,
                 '槎水镇': 31963, '开发区': 11898, '水吼镇': 30404},
        '2022': {'王河镇': 51666, '黄铺镇': 46684, '梅城镇': 74255, '官庄镇': 27433, '油坝乡': 19668, '塔畈乡': 19343, '黄柏镇': 14159, '天柱山镇': 12440, '黄泥镇': 19209, '源潭镇': 60820, '龙潭乡': 18516, '痘姆乡': 17630, '余井镇': 54932, '五庙乡': 10174, '槎水镇': 31963, '开发区': 11898, '水吼镇': 30404},
        '2023': {'槎水镇': 30993, '痘姆乡': 17129, '水吼镇': 29477, '官庄镇': 26445, '黄柏镇': 13470, '塔畈乡': 18773, '天柱山镇': 12244, '王河镇': 49752, '五庙乡': 9746, '油坝乡': 18946, '开发区': 11448, '龙潭乡': 17870, '余井镇': 52951, '梅城镇': 72615, '源潭镇': 59217, '黄铺镇': 45276, '黄泥镇': 18587},
        '2024': {'梅城镇': 71190, '开发区': 11325, '天柱山镇': 11656, '油坝乡': 18338, '余井镇': 50860, '龙潭乡': 17157, '源潭镇': 56649, '黄柏镇': 12901, '塔畈乡': 18116, '官庄镇': 25455, '槎水镇': 29626, '黄泥镇': 17988, '王河镇': 48290, '黄铺镇': 43798, '痘姆乡': 16544, '水吼镇': 28231, '五庙乡': 9398},
    }


