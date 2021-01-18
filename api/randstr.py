import random
import time
from api.identity import *
from api.firstname import first_name
from api.langconv import *
import hashlib





# 手机号开头
phone_number = [139,138,137,136,135,134,159,158,15,150,151,152,188,
                130,131,132,156,155,133,153,173,189]

# 随机生成姓名
def get_name():
    name_code = ''
    # 在百家姓列表里面随便选择一个姓
    name_code += random.choice(first_name)
    ran_num = random.randint(0,1)
    # 为0生成的名字是两个字，为1生成的名字是一个字
    if ran_num == 0:
        for i in range(2):
            # 从十进制汉字编码随机选取一个
            ran = random.randint(19968, 40869)
            # 将其转换为汉字
            ran = chr(ran)
            name_code += ran
    else:
        # 从十进制汉字编码随机选取一个
        ran = random.randint(19968, 40869)
        # 将其转换为汉字
        ran = chr(ran)
        name_code += ran
    # 将name_code里面的繁体字转换为简体字
    name_code = Converter('zh-hans').convert(name_code)
    # 编码
    name_code.encode('utf-8')
    return name_code

# 随机生成出生日期
# def get_birthday():
#     # 随机生成年月
#     year = random.randint(1960, 2000)
#     month = random.randint(1, 12)
#     # 判断每个月多少天随机生成日
#     if year % 4 == 0:
#         if month in (1, 3, 5, 7, 8, 10, 12):
#             day = random.randint(1, 31)
#         elif month in (4, 6, 9, 11):
#             day = random.randint(1, 30)
#         else:
#             day = random.randint(1, 29)
#     else:
#         if month in (1, 3, 5, 7, 8, 10, 12):
#             day = random.randint(1, 31)
#         elif month in (4, 6, 9, 11):
#             day = random.randint(1, 30)
#         else:
#             day = random.randint(1, 28)
#     # 小于10 的月份前面加0
#     if month < 10:
#         month = '0' + str(month)
#     if day < 10:
#         day = '0' + str(day)
#     birthday = str(year)+ str(month) + str(day)
#     return birthday

# 匿名函数

get_sex = lambda:random.choice(['男','女'])

# 随机生成手机号
def get_tel():
    tel = ''
    tel += str(random.choice(phone_number))
    ran = ''
    for i in range(8):
        ran += str(random.randint(0, 9))
    tel += ran
    return tel

# 随机生成银行卡号
def get_card_id():
    card_id = '621661'
    for i in range(13):
        ran = str(random.randint(0, 9))
        card_id += ran
    return card_id

# 随机生成邮箱
def get_email():
    email_suf = random.choice(['@163.com','@qq.com','@126.com','@sina.com','@sina.cn','@soho.com','@yeah.com'])
    phone = get_tel()
    email = phone + email_suf
    return email


def get_time():
    """生成时间戳"""
    now = int(time.time())
    timeArray = time.localtime(now)
    otherStyleTime = time.strftime("%Y%m%d%H%M%S", timeArray)
    return otherStyleTime

def get_date():
    """获取当前日期"""
    today = get_time()
    todaylist = list(today)
    todaystr = ''.join(todaylist[:8])
    return todaystr

def generate_random_str(randomlength=16):
    """
    生成一个指定长度的随机字符串
    """
    random_str = ''
    base_str = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789'
    length = len(base_str) - 1
    for i in range(randomlength):
        random_str += base_str[random.randint(0, length)]
    return random_str


def generate_random_num(randomlength=16):
    """
    生成一个指定长度的随机字符串
    """
    random_num = ''
    base_str = '0123456789'
    length = len(base_str) - 1
    for i in range(randomlength):
        random_num += base_str[random.randint(0, length)]
    return random_num

def getStrAsMD5(parmStr):
    if isinstance(parmStr,str):
    	 # 如果是unicode先转utf-8
    	parmStr = parmStr.encode("utf-8")
    m = hashlib.md5()
    m.update(parmStr)
    return m.hexdigest()




