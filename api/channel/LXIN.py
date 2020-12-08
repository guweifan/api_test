import random
import os
import time
from api.Uploadfile import get_tar, upload_LXIN
from api.identity import IdNumber
from walnuts import RequestMapping, Method, Requester
from api.randstr import get_name,generate_random_num,get_tel,get_time,get_card_id,get_email,get_date



@RequestMapping(path='{app.sit1_gateway}',method=Method.POST)
class LXIN:

    @RequestMapping(method=Method.POST)
    def PATSCMSS5005(self):
        '''乐信授信申请'''
        seqno = generate_random_num(17)
        calseqno = "LN" + generate_random_num(12)
        name = get_name()
        mobile = get_tel()
        mail = get_email()
        cardNo = "6216610200016587010"
        applyNo = generate_random_num(18)
        userid = "user"+generate_random_num(9)
        random_sex = random.randint(1, 2)
        applyTime = get_time()
        date = get_date()
        idnumber = IdNumber.generate_id(random_sex)
        birthDate = IdNumber(idnumber).get_birthday()

        """影像件上传155 SFTP"""
        tar = get_tar(applyNo=applyNo)
        src = "D:\\Python_work\\walnuts_api\\api_test\\img\\" + tar
        path = "/upload/LXIN/photo/" + date + "/" + tar
        upload_LXIN(src, path)
        time.sleep(1)
        os.remove(src)

        """报文头信息"""
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
        "input":{
            "applyNo":applyNo,
            "channelCode":"LXIN",
            "applyTime":applyTime,
            "prodCode":"LXIN001",
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
                "monthIncome": "5",
                "inctry": "156",
                "liveStatus": "5",
                "liveYear": "5",
                "liveAddProvince": "上海",
                "liveAddCity": "上海",
                "liveAddArea": "黄浦",
                "liveAddress": "滇池路81号嘉煜外滩中心",
                "cardTpye": "C",
                "workInfo": {
                    "empName": "上海中银消费",
                    "empTelNo": "010-88888888",
                    "empIndustry": "J",
                    "empProp": "0",
                    "workAddProvince": "上海",
                    "workAddCity": "上海",
                    "workAddArea": "黄浦",
                    "workAddDetail": "滇池路74号中银消费",
                    "empZipCode": "200120",
                    "profession": "0",
                    "jobTit": "9",
                    "jobPos": "9",
                },
                "emergList": [
                    {
                    "emergName": "马保国",
                    "emergRelation": "PARENT",
                    "emergTel": "15936617570",
                    "emergCertNo": "440300196308081042"
                    }
                ]
            }
            },
        "comm_req": {
                "trantm": "752512",
                "initiator_system": "301",
                "app_version": "1.0",
                "trxn_branch": "77710",
                "call_seq": calseqno,
                "trxn_teller": "95068241",
                "sponsor_system": "810",
                "auth_user_id": "587046",
                "servtp": "TE",
                "sys_version": "1.0",
                "inpudt": date,
                "servno": "004",
                "busi_seq": seqno,
                "page_start": "1",
                "trxn_seq": seqno,
                "tranbr": date,
                "trandt": date,
                "longitude": "31.2579921",
                "page_size": "10",
                "orderSeq": calseqno,
                "phone_type": "0",
                "initiator_date": date,
                "inpucd": "985",
                "busisq": seqno,
                "rsa_key": "77777777777777",
                "inpusq": calseqno,
                "corpno": "985",
                "ip_address": "127.0.0.1",
                "busi_org_id": "025",
                "busiseqno": seqno,
                "terminal_os_type": "0",
                "tranus": "xadmin",
                "initiator_seq": calseqno,
                "pageIndex": "1",
                "pageno": "1",
                "pgsize": "1",
                "callseqno": calseqno,
                "channel_id": "LXIN"
            }
        }
        return Requester(headers=header, json=data)


    @RequestMapping(method=Method.POST)
    def PATSCMSS5006(self,applyNo):
        '''授信申请查询'''
        seqno = generate_random_num(17)
        calseqno = "LN" + generate_random_num(12)
        date = get_date()

        """报文头信息"""
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
            "input":{
                "applyNo": applyNo,
                "channelCode": "LXIN",
                "prodCode": "02050015"
            },
            "comm_req": {
                "trantm": "752512",
                "initiator_system": "301",
                "app_version": "1.0",
                "trxn_branch": "77710",
                "call_seq": calseqno,
                "trxn_teller": "95068241",
                "sponsor_system": "810",
                "auth_user_id": "587046",
                "servtp": "TE",
                "sys_version": "1.0",
                "inpudt": date,
                "servno": "004",
                "busi_seq": seqno,
                "page_start": "1",
                "trxn_seq": seqno,
                "tranbr": date,
                "trandt": date,
                "longitude": "31.2579921",
                "page_size": "10",
                "orderSeq": calseqno,
                "phone_type": "0",
                "initiator_date": date,
                "inpucd": "985",
                "busisq": seqno,
                "rsa_key": "77777777777777",
                "inpusq": calseqno,
                "corpno": "985",
                "ip_address": "127.0.0.1",
                "busi_org_id": "025",
                "busiseqno": seqno,
                "terminal_os_type": "0",
                "tranus": "xadmin",
                "initiator_seq": calseqno,
                "pageIndex": "1",
                "pageno": "1",
                "pgsize": "1",
                "callseqno": calseqno,
                "channel_id": "LXIN"
            }
        }
        return Requester(headers=header, json=data)


    @RequestMapping(method=Method.POST)
    def PATSCMSS6002(self,applyNo):
        '''借款申请-标准'''
        seqno = generate_random_num(17)
        calseqno = "LN" + generate_random_num(12)
        date = get_date()
        applyTime = get_time()
        paymentApplyNo = "L" + generate_random_num(13)

        """报文头信息"""
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
            "applyNo":applyNo,
            "paymentApplyNo":paymentApplyNo,
            "channelCode": "LXIN",
            "userId": "",
            "applyTime": applyTime,
            "prodCode": "02050015",
            "applyAmt": "2000",
            "applTnr": "12",
            "repytp": "1",
            "intRate": "",
            "loanPurpose": "",
            "insureNo": "",
            "busiScen": "0",
            "extInfo": {
                "busiType":"3"
            },
            "comm_req": {
                "trantm": "752512",
                "initiator_system": "301",
                "app_version": "1.0",
                "trxn_branch": "77710",
                "call_seq": calseqno,
                "trxn_teller": "95068241",
                "sponsor_system": "810",
                "auth_user_id": "587046",
                "servtp": "TE",
                "sys_version": "1.0",
                "inpudt": date,
                "servno": "004",
                "busi_seq": seqno,
                "page_start": "1",
                "trxn_seq": seqno,
                "tranbr": date,
                "trandt": date,
                "longitude": "31.2579921",
                "page_size": "10",
                "orderSeq": calseqno,
                "phone_type": "0",
                "initiator_date": date,
                "inpucd": "985",
                "busisq": seqno,
                "rsa_key": "77777777777777",
                "inpusq": calseqno,
                "corpno": "985",
                "ip_address": "127.0.0.1",
                "busi_org_id": "025",
                "busiseqno": seqno,
                "terminal_os_type": "0",
                "tranus": "xadmin",
                "initiator_seq": calseqno,
                "pageIndex": "1",
                "pageno": "1",
                "pgsize": "1",
                "callseqno": calseqno,
                "channel_id": "LXIN"
            }
        }
        return Requester(headers=header, json=data)

    @RequestMapping(method=Method.POST)
    def PATSCMSS6003(self):
        '''乐信借款审批结果查询'''
        header = {}
        data = {
            "input":{
                "applyNo": "",
                "channelCode": "LXIN",
                "prodCode": "02050015"
            },
        }
        return Requester(headers=header, json=data)


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
        return Requester(headers=header, json=data)

    @RequestMapping(method=Method.POST)
    def PATSCMSS7002(self,paymentApplyNo):
        '''借款支用结果查询-标准'''
        header = {}
        data = {
            "paymentApplyNo":"",
            "channelCode":"LXIN",
            "prodCode":"02050015"
        }
        return Requester(headers=header, json=data)

    @RequestMapping(method=Method.POST)
    def PATSCMSS8001(self):
        '''乐信查询还款计划'''
        header = {}
        data = {
            "loanNo":"",
            "channelCode":""
        }
        return Requester(headers=header, json=data)

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
        return Requester(headers=header, json=data)
