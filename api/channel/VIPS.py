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
        src_file = '/img\\'
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
class loanApply:

    @RequestMapping(method=Method.POST)
    def loanApply(self):
        '''唯品会提现申请'''
        seqno = generate_random_num(12)
        headers = {
        "dserviceId":"PATSVPSS2001",
        "api_id":"PATSVPSS2001",
        "callseqno":seqno,
        "busiseqno":seqno,
        "calseqno":seqno,
        "dversion":"1.0",
        "Content-Type":"application/json"
        }
        data = {
        "input": {
        "amount": "500.00",
        "loanUse": "A",
        "graceDay": "2",
        "trxnType": "1",
        "dailyIntRate": "0.00018",
        "openAccountOrderNo": "BO2398009046872288",
        "requestNo": "1601273994464141910",
        "userName": "祝嬖",
        "repayType": "01",
        "userCardNo": "622909049100014018",
        "userIdExpiryDate": "20290907",
        "stage": "3",
        "channelUserId": "B00000000379",
        "userMobile": "15892870937",
        "loanOrderNo": "62290904910001421",
        "userIdStartDate": "20280916",
        "yearIntRate": "0.36",
        "repayDate": "",
        "bankCardCode": "CIB",
        "channelCode": "VIP",
        "userIdNo": "220801196004073943",
        "extraInfo": ""
    },
    "comm_req": {
        "initiator_date": "20200928",
        "initiator_system": "333",
        "trxn_branch": "3443",
        "initiator_seq": seqno,
        "call_seq": seqno,
        "busi_seq": seqno,
        "sponsor_system": "100",
        "busi_org_id": "985",
        "channel_id": "VIPS"
    }
}











# if __name__ == '__main__':
    # http_bin = vip_encryption()
    # http_bin.add_header_to_all()
    # http_bin.post_form().json()
    # print(http_bin.vip_encryption())
    # http_bin.path_var().json()
    # post_json()

