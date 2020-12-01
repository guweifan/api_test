import random
from api.identity import IdNumber
from walnuts import RequestMapping, Method, Requester
from api.randstr import get_name,generate_random_num,get_tel,generate_random_str,get_time




@RequestMapping(path='{app.sit3_gateway}',method=Method.POST)
class JieBei_apply:

    @RequestMapping(method=Method.POST)
    def PATSJBSS1001(self):
        '''授信申请'''
        seqno = generate_random_str(17)
        calseqno = "LN" + generate_random_num(12)
        name = get_name()
        mobile = get_tel()
        applyNo = generate_random_num(18) +"A"
        creditNo = applyNo
        random_sex = random.randint(1, 2)
        applyTime = get_time()
        idnumber = IdNumber.generate_id(random_sex)

        header = {
            "api_id":"PATSJBSS1001",
            "country":"cn",
            "calseqno":seqno,
            "dapplication":"81001",
            "service":"PATSJBSS1001",
            "callseqno":calseqno,
            "dgroup":"onl01",
            "dversion":"1.0",
            "busiseqno":calseqno,
            "Content-Type":"application/json"
        }
        data = {
            "input":{
                "applyNo":applyNo,
                "creditNo":creditNo,
                "productCode":"JB",
                "bizMode":"PLATFORM_1",
                "bizType":"ADMIT_APPLY",
                "source":"USER",
                "creditFlag":"N",
                "repayMode":"1",
                "pricingRating":"7",
                "consumingScore":"100.0",
                "name":name,
                "mobileNo":mobile,
                "certType":"01",
                "certNo":idnumber,
                "certValidEndDate":"长期",
                "cardNo":"6225880118085993",
                "applyExpiredDate":"2020-12-31",
                "addr":{
                    "prov": "浙江省",
                    "city": "杭州市",
                    "area": "⻄湖区",
                    "address": "5a2m6Zmi6LevMTI45Y+3LUEx5bqnMTLivKnpgq7lsYA="
                },
                "riskInfo":{
                    "joinRisk":1,
                    "riskRating":"A",
                    "solvencyRatings":"B",
                    "apolloInfo":{"have_car_prob_grade":"02","have_fang_prob_grade":"01","xfdc_index":"07","mobile_fixed_grade":"08",
                    "adr_stability_grade":"09","occupation":"军人","tot_pay_amt_6m_grade":"08","last_6m_avg_asset_total_grade":"06",
                    "ovd_order_cnt_6m_grade": "01","ovd_order_amt_6m_grade": "01","positive_biz_cnt_1y_grade": "10","risk_score": "980",
                    "cust_seg":"A","dev_stability_grade":"A","ovd_order_days_6m_grade":"01","first_loan_length_grade":"05","repay_amt_6m_grade":"07"
                    },
                },
                "extInfo":{
                    "securityId": "cadfasdf-fasdfasdf-fapsdfiprteuensd-34"
                    },
            },
            "comm_req":{
                "trantm":"844568",
                "initiator_system":"301",
                "app_version":"1.0",
                "trxn_branch":"06924",
                "call_seq":seqno,
                "trxn_teller":"07988122",
                "sponsor_system":"810",
                "auth_user_id":"153148",
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
                "busisq":calseqno,
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
                "channel_id":"JIEB"
            },
        }

        return Requester(headers=header, json=data)


    @RequestMapping(method=Method.POST)
    def ICMSJKSS0002(self,applyNo,applid):
        '''进件中心发起影像件'''
        calseqno = "LN" + generate_random_num(12)

        header = {
            "dserviceId":"ICMSJKSS0002",
            "api_id":"ICMSJKSS0002",
            "country":"cn",
            "dapplication":"01001",
            "callseqno":calseqno,
            "dgroup":"01",
            "dversion":"1.0",
            "busiseqno":calseqno,
            "Content-Type":"application/json"
        }
        data ={
            "input":{
                "applid":applid,
                "applyNo":applyNo,
                "tarFilePath":"",
                "downStatus":"",
                "tarFileNa":"",
                "fileList":[
                ]
            },
            "comm_req":{
                "servtp":"TE",
                "xcopfg":"0",
                "inpucd":"985",
                "servno":"004",
                "pageno":"1",
                "counts":"0",
                "busisq":calseqno,
                "pgsize":"10",
                "corpno":"985",
                "tranbr":"985000",
                "xdcnfg":"1",
                "tranus":"9852001"
            }
        }

        return Requester(headers=header, json=data)



