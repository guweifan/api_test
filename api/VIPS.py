import random
from api.identity import IdNumber
from api.Uploadfile import upload, rename
from walnuts import RequestMapping, Method, Requester
from api.randstr import get_name,generate_random_num,get_tel,generate_random_str,get_time,get_date,get_birthday,get_email




@RequestMapping(path='{app.vip_encrvption}', method=Method.POST)
class Encrvption:

    @RequestMapping(method=Method.POST)
    def VIPS_apply(self):
        '''授信申请接口加密'''
        seqno = generate_random_str(9)
        userBirthDate = get_birthday()
        todaydate = get_date()

        # 客户信息
        custName = get_name()  # 客户名称
        usertel = get_tel()  # 电话号码
        spname = get_name()  # 配偶名称
        emergTel = get_tel()  # 配偶联系安话
        email = get_email()  # 邮件地址
        random_sex = random.randint(0, 1)
        idnumber = IdNumber.generate_id(random_sex)  # 客户身份证号码
        # 申请单号
        referno = "BO" + generate_random_num(16)

        """影像件上传"""
        applyImgPath = "/lttsdata/ICMS/VIPS" + referno + "/1.jpg"
        src_file = 'D:\\Python_work\\walnuts_api\\api_test\\img\\'
        src_file = rename(src_file, referno)
        src_file = src_file + "\\1.jpg"
        upload(src_file, applyImgPath)

        data = {
            "header":{
                    "requestNo":seqno,
                    "timestamp":seqno,
                    "merchantId":"VIP",
                    },
            "body":{
                "openAccountOrderNo":referno,
                "userBaseInfo":{
                    "userName":custName,
                    "userMobile":usertel,
                    "idType":"0",
                    "userIdNo":idnumber,
                    "userIdIssueOrg":"公安局",
                    "userIdStartDate":"20180916",
                    "userIdExpiryDate":"20280916",
                    "userNation":"01",
                    "userSex":random_sex + 1,
                    "userBirthDate":userBirthDate,
                    "education":"DOCTOR",
                    "userMaritalStatus":"MARRIED_NO_CHILDREN",
                    "userOccupation":"020403",
                    "userCardNo":"622202649761688358",
                    "userCardType":"10",
                    "spouseName":spname,
                    "spouseMobile":emergTel,
                    "spouseCertType":"0",
                    "spouseIdNo":"110101199210015111",
                    "spouseExpiryDate":"20280916",
                    "spouseCorp":"上海市棉花糖厂",
                    "userCorp":"上海市棉花糖厂",
                    "userCorpAddr":"上海市浦东新区蓝天路778号",
                    "userCorpType":"",
                    "userCorpZip":"",
                    "userEmail":email,
                    "userResidenceAddrProvince":"上海市",
                    "userResidenceAddrCity":"上海市",
                    "userResidenceAddrCounty":"浦东新区",
                    "userResidenceAddr":"上海市浦东新区蓝天路233号",
                    "userLiveAddrProvince":"上海市",
                    "userLiveAddrCity":"上海市",
                    "userLiveAddrCounty":"浦东新区",
                    "userLiveAddr":"上海市浦东新区蓝天路233号",
                    "userLiveZip":"200120",
                    "userLiveStatus":"TENEMENT",
                },
                "contactInfo":{
                    "emergencyContactName":spname,
                    "emergencyContactMobile":emergTel,
                    "emergencyContactRelType":"SPOUSE",
                },
                "incomeInfo":{
                    "monthIncome":"6",
                    "yearIncome":"",
                    "familyIncom":"",
                    "moreIncome":"",
                    "taxIdCode":"",
                },
                "riskInfo":{
                    "limit":"20000",
                    "dailyIntRate":"",
                    "yearIntRate":"0.237600",
                    "vipApplyScore":"",
                },
                "extraInfo":{
                    "bizDate":todaydate,
                    "ocrType":"01",
                }
            }
        }

        return Requester(json=data)

# 招联授信
@RequestMapping(path='{app.vip_apply}', method=Method.POST)
class openAccount:

    @RequestMapping(method=Method.POST)
    def creditApply(self):
        '''授信申请接口'''
        fun = Encrvption()
        data = fun.VIPS_apply().json()
        return Requester(json=data)











# if __name__ == '__main__':
    # http_bin = vip_encryption()
    # http_bin.add_header_to_all()
    # http_bin.post_form().json()
    # print(http_bin.vip_encryption())
    # http_bin.path_var().json()
    # post_json()

