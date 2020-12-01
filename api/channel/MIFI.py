import random
from api.identity import IdNumber
from api.Uploadfile import rename,upload,upload_MI
from api.savecustinfo import readExcel,writeExcel
from walnuts import RequestMapping, Method, Requester
from api.randstr import get_name,generate_random_num,get_tel,generate_random_str,get_time




@RequestMapping(path='{app.sit1_gateway}',method=Method.POST)
class MIFI_apply:


    @RequestMapping(method=Method.POST)
    def mifi_apply(self):
        '''授信申请'''
        seqno = generate_random_str(17)
        calseqno = "LN" + generate_random_num(12)
        name = get_name()
        mobile = get_tel()
        openId = generate_random_num(9)
        applyNo = "GU" + generate_random_num(10)
        random_sex = random.randint(1, 2)
        applyTime = get_time()
        idnumber = IdNumber.generate_id(random_sex)

        """sit2影像件上传"""
        filename = "IMG_" + applyNo + "_" + applyTime + ".tar.gz"
        src_file = 'D:\\Python_work\\walnuts_api\\api_test\\resources\\'
        applyImgPath = "/lttsdata/MIFI/img/" + filename
        src_file = rename(src_file,filename)
        upload(src_file, applyImgPath)

        # """sit影像件上传"""
        # filename = "IMG_" + applyNo + "_" + applyTime + ".tar.gz"
        # src_file = 'D:\\Python_work\\walnuts_api\\api_test\\resources\\'
        # applyImgPath = "/pc_zyxj/credit/img/20201102/" + filename
        # src_file = rename(src_file, filename)
        # upload_MI(src_file, applyImgPath)

        """存储客户信息"""
        custinfo = [name, mobile, idnumber, applyNo, openId, applyImgPath]
        writeExcel(sheetname=idnumber, custinfo=custinfo)
        """定义请求header和body"""
        header = {
            "api_id":"PATSMISS1001",
            "country":"cn",
            "calseqno":seqno,
            "dapplication":"81001",
            "service":"PATSMISS1001",
            "callseqno":calseqno,
            "dgroup":"onl01",
            "dversion":"1.0",
            "busiseqno":calseqno,
            "Content-Type":"application/json"
        }
        data = {
            "input":{
                "openId":openId,
                "applyNo":applyNo,
                "applyTime":applyTime,
                "channelCode":"MIFI",
                "timestamp":"",
                "bankInfo": {
                    "certNo": idnumber,
                    "name": name,
                    "mobile": mobile,
                    "bankName": "中国银行",
                    "cardNo": "6216610200016587010",
                    "idNum": idnumber
                },
                "userInfo": {
                    "name": name,
                    "mobile": mobile,
                    "idNum": idnumber,
                    "openId": openId
                },
                "extInfo":{
                    "incomeLevel":"6",
                    "applyImgPath":applyImgPath,
                    "applyAuthPath":"",
                    "industry":{
                        "firstCode":"B",
                        "firstName":"采矿业",
                        "secondCode":"C",
                        "secondName":"制造业"
                    },
                    "career":{
                        "firstCode":"Y",
                        "firstName":"不便分类的其他从业人员",
                        "secondCode":"Z",
                        "secondName":"未知"
                    },
                    "faceCmpScore":"",
                    "companyName":"棉花糖厂",
                    "riskData":{
                        "associateDeviceCount":"",
                        "devicePrintAssociateAccountCount":"",
                        "gPSConsistency":"",
                        "devicePrintNull":"",
                        "isMobileTypeChange":"",
                        "deviceIsBlack":"",
                        "associateDevicePrintCount":"",
                        "isFrequentlyUsedDevicePrint":"",
                        "devicePrintIsBlack":"",
                        "deviceAssociateAccountCount":"",
                        "deviceNull":"",
                        "deviceSystem":"",
                        "iPConsistency":"",
                        "iPConcentration":"",
                        "gPSConcentration":"",
                        "mobileTypeNull":"",
                        "isFrequentlyUsedDevice":""
                    },
                    "ocr":{
                        "nameOcr":name,
                        "numberOcr":idnumber,
                        "addressOcr":"上海",
                        "ethnicOcr":"汉",
                        "dueTimeOcr":"20100801_20300801",
                        "sexOcr":"male",
                        "issueOrgOcr":"公安局"
                    },
                }
            },
            "comm_req":{
                "trantm":"752512",
                "initiator_system":"301",
                "app_version":"1.0",
                "trxn_branch":"77710",
                "call_seq":calseqno,
                "trxn_teller":"95068241",
                "sponsor_system":"810",
                "auth_user_id":"587046",
                "servtp":"TE",
                "sys_version":"1.0",
                "inpudt":"20200604",
                "servno":"004",
                "busi_seq":seqno,
                "page_start":"1",
                "trxn_seq":seqno,
                "tranbr":"985000",
                "trandt":"20200604",
                "longitude":"31.2579921",
                "page_size":"10",
                "orderSeq":calseqno,
                "phone_type":"0",
                "initiator_date":"20200711",
                "inpucd":"985",
                "busisq":seqno,
                "rsa_key":"77777777777777",
                "inpusq":calseqno,
                "corpno":"985",
                "ip_address":"127.0.0.1",
                "busi_org_id":"025",
                "busiseqno":seqno,
                "terminal_os_type":"0",
                "tranus":"xadmin",
                "initiator_seq":calseqno,
                "pageIndex":"1",
                "pageno":"1",
                "pgsize":"1",
                "callseqno":calseqno,
                "channel_id":"MIFI"
            }
        }
        return Requester(headers=header, json=data)

    @RequestMapping(method=Method.POST)
    def mifi_pay(self, idnum, applyId):
        '''用信申请'''
        seqno = generate_random_str(17)
        calseqno = "LN" + generate_random_num(12)
        paymentNo = "pay" + generate_random_num(10)
        mobile1 = get_tel()
        mobile2 = get_tel()

        # 读取excel，获取客户信息
        custinfo = readExcel(idnum)

        name = custinfo[0]
        mobile = custinfo[1]
        idnumber = custinfo[2]
        applyNo = custinfo[3]
        openId = custinfo[4]
        applyImgPath = custinfo[5]

        header = {
            "api_id":"PATSMISS2001",
            "country":"cn",
            "calseqno":calseqno,
            "dapplication":"81001",
            "service":"PATSMISS2001",
            "callseqno":calseqno,
            "dgroup":"onl01",
            "dversion":"1.0",
            "busiseqno":calseqno,
            "Content-Type":"application/json"
        }
        data = {
                "input":{
                    "paymentNo": paymentNo,
                    "applyId": applyId,
                    "applyNo": applyNo,
                    "idNum": idnumber,
                    "idType": "CNI",
                    "openId": openId,
                    "mobile": mobile,
                    "userName": name,
                    "loanUse":"1",
                    "contact1Name":"张三",
                    "contact1Relation": "01",
                    "contact1MobileNo": mobile1,
                    "contact2Name":"李四",
                    "contact2Relation":"02",
                    "contact2MobileNo": mobile2,
                    "riskData":{
                        "associateDeviceCount":"0",
                        "devicePrintAssociateAccountCount":"0",
                        "gPSConsistency":"0",
                        "devicePrintNull":"0",
                        "isMobileTypeChange":"0",
                        "deviceIsBlack":"0",
                        "associateDevicePrintCount":"0",
                        "isFrequentlyUsedDevicePrint":"0",
                        "devicePrintIsBlack":"0",
                        "deviceAssociateAccountCount":"0",
                        "deviceNull":"0",
                        "deviceSystem":"0",
                        "iPConsistency":"0",
                        "iPConcentration":"0",
                        "gPSConcentration":"0",
                        "mobileTypeNull":"0",
                        "isFrequentlyUsedDevice":"0"
                    },
                    "loanAmount":"100000",
                    "firstRepayDay":"",
                    "extInfo":{
                        "faceCmpScore":"",
                        "industry":{
                        "firstCode":"",
                        "firstName":"",
                        "secondCode":"",
                        "secondName":""
                    },
                        "career":{
                        "firstCode":"",
                        "firstName":"",
                        "secondCode":"",
                        "secondName":""
                    },
                        "companyName":"",
                        "applyAuthPath":"",
                        "applyImgPath":"",
                        "incomeLevel":"",
                    },
                    "bankAmount":"300000",
                    "bankCardNum":"6216610200016587010",
                    "term":"12",
                    "loanRate":"23.900000",
                    "channelCode":"MIFI"
                },
                "comm_req":{
                    "trantm":"065575",
                    "initiator_system":"301",
                    "app_version":"1.0",
                    "trxn_branch":"51636",
                    "call_seq":"393713849625",
                    "trxn_teller":"79632141",
                    "sponsor_system":"810",
                    "auth_user_id":"419195",
                    "servtp":"TE",
                    "sys_version":"1.0",
                    "inpudt":"20200604",
                    "servno":"004",
                    "busi_seq":seqno,
                    "page_start":"1",
                    "trxn_seq":seqno,
                    "tranbr":"985000",
                    "trandt":"20200604",
                    "longitude":"31.2579921",
                    "page_size":"10",
                    "orderSeq":seqno,
                    "phone_type":"0",
                    "initiator_date":"20200711",
                    "inpucd":"985",
                    "busisq":seqno,
                    "rsa_key":"77777777777777",
                    "inpusq":seqno,
                    "corpno":"985",
                    "ip_address":"127.0.0.1",
                    "busi_org_id":"025",
                    "busiseqno":seqno,
                    "terminal_os_type":"0",
                    "tranus":"xadmin",
                    "initiator_seq":seqno,
                    "pageIndex":"1",
                    "pageno":"1",
                    "pgsize":"1",
                    "callseqno":seqno,
                    "channel_id":"MIFI"
                }
            }
        return Requester(headers=header, json=data)


    @RequestMapping(method=Method.POST)
    def mifi_apply_query(self, applyNo, openId):
        '''授信结果查询'''
        seqno = generate_random_str(10)
        calseqno = "LN" + generate_random_num(12)
        header= {
                "api_id":"PATSMISS1002",
                "country":"cn",
                "calseqno":calseqno,
                "dapplication":"81001",
                "service":"PATSMISS1002",
                "callseqno":calseqno,
                "dgroup":"onl01",
                "dversion":"1.0",
                "busiseqno":calseqno,
                "Content-Type":"application/json"
            }

        data={
            "input":{
                "openId":openId,
                "applyNo":applyNo
            },
            "comm_req":{
                "trantm":"058444",
                "initiator_system":"301",
                "app_version":"1.0",
                "trxn_branch":"27133",
                "call_seq":seqno,
                "trxn_teller":"90148331",
                "sponsor_system":"810",
                "auth_user_id":"978230",
                "servtp":"TE",
                "sys_version":"1.0",
                "inpudt":"20200604",
                "servno":"004",
                "busi_seq":seqno,
                "page_start":"1",
                "trxn_seq":calseqno,
                "tranbr":"985000",
                "trandt":"20200604",
                "longitude":"31.2579921",
                "page_size":"10",
                "orderSeq":seqno,
                "phone_type":"0",
                "initiator_date":"20200711",
                "inpucd":"985",
                "busisq":seqno,
                "rsa_key":"77777777777777",
                "inpusq":calseqno,
                "corpno":"985",
                "ip_address":"127.0.0.1",
                "busi_org_id":"025",
                "busiseqno":seqno,
                "terminal_os_type":"0",
                "tranus":"xadmin",
                "initiator_seq":calseqno,
                "pageIndex":"1",
                "pageno":"1",
                "pgsize":"1",
                "callseqno":calseqno,
                "channel_id":"MIFI"
            }
        }
        return Requester(headers=header, json=data)


    @RequestMapping(method=Method.POST)
    def mifi_pay_query(self,paymentNo, openId):
        '''用信结果查询'''
        seqno = generate_random_str(10)
        calseqno = "LN" + generate_random_num(12)
        header ={
            "api_id":"PATSMISS2002",
            "country":"cn",
            "calseqno":calseqno,
            "dapplication":"81001",
            "service":"PATSMISS2002",
            "callseqno":calseqno,
            "dgroup":"onl01",
            "dversion":"1.0",
            "busiseqno":calseqno,
            "Content-Type":"application/json"
        }
        data = {
            "input":{
                "paymentNo":paymentNo,
                "openId":openId
            },
            "comm_req":{
                "trantm":"093941",
                "initiator_system":"301",
                "app_version":"1.0",
                "trxn_branch":"09451",
                "call_seq":calseqno,
                "trxn_teller":"45319371",
                "sponsor_system":"810",
                "auth_user_id":"068503",
                "servtp":"TE",
                "sys_version":"1.0",
                "inpudt":"20200604",
                "servno":"004",
                "busi_seq":calseqno,
                "page_start":"1",
                "trxn_seq":calseqno,
                "tranbr":"985000",
                "trandt":"20200604",
                "longitude":"31.2579921",
                "page_size":"10",
                "orderSeq":seqno,
                "phone_type":"0",
                "initiator_date":"20200711",
                "inpucd":"985",
                "busisq":calseqno,
                "rsa_key":"77777777777777",
                "inpusq":calseqno,
                "corpno":"985",
                "ip_address":"127.0.0.1",
                "busi_org_id":"025",
                "busiseqno":seqno,
                "terminal_os_type":"0",
                "tranus":"xadmin",
                "initiator_seq":calseqno,
                "pageIndex":"1",
                "pageno":"1",
                "pgsize":"1",
                "callseqno":seqno,
                "channel_id":"MIFI"
            }
        }
        return Requester(headers=header, json=data)

