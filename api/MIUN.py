import random
from api.identity import IdNumber
from api.Uploadfile import rename,upload,upload_MI
from api.savecustinfo import readExcel,writeExcel
from walnuts import RequestMapping, Method, Requester
from api.randstr import get_name,generate_random_num,get_tel,generate_random_str,get_time




@RequestMapping(path='{app.sit_gateway}',method=Method.POST)
class MIUN_apply:


    @RequestMapping(method=Method.POST)
    def miun_apply(self):
        '''小米联合贷授信申请'''
        seqno = generate_random_str(7)
        calseqno = "LN" + generate_random_num(12)
        name = get_name()
        mobile = get_tel()
        userid = generate_random_str(9)
        applyNo = "GU" + generate_random_num(10)
        random_sex = random.randint(1, 2)
        applyTime = get_time()
        idnumber = IdNumber.generate_id(random_sex)

        # """影像件上传"""
        # filename = "IMG_" + applyNo + "_" + applyTime + ".tar.gz"
        # src_file = 'D:\\Python_work\\walnuts_api\\api_test\\resources\\'
        # applyImgPath = "/lttsdata/MIUN/20201105/" + "IMG_" + applyNo + "_" + applyTime + ".tar.gz"
        # src_file = rename(src_file, filename)
        # upload(src_file, applyImgPath)
        # """存储客户信息"""
        # custinfo = [name, mobile, idnumber, applyNo, applyImgPath]
        # writeExcel(sheetname=idnumber, custinfo=custinfo)
        """定义请求header和body"""
        header = {
                "api_id":"PATSMUSS1003",
                "country":"cn",
                "calseqno":calseqno,
                "dapplication":"81001",
                "service":"PATSMUSS1003",
                "callseqno":calseqno,
                "dgroup":"onl01",
                "dversion":"1.0",
                "busiseqno":calseqno,
                "Content-Type":"application/json"
            }
        data = {
        "input":{
            "businessMode":"1",
            "idType":"CNI",
            "serialNum":applyNo,
            "decReason":"",
            "extraData":{
                "birthday":"19930506",
                "signPlace":"上海",
                "industry":
                    {
                        "firstName": "农业",
                        "firstCode": "01",
                        "secondCode": "02",
                        "secondName": "林业"
                    },
                "career":
                    {
                        "firstName":"企业负责人",
                        "firstCode":"05",
                        "secondCode":"04",
                        "secondName":"事业单位负责人"
                    },
                "education":"-1",
                "gender":"",
                "city":"上海",
                "nation":"汉",
                "cardsday":"20190315",
                "faceScore":"80",
                "pbcQuery": "2",
                "pbcScore": {
                    "acct_age": "0",
                    "account_cnt": "0",
                    "cur_account_cnt": "3",
                    "fund_amt": "20.12",
                    "avg_hfamt_12mth": "35.12",
                    "disp_cnt": "2",
                    "compen_cnt": "3",
                    "guar_cnt": "3",
                    "guar_lvlmax": "3",
                    "enfore_cnt": "3",
                    "loan_acct_age": "4",
                    "loan_account_cnt": "5",
                    "loan_total_amt": "50.32",
                    "house_account_cnt_12mth": "4",
                    "car_account_cnt_12mth": "0",
                    "consu_account_cnt_6mth": "0",
                    "consu_account_cnt_12mth": "0",
                    "busi_account_cnt_12mth": "0",
                    "cur_loan_account_cnt": "0",
                    "cur_loan_total_amt": "0",
                    "cur_loan_ovd_tm": "0",
                    "cur_loan_bal": "0",
                    "cur_loan_rpm_am": "0",
                    "cur_loan_ovd_amt": "0",
                    "house_cur_account_cnt": "0",
                    "house_cur_total_amt": "0",
                    "consu_cur_account_cnt": "0",
                    "consu_cur_total_amt": "0",
                    "busi_cur_account_cnt": "0",
                    "busi_cur_total_amt": "0",
                    "car_cur_account_cnt": "0",
                    "car_cur_total_amt": "0",
                    "house_cur_ovd_tm": "0",
                    "house_cur_bal": "0",
                    "house_cur_rpm_amt": "0",
                    "house_cur_ovd_amt": "0",
                    "car_cur_ovd_tm": "0",
                    "car_cur_bal": "0",
                    "car_cur_rpm_amt": "0",
                    "car_cur_ovd_amt": "0",
                    "consu_cur_ovd_tm": "0",
                    "consu_cur_bal": "0",
                    "consu_cur_rpm_amt": "0",
                    "consu_cur_ovd_amt": "0",
                    "busi_cur_ovd_tm": "0",
                    "busi_cur_bal": "0",
                    "busi_cur_rpm_amt": "0",
                    "busi_cur_ovd_amt": "0",
                    "loan_ovdmax": "0",
                    "loan_ovdmax_6mth": "0",
                    "loan_ovdmax_12mth": "0",
                    "loan_ovdcnt_6mth": "0",
                    "loan_ovdcnt_12mth": "0",
                    "house_ovdcnt_6mth": "0",
                    "house_ovdcnt_12mth": "0",
                    "car_ovdcnt_6mth": "0",
                    "car_ovdcnt_12mth": "0",
                    "busi_ovdcnt_6mth": "0",
                    "busi_ovdcnt_12mth": "35",
                    "consu_ovdcnt_6mth": "35",
                    "consu_ovdcnt_12mth": "35",
                    "ccard_acct_age": "35",
                    "ccard_cnt": "35",
                    "ccard_cur_cnt": "35",
                    "ccard_normal_cnt": "35",
                    "ccard_disnormal_cnt": "35",
                    "ccard_credit_cnt": "35",
                    "ccard_cnt_6mth": "35",
                    "ccard_cnt_12mth": "35",
                    "agency_cnt_6mth": "35",
                    "agency_cnt_12mth": "35",
                    "ccard_avg_amt": "35",
                    "ccard_cur_avg_amt": "35",
                    "ccard_ovd_cnt": "35",
                    "ccard_amtl_rpm": "35",
                    "ccard_rpm_cnt": "35",
                    "ccard_amtl_arp": "35",
                    "ccard_arp_cnt": "35",
                    "ccard_amtc_utl": "35",
                    "ccard_ovd_bal": "35",
                    "ccard_amtc_aut_p6m": "35",
                    "ccard_ovd_amt": "35",
                    "ccard_ovd_tm": "35",
                    "ccard_bad_bal": "35",
                    "ccard_ovd_cnt_6mth": "35",
                    "ccard_ovd_cnt_12mth": "35",
                    "ccard_ovd_maxamt_6mth": "35",
                    "ccard_ovd_maxamt_12mth": "35",
                    "scard_acct_age": "35",
                    "scard_cnt": "35",
                    "scard_cur_cnt": "35",
                    "scard_normal_cnt": "35",
                    "scard_disnormal_cnt": "35",
                    "scard_cnt_12mth": "35",
                    "scard_total_amt": "35",
                    "scard_cur_total_amt": "35",
                    "scard_overdraft_cnt": "35",
                    "scard_cur_avg_amt": "35",
                    "scard_max_bal": "35",
                    "scard_od_amt_180up": "35",
                    "scard_amtl_rpm": "35",
                    "scard_amtl_arp": "35",
                    "scard_agency_cnt": "35",
                    "scard_cur_avgbal_6mth": "35",
                    "scard_ovd_cnt": "35",
                    "scard_ovd_amt": "35",
                    "query_num_1mth": "35",
                    "per_query_num_1mth": "35",
                    "loan_query_num_1mth": "35",
                    "ccard_query_num_1mth": "35",
                    "query_num_3mth": "35",
                    "per_query_num_3mth": "35",
                    "loan_query_num_3mth": "35",
                    "ccard_query_num_3mth": "35",
                    "query_num_6mth": "35",
                    "per_query_num_6mth": "35",
                    "loan_query_num_6mth": "35",
                    "ccard_query_num_6mth": "35",
                    "last_query_age": "35",
                    "query_age": "35",
                    "ovd_cnt_3mth": "35",
                    "ovd_cnt_6mth": "35",
                    "ovd_cnt_12mth": "35",
                    "ovd_maxterm_3mth": "35",
                    "ovd_maxterm_6mth": "35",
                    "ovd_maxterm_12mth": "35",
                    "reports_time": "20201012"
                },
                "nataddhomeAddressCity":"上海市",
                "province":"上海",
                "marriage":"-1",
                "expireDate":"20240315",
                "issueDate":"20190315",
                "enterpriseName":"未知",
                "monthlyIncome":"5",
                "cardData":"/lttsdata/MIUN/20201105/IMG_053838476704_202011051448.tar.gz",
                "area":"浦东新区",
                "natadd":"上海市黄浦区滇池路81号",
                "marrys":"-1",
                "address":"上海市黄浦区滇池路81号",
                "race":"汉",
                "unitName":"未知",
                "sex":"",
                "liveCondition":"未知",
                "authProtocol":"",
                "cardeday":"20240315",
                "incomeLevel":"5",
                "nataddAddressArea":"黄浦区",
                "pbcScore":"80",
                "authority":"上海市黄浦区滇池路街道办事处",
                "nataddAddressProvince":"上海市"
            },
            "userSource":"",
            "mobile":mobile,
            "bankMobile":mobile,
            "loanBefore":"Y",
            "userName":name,
            "timeStamp":applyTime,
            "userid":userid,
            "rateType":"D",
            "rate":"300",
            "provider":"ZYBANK",
            "creditResult":"PAS",
            "applyNo":applyNo,
            "bankCardNum":"6216610200016587010",
            "creditAmount":"1000000",
            "idNum":idnumber,
            "loanCategory":"0",
            "channelCode":"MIUN"
        },
        "comm_req":{
            "trantm":"818557",
            "initiator_system":"301",
            "app_version":"1.0",
            "trxn_branch":"79470",
            "call_seq":seqno,
            "trxn_teller":"29502258",
            "sponsor_system":"810",
            "auth_user_id":"062169",
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
            "channel_id":"MIUN"
        }
}
        return Requester(headers=header, json=data)



    @RequestMapping(method=Method.POST)
    def miun_pay(self, idnum, applyId):
        '''用信申请'''
        seqno = generate_random_str(7)
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
                    "loanAmount":"300000",
                    "firstRepayDay":"",
                    "extInfo":{
                        "faceCmpScore":"80",
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
                        "companyName":"棉花糖厂",
                        "applyAuthPath":"",
                        "applyImgPath":applyImgPath,
                        "ocr":{
                            "nameOcr":name,
                            "numberOcr":idnumber,
                            "addressOcr":"上海",
                            "ethnicOcr":"汉",
                            "dueTimeOcr":"20100801_20300801",
                            "sexOcr":"male",
                            "issueOrgOcr":"公安局"
                        },
                        "incomeLevel":"6",
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