@RequestMapping(path="http://10.182.211.179:9009/gateway/ICMSLNTS0001", method=Method.POST)
class ICMSLNTS0001:

    @RequestMapping(method=Method.POST)
    def ICMSLNTS0001(self,reqid):
        calseqno = generate_random_num(12)
        seqno = get_time()
        '''富士通回调'''
        header = {
            "Content-Type":"application/json;charset=UTF-8",
            "callseqno":calseqno,
            "consumercallseqno":calseqno,
            "busiseqno":calseqno,
            "Accept":"application/json;charset=UTF-8",
        }

        data = {
                "input":{
                "is_cust_tel_flag":"1",
                "req_id":reqid,
                "survey_records":[
                    {
                        "answer_text":"模拟结果",
                        "consistency":"0",
                        "survey_id":"JB0101"
                    },
                    {
                        "answer_text":"模拟结果",
                        "consistency":"0",
                        "survey_id":"JB0102"
                    },
                    {
                        "answer_text":"模拟结果",
                        "consistency":"0",
                        "survey_id":"JB0103"
                    },
                    {
                        "answer_text":"模拟结果",
                        "consistency":"0",
                        "survey_id":"JB0104"
                    },
                    {
                        "answer_text":"模拟结果",
                        "consistency":"0",
                        "survey_id":"JB0105"
                    },
                    {
                        "answer_text":"模拟结果",
                        "consistency":"0",
                        "survey_id":"JB0106"
                    },
                    {
                        "answer_text":"模拟结果",
                        "consistency":"0",
                        "survey_id":"JB0107"
                    }
                ],
                "tel_group":"2"
            },
            "sys":{
                "prcscd":"FASTReceiveTelverf",
                "servicecode":"FASTReceiveTelverf"
            },
            "comm_req":{
                "trantm":"094009",
                "authpw":"",
                "smryds":"",
                "initiator_system":"810",
                "trxn_branch":"42839",
                "rviast":"",
                "counts":"0",
                "trxn_teller":"000",
                "authtp":"",
                "trxn_code":"PO.POJD101",
                "consumercallseqno":seqno,
                "scenid":"",
                "servtp":"TE",
                "sms_send_info":[

                ],
                "inpudt":"20200711",
                "busi_seq":seqno,
                "page_start":"1",
                "computer_date":"20200824",
                "auto_chrg_info":{

                },
                "trxn_seq":seqno,
                "devitp":"",
                "trandt":"20200825",
                "page_size":"1",
                "authlv":"",
                "computer_time":"09:40:09 175",
                "spcapi":"",
                "initiator_date":"20200711",
                "custac":"",
                "encrypted_info":[

                ],
                "inpucd":"985",
                "custom_fields":[

                ],
                "inpusq":seqno,
                "corpno":"985",
                "gl_entries":[

                ],
                "authsq":"",
                "aubrlv":"",
                "trxn_desc":"TODO",
                "transq":seqno,
                "smrycd":"",
                "main_trxn_seq":seqno,
                "favalu":"",
                "passwd":"",
                "pageno":"1",
                "channel_id":"JIEB",
                "device":"",
                "warning_info":[

                ],
                "call_out_seq":seqno,
                "smsvrf":"",
                "routtp":"",
                "authfg":"",
                "sponsor_system":"810",
                "trxn_date":"20200824",
                "sub_system_id":"81001",
                "auth_user_id":"091743",
                "sessid":"",
                "aptrtp":"",
                "auth_reason":[

                ],
                "routky":"",
                "finance_info":{

                },
                "servno":"004",
                "authbr":"",
                "zonetp":"",
                "pagesize":"1",
                "tranbr":"985000",
                "cletid":"",
                "retrtm":"",
                "busisq":seqno,
                "authif":"",
                "ip_address":"127.0.0.1",
                "busi_org_id":"985",
                "authus":"",
                "fatype":"",
                "tranus":"xadmin",
                "terminal_os_type":"0",
                "workflowInfo":{

                },
                "consumersysid":"",
                "surefg":"",
                "pgsize":"",
                "spared":""
            }
        }

        return Requester(headers=header, json=data)