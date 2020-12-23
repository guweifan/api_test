import random
from api.identity import IdNumber
from api.Uploadfile import upload,exec_commands
from walnuts import RequestMapping, Method, Requester
from api.randstr import get_name,generate_random_num,get_tel,generate_random_str,get_time




@RequestMapping(path='{app.sit1_gateway}',method=Method.POST)
class JDJR_apply:

    @RequestMapping(method=Method.POST)
    def PATSJDSS1001(self,):
        '''授信申请'''
        seqno = generate_random_str(17)
        calseqno = "LN" + generate_random_num(12)
        name = get_name()
        mobile = get_tel()
        userid = "user"+generate_random_num(9)
        applyNo = "J" + generate_random_num(10)
        random_sex = random.randint(1, 2)
        idnumber = IdNumber.generate_id(random_sex)

        """影像件上传"""
        cmd_mk = "mkdir " + userid
        cmd_cp = "cp -r " + userid + " /upload/crpl_zhongyin/20200917/ocr"
        cmd_rm = "rm -rf " + userid
        exec_commands(cmd_mk)
        exec_commands(cmd_cp)
        exec_commands(cmd_rm)
        upload("D:\\Python_work\\walnuts_api\\api_test\\img\\1.txt",
               "/upload/crpl_zhongyin/20200917/ocr/" + userid + "/1.txt")
        upload("D:\\Python_work\\walnuts_api\\api_test\\img\\2.txt",
               "/upload/crpl_zhongyin/20200917/ocr/" + userid + "/2.txt")
        upload("D:\\Python_work\\walnuts_api\\api_test\\img\\3.txt",
               "/upload/crpl_zhongyin/20200917/ocr/" + userid + "/3.txt")

        """报文头信息"""
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
                "applyTime":"20200917",
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

    @RequestMapping(method=Method.POST)
    def PATSJDSS1004(self):
        '''实时额度查询'''
        seqno = generate_random_str(17)
        calseqno = "LN" + generate_random_num(12)

        header = {
            "api_id": "PATSJDSS1004",
            "country": "cn",
            "calseqno": seqno,
            "dapplication": "81001",
            "service": "PATSJDSS1004",
            "callseqno": calseqno,
            "dgroup": "onl01",
            "dversion": "1.0",
            "busiseqno": calseqno,
            "Content-Type": "application/json"
        }
        data = {
            "input": {
                "applyNo": "1201209348270621",
                "userId":"9a3b9fb0ab704e8d83a5c1b5521377de",
                "username":"公西觎",
                "certNo":"210422198001252943",
                "userTel": "18885752217",
                "applyTime": "20201209150307",
                "channelCode": "CRPL_ZHONGYIN",
                "applyProduct": "zhongyin_001",
            },
            "comm_req": {
                "trantm": "844568",
                "initiator_system": "301",
                "app_version": "1.0",
                "trxn_branch": "06924",
                "call_seq": seqno,
                "trxn_teller": "07988122",
                "sponsor_system": "810",
                "auth_user_id": "153148",
                "servtp": "TE",
                "sys_version": "1.0",
                "inpudt": "20200604",
                "servno": "004",
                "busi_seq": seqno,
                "page_start": "1",
                "trxn_seq": seqno,
                "tranbr": "985000",
                "trandt": "20200604",
                "longitude": "31.2579921",
                "page_size": "10",
                "orderSeq": seqno,
                "phone_type": "0",
                "initiator_date": "20200711",
                "inpucd": "985",
                "busisq": calseqno,
                "rsa_key": "77777777777777",
                "inpusq": seqno,
                "corpno": "985",
                "ip_address": "127.0.0.1",
                "busi_org_id": "025",
                "busiseqno": seqno,
                "terminal_os_type": "0",
                "tranus": "xadmin",
                "initiator_seq": seqno,
                "pageIndex": "1",
                "pageno": "1",
                "pgsize": "1",
                "callseqno": seqno,
                "channel_id": "JDJR"
            }
        }
        return Requester(headers=header, json=data)