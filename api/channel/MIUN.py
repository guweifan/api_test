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
                "api_id":"ICMSJKTS0102",
                "country":"cn",
                "calseqno":calseqno,
                "dapplication":"81001",
                "service":"ICMSJKTS0102",
                "callseqno":calseqno,
                "dgroup":"onl01",
                "dversion":"1.0",
                "busiseqno":calseqno,
                "Content-Type":"application/json"
            }
        data = {
            "input": {"businessMode": "1", "decReason": "",
                               "extraData": {"birthday": "19930506", "signPlace": "上海市黄浦区滇池路街道办事处",
                                             "career": {"firstName": "国家机关、党群组织、企业、事业单位负责人", "firstCode": "0",
                                                        "secondCode": "04", "secondName": "事业单位负责人"},
                                             "education": "999", "gender": "1", "city": "上海", "nation": "汉",
                                             "industryes": "J", "cardsday": "20190315",
                                             "industry": {"firstName": "金融业", "firstCode": "J", "secondCode": "67",
                                                          "secondName": "资本市场服务"}, "faceScore": "90",
                                             "nataddhomeAddressCity": "上海", "province": "上海", "pbcQuery": "",
                                             "marriage": "-1", "expireDate": "20240315", "issueDate": "20190315",
                                             "enterpriseName": "未知", "monthlyIncome": "5",
                                             "cardData": "/lttsdata/MIUN/20201105/IMG_402071594408083456_20180809102350.tar.gz",
                                             "area": "浦东新区", "profession": "0", "natadd": "上海市黄浦区滇池路81号",
                                             "marrys": "90", "address": "上海市黄浦区滇池路81号", "race": "汉", "unitName": "未知",
                                             "sex": "男", "liveCondition": "未知", "authProtocol": "上海市黄浦区滇池路81号",
                                             "cardeday": "20240315", "incomeLevel": "5", "nataddAddressArea": "浦东新区",
                                             "pbcScore": "{\"guar_cnt\":\"0\",\"cur_loan_rpm_amt\":\"0\",\"consu_cur_ovd_amt\":\"0\",\"car_ovdcnt_6mth\":\"0\",\"busi_account_cnt_12mth\":\"0\",\"ccard_cur_avg_amt\":\"0\",\"ccard_amtl_arp\":\"0\",\"scard_agency_cnt\":\"0\",\"agency_cnt_12mth\":\"0\",\"ccard_ovd_cnt_6mth\":\"0\",\"scard_cur_total_amt\":\"0\",\"acct_age\":\"0\",\"consu_cur_account_cnt\":\"0\",\"consu_cur_ovd_tm\":\"0\",\"busi_ovdcnt_12mth\":\"0\",\"loan_ovdmax_12mth\":\"0\",\"consu_ovdcnt_12mth\":\"0\",\"house_cur_bal\":\"0\",\"ccard_acct_age\":\"0\",\"loan_query_num_1mth\":\"0\",\"car_cur_ovd_tm\":\"0\",\"ccard_rpm_cnt\":\"0\",\"loan_account_cnt\":\"0\",\"ccard_arp_cnt\":\"0\",\"fund_amt\":\"0\",\"query_num_3mth\":\"0\",\"reports_time\":\"20201105\",\"loan_query_num_6mth\":\"0\",\"ovd_maxterm_3mth\":\"0\",\"consu_account_cnt_12mth\":\"0\",\"loan_ovdcnt_12mth\":\"0\",\"ccard_ovd_bal\":\"0\",\"enfore_cnt\":\"0\",\"house_cur_total_amt\":\"0\",\"ccard_disnormal_cnt\":\"0\",\"house_cur_account_cnt\":\"0\",\"avg_hfamt_12mth\":\"0\",\"ccard_ovd_maxamt_12mth\":\"0\",\"cur_loan_ovd_tm\":\"0\",\"ccard_amtc_utl\":\"0\",\"ovd_maxterm_6mth\":\"0\",\"scard_cur_avgbal_6mth\":\"0\",\"scard_cnt_12mth\":\"0\",\"car_cur_bal\":\"0\",\"house_ovdcnt_12mth\":\"0\",\"ccard_cnt_12mth\":\"0\",\"ccard_amtc_aut_p6m\":\"0\",\"scard_total_amt\":\"0\",\"scard_ovd_cnt\":\"0\",\"query_age\":\"0\",\"consu_cur_bal\":\"0\",\"scard_amtl_rpm\":\"0\",\"busi_cur_rpm_amt\":\"0\",\"scard_cnt\":\"0\",\"car_cur_total_amt\":\"0\",\"loan_total_amt\":\"0\",\"consu_ovdcnt_6mth\":\"0\",\"busi_cur_bal\":\"0\",\"ccard_ovd_amt\":\"0\",\"ccard_cnt_6mth\":\"0\",\"query_num_6mth\":\"0\",\"car_cur_account_cnt\":\"0\",\"house_cur_rpm_amt\":\"0\",\"loan_acct_age\":\"0\",\"agency_cnt_6mth\":\"0\",\"ccard_ovd_cnt_12mth\":\"0\",\"ovd_cnt_3mth\":\"0\",\"ccard_ovd_tm\":\"0\",\"car_cur_rpm_amt\":\"0\",\"ovd_cnt_12mth\":\"0\",\"scard_cur_avg_amt\":\"0\",\"guar_lvlmax\":\"0\",\"consu_cur_rpm_amt\":\"0\",\"car_account_cnt_12mth\":\"0\",\"loan_ovdmax\":\"0\",\"query_num_1mth\":\"0\",\"ccard_credit_cnt\":\"0\",\"ccard_query_num_1mth\":\"0\",\"last_query_age\":\"0\",\"ovd_cnt_6mth\":\"0\",\"cur_loan_account_cnt\":\"0\",\"house_ovdcnt_6mth\":\"0\",\"disp_cnt\":\"0\",\"per_query_num_1mth\":\"0\",\"ccard_cur_cnt\":\"0\",\"ccard_amtl_rpm\":\"0\",\"cur_loan_bal\":\"0\",\"loan_ovdcnt_6mth\":\"0\",\"scard_ovd_amt\":\"0\",\"busi_ovdcnt_6mth\":\"0\",\"consu_cur_total_amt\":\"0\",\"scard_od_amt_180up\":\"0\",\"busi_cur_ovd_amt\":\"0\",\"busi_cur_account_cnt\":\"0\",\"ccard_normal_cnt\":\"0\",\"ccard_query_num_6mth\":\"0\",\"loan_ovdmax_6mth\":\"0\",\"loan_query_num_3mth\":\"0\",\"ccard_ovd_cnt\":\"0\",\"car_ovdcnt_12mth\":\"0\",\"ccard_bad_bal\":\"0\",\"cur_loan_total_amt\":\"0\",\"scard_disnormal_cnt\":\"0\",\"ovd_maxterm_12mth\":\"0\",\"cur_loan_ovd_amt\":\"0\",\"ccard_query_num_3mth\":\"0\",\"compen_cnt\":\"0\",\"ccard_cnt\":\"0\",\"per_query_num_6mth\":\"0\",\"busi_cur_total_amt\":\"0\",\"ccard_ovd_maxamt_6mth\":\"0\",\"scard_acct_age\":\"0\",\"car_cur_ovd_amt\":\"0\",\"account_cnt\":\"0\",\"scard_amtl_arp\":\"0\",\"house_cur_ovd_tm\":\"0\",\"house_account_cnt_12mth\":\"0\",\"scard_cur_cnt\":\"0\",\"house_cur_ovd_amt\":\"0\",\"per_query_num_3mth\":\"0\",\"cur_account_cnt\":\"0\",\"ccard_avg_amt\":\"0\",\"consu_account_cnt_6mth\":\"0\",\"scard_max_bal\":\"0\",\"busi_cur_ovd_tm\":\"0\",\"scard_overdraft_cnt\":\"0\",\"scard_normal_cnt\":\"0\"}",
                                             "authority": "上海市黄浦区滇池路街道办事处", "nataddAddressProvince": "上海"},
                               "bankMobile": "15014486030", "loanBefore": "Y", "userTel": "15014486030",
                               "custName": "客户920177667", "userId": "A6386353928", "cardNo": "6216610200016587010",
                               "certNo": "130101199111230127", "applyAmont": "20000", "rateType": "D",
                               "applyProduct": "02050012", "certtp": "101", "dyrate": "0.03", "creditResult": "PAS",
                               "applyNo": "622944023103", "applyTime": "19760527101051", "loanCategory": "0",
                               "channelCode": "MIUN"},
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
    def miun_pay(self):
        '''用信申请'''
        seqno = generate_random_str(7)
        calseqno = "LN" + generate_random_num(12)




        header = {
            "api_id":"ICMSJKTS0103",
            "country":"cn",
            "calseqno":calseqno,
            "dapplication":"81001",
            "service":"ICMSJKTS0103",
            "callseqno":calseqno,
            "dgroup":"onl01",
            "dversion":"1.0",
            "busiseqno":calseqno,
            "Content-Type":"application/json"
        }
        data = {
            "input": {
                "dailyIntRate": "0.002376",
                "userTel": "15014486030",
                "custName": "客户920177667",
                "riskData": {
                    "loaninterestscore": "",
                    "locationscore": "",
                    "travelinterestscore": "",
                    "financeinterestcore": "",
                    "shoppinginterestscore": "",
                    "lifeserviceinterestscore": "",
                    "lthrepaymonthsscore": "",
                    "totalrepaymonthsscore":"",
                    "launchdauscore": "",
                    "socialinterestscore": "",
                    "generalscore": "",
                    "readinginterestscore": "",
                    "gameinterestscore": ""
                },
                "userId": "A6386353928",
                "cardNo": "6216606301234560403",
                "loanAmount": "1000",
                "paymentNo": "768304095060",
                "certNo": "130101199111230133",
                "bankAmount": "10000",
                "certtp": "101",
                "loanPurpose": "20",
                "orderProduct": "02050012",
                "loanPeriod": "12",
                "channelCode": "MIUN"
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

