import random
from api.identity import IdNumber
from walnuts import RequestMapping, Method, Requester
from api.randstr import get_name,generate_random_num,get_tel,generate_random_str,get_time,get_card_id,get_email




@RequestMapping(path='{app.sit_gateway}',method=Method.POST)
class LXIN:

    @RequestMapping(method=Method.POST)
    def PATSCMSS5005(self):
        '''授信申请'''
        seqno = generate_random_str(17)
        calseqno = "LN" + generate_random_num(12)
        name = get_name()
        mobile = get_tel()
        mail = get_email()
        cardNo = get_card_id()
        applyNo = generate_random_num(18)
        userid = "user"+generate_random_num(9)
        random_sex = random.randint(1, 2)
        applyTime = get_time()
        idnumber = IdNumber.generate_id(random_sex)
        birthDate = IdNumber.get_birthday(idnumber)

        header = {
            "api_id":"PATSCMSS5005",
            "country":"cn",
            "calseqno":seqno,
            "dapplication":"81001",
            "service":"PATSCMSS5005",
            "callseqno":calseqno,
            "dgroup":"onl01",
            "dversion":"1.0",
            "busiseqno":calseqno,
            "Content-Type":"application/json"
        }
        data = {
            "applyNo":applyNo,
            "channelCode":"LXIN",
            "applyTime":applyTime,
            "prodCode":"02050015",
            "applyAmt":"20000",
            "applyPeriod":"12",
            "userInfo":{
                "userId":userid,
                "custName":name,
                "certNo":idnumber,
                "gender":random_sex,
                "cardNo":cardNo,
                "mobileNo":mobile,
                "emaill":mail,
                "certType": "101",
                "certValidStart": "20200810",
                "certValidEnd": "99991231",
                "birthDate": birthDate,
                "marryStatus": "10",
                "eduLevel": "010",
                "degree": "5",
                "yearIncome": "200000",
                "inctry": "156",
                "liveStatus": "5",
                "liveYear": "5",
                "liveAddProvince": "上海",
                "liveAddCity": "上海",
                "liveAddArea": "黄浦区",
                "liveAddress": "滇池路81号嘉煜外滩中心",
                "cardTpye": "0",
                "workInfo": {
                    "empName": "上海中银消费",
                    "empTelNo": "010-88888888",
                    "empIndustry": "J",
                    "empProp": "0",
                    "workAddProvince": "上海市",
                    "workAddCity": "上海",
                    "workAddArea": "黄浦区",
                    "workAddDetail": "滇池路74号中银消费",
                    "empZipCode": "200120",
                    "profession": "0",
                    "jobTit": "9",
                    "jobPos": "9",
                },
                "emergList":{
                    "emergRelation":"PARENT",
                    "emergName":"毛链",
                    "emergTel": "17395800902",
                    "emergCertNo": "130701197605236186",
                }
            },
        }
        return Requester(headers=header, json=data)


    @RequestMapping(method=Method.POST)
    def PATSCMSS5006(self,applyNo):
        '''授信申请查询'''
        seqno = generate_random_str(11)
        header = {
            "api_id": "PATSCMSS5006",
            "country": "cn",
            "calseqno": seqno,
            "dapplication": "81001",
            "service": "PATSCMSS5006",
            "callseqno": seqno,
            "dgroup": "onl01",
            "dversion": "1.0",
            "busiseqno": seqno,
            "Content-Type": "application/json"
        }
        data = {
            "applyNo":applyNo,
            "channelCode":"LXIN",
            "prodCode":"02050015"
        }
        return Requester(header = header, json = data)


    @RequestMapping(method=Method.POST)
    def PATSCMSS6002(self):
        '''借款申请-标准'''
        seqno = generate_random_str(11)
        applyTime = get_time()
        header = {
            "api_id": "PATSCMSS6002",
            "country": "cn",
            "calseqno": seqno,
            "dapplication": "81001",
            "service": "PATSCMSS6002",
            "callseqno": seqno,
            "dgroup": "onl01",
            "dversion": "1.0",
            "busiseqno": seqno,
            "Content-Type": "application/json"
        }
        data = {
            "applyNo":"",
            "paymentApplyNo":"",
            "channelCode": "",
            "userId": "",
            "applyTime": applyTime,
            "prodCode": "02050015",
            "applyAmt": "",
            "applTnr": "",
            "repytp": "",
            "intRate": "",
            "loanPurpose": "",
            "insureNo": "",
            "busiScen": "",
            "extInfo": {
                "busiType":""
            },
        }
        return Requester(header=header, json=data)

    @RequestMapping(method=Method.POST)
    def PATSCMSS6003(self):
        '''乐信借款审批结果查询'''
        header = {}
        data = {
            "applyNo":"",
            "channelCode":"LXIN",
            "prodCode":"02050015"
        }
        return Requester(header=header, json=data)


    @RequestMapping(method=Method.POST)
    def PATSCMSS7001(self):
        '''借款支用申请-标准'''
        header = {}
        data = {
            "applyNo":"",
            "paymentApplyNo":"",
            "channelCode":"",
            "userId":"",
            "applyTime": "",
            "payDayRule": "",
            "payDay": "",
            "cashPayFlag": "",
            "payType": "",
            "acctName": "",
            "acctNo": "",
            "acctType": "",
            "openAcctBank": "",
            "mobileNo":""
        }
        return Requester(header=header, json=data)

    @RequestMapping(method=Method.POST)
    def PATSCMSS7002(self,paymentApplyNo):
        '''借款支用结果查询-标准'''
        header = {}
        data = {
            "paymentApplyNo":"",
            "channelCode":"LXIN",
            "prodCode":"02050015"
        }
        return Requester(header=header, json=data)

    @RequestMapping(method=Method.POST)
    def PATSCMSS8001(self):
        '''乐信查询还款计划'''
        header = {}
        data = {
            "loanNo":"",
            "channelCode":""
        }
        return Requester(header=header, json=data)

    @RequestMapping(method=Method.POST)
    def PATSCMSS8002(self):
        '''乐信提前还款试算'''
        header = {}
        data = {
            "loanNo":"",
            "channelCode":"",
            "repayType": "",
            "mode": "",
            "repayAmt": "",
            "paymentApplyNo": "",
        }
        return Requester(header=header, json=data)
