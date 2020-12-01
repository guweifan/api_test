import random
from api.identity import IdNumber
from api.Uploadfile import rename,upload,upload_MI
from api.savecustinfo import readExcel,writeExcel
from walnuts import RequestMapping, Method, Requester
from api.randstr import get_name,generate_random_num,get_tel,generate_random_str,get_time




@RequestMapping(path='{app.uat_gateway}',method=Method.POST)
class JDJR_apply:

    @RequestMapping(method=Method.POST)
    def PATSJDSS1001(self):
        '''授信申请'''
        seqno = generate_random_str(17)
        calseqno = "LN" + generate_random_num(12)
        name = get_name()
        mobile = get_tel()
        userid = "user"+generate_random_num(9)
        applyNo = "GU" + generate_random_num(10)
        random_sex = random.randint(1, 2)
        applyTime = get_time()
        idnumber = IdNumber.generate_id(random_sex)

        header = {
            "api_id":"PATSJDSS1001",
            "country":"cn",
            "calseqno":seqno,
            "dapplication":"81001",
            "service":"PATSJDSS1001",
            "callseqno":calseqno,
            "dgroup":"onl01",
            "dversion":"1.0",
            "busiseqno":calseqno,
            "Content-Type":"application/json"
        }
        data = {
            "input":{
                "ocrInfo":{
                    "signPlace":"上海",
                    "address":"上海",
                    "validDate":"20190306_20390306",
                    "sex":"男",
                    "name":name,
                    "ethnicGroups":"汉",
                    "idNumber":idnumber
                },
                "userInfo":{
                    "homeAddressCountry":"黄埔",
                    "workAddressDetail":"滇池路756号",
                    "profession":"PROFESSION_001",
                    "homeAddressDetail":"滇池路135号",
                    "workAddressCity":"上海",
                    "education":"UNDERGRADUATE",
                    "unitName":"上海中银消费",
                    "userTel":mobile,
                    "userId":userid,
                    "certNo":idnumber,
                    "homeAddressProvince":"上海",
                    "homeAddressArea":"黄埔",
                    "school":"北京大学",
                    "homeAddressCity":"上海",
                    "workAddressCountry":"黄埔",
                    "workAddressProvince":"上海",
                    "workAddressArea":"黄埔",
                    "unitTel":"17369777481",
                    "emergList":[
                        {
                            "emergRelation":"PARENT",
                            "emergTel":"15215314777",
                            "emergName":"客户之父"
                        },
                        {
                            "emergRelation":"PARENT",
                            "emergTel":"15810943875",
                            "emergName":"客户之母"
                        }
                    ],
                    "username":name,
                    "monthlyIncome":"LEVEL_5"
                },
                "applyProduct":"zhongyin_001",
                "applyNo":applyNo,
                "notifyUrl":"https://jie.baitiao.com/inv/crpl/loan/checkApplyResult",
                "applyTime":applyTime,
                "applyPeriod":"12",
                "channelCode":"CRPL_ZHONGYIN",
                "applyAmount":"300000"
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
                "channel_id":"JDJR"
            }
        }
        return Requester(headers=header, json=data)