import random
from api.identity import IdNumber
from walnuts import RequestMapping, Method, Requester
from api.randstr import get_name,generate_random_num,get_tel,generate_random_str,get_card_id



@RequestMapping(path='{app.dev_gateway}',method=Method.POST)
class IUMS:

    @RequestMapping(method=Method.POST)
    def IUMSCUTS0010(self):
        """IUMSCUTS0010 绑卡签约信息登记"""
        seqno = generate_random_str(17)
        calseqno = "LN" + generate_random_num(12)
        custna = get_name()
        random_sex = random.randint(1, 2)
        certno = IdNumber.generate_id(random_sex)
        cardno = get_card_id()
        tel = get_tel()

        header = {
            "api_id": "IUMSCUTS0010",
            "country": "cn",
            "calseqno": seqno,
            "dapplication": "81001",
            "service": "IUMSCUTS0010",
            "callseqno": calseqno,
            "dgroup": "onl01",
            "dversion": "1.0",
            "busiseqno": calseqno,
            "Content-Type": "application/json"
        }
        data = {
            "input":{
                "custna":custna,
                "certtp": "101",
                "certno": certno,
                "channalId": "JDJR",
                "out_user_id": "",
                "cardNo": cardno,
                "cardBin": "621661",
                "cardType": "0",
                "bankNo": "01040000",
                "bankName": "中国银行",
                "registe_type": "1",
                "bankProvince": "天津",
                "bankCity": "天津市",
                "mobileNo": tel,
                "bindCardId": calseqno,
            },
        "comm_req":{
            "xcopfg": "0",
            "inpucd": "985",
            "counts": "0",
            "busisq": calseqno,
            "corpno": "985",
            "xdcnfg": "1",
            "tranus": "9852001",
            "servtp": "TE",
            "servno": "004",
            "pageno": "1",
            "pgsize": "10",
            "tranbr": "985000",
            "channel_id": "JDJR"
            }
        }
        return Requester(headers=header, json=data)

    @RequestMapping(method=Method.POST)
    def IUMSCUTS0010_2(self,custna,certno,cardno):
        """IUMSCUTS0010 绑卡解约信息登记"""
        seqno = generate_random_str(17)
        calseqno = "LN" + generate_random_num(12)
        tel = get_tel()

        header = {
            "api_id": "IUMSCUTS0010",
            "country": "cn",
            "calseqno": seqno,
            "dapplication": "81001",
            "service": "IUMSCUTS0010",
            "callseqno": calseqno,
            "dgroup": "onl01",
            "dversion": "1.0",
            "busiseqno": calseqno,
            "Content-Type": "application/json"
        }
        data = {
            "input": {
                "custna": custna,
                "certtp": "101",
                "certno": certno,
                "channalId": "JDJR",
                "out_user_id": "",
                "cardNo": cardno,
                "cardBin": "621661",
                "cardType": "0",
                "bankNo": "01040000",
                "bankName": "中国银行",
                "registe_type": "2",
                "bankProvince": "天津",
                "bankCity": "天津市",
                "mobileNo": tel,
                "bindCardId": "010",
            },
            "comm_req": {
                "xcopfg": "0",
                "inpucd": "985",
                "counts": "0",
                "busisq": calseqno,
                "corpno": "985",
                "xdcnfg": "1",
                "tranus": "9852001",
                "servtp": "TE",
                "servno": "004",
                "pageno": "1",
                "pgsize": "10",
                "tranbr": "985000",
                "channel_id": "JDJR"
            }
        }
        return Requester(headers=header, json=data)


    @RequestMapping(method=Method.POST)
    def IUMSCUTS0011(self,cardno):
        """IUMSCUTS0011 卡信息查询"""
        seqno = generate_random_str(17)
        calseqno = "LN" + generate_random_num(12)


        header = {
            "api_id": "IUMSCUTS0011",
            "country": "cn",
            "calseqno": seqno,
            "dapplication": "81001",
            "service": "IUMSCUTS0011",
            "callseqno": calseqno,
            "dgroup": "onl01",
            "dversion": "1.0",
            "busiseqno": calseqno,
            "Content-Type": "application/json"
        }
        data = {
            "input": {
                "cardNo": cardno,
                "channalId": "JDJR",
            },
            "comm_req": {
                "xcopfg": "0",
                "inpucd": "985",
                "counts": "0",
                "busisq": calseqno,
                "corpno": "985",
                "xdcnfg": "1",
                "tranus": "9852001",
                "servtp": "TE",
                "servno": "004",
                "pageno": "1",
                "pgsize": "10",
                "tranbr": "985000",
                "channel_id": "JDJR"
            }
        }
        return Requester(headers=header, json=data)



    @RequestMapping(method=Method.POST)
    def IUMSCUTS0009(self, custid, certno):
        """IUMSCUTS0009 卡信息查询"""
        seqno = generate_random_str(17)
        calseqno = "LN" + generate_random_num(12)

        header = {
            "api_id": "IUMSCUTS0009",
            "country": "cn",
            "calseqno": seqno,
            "dapplication": "81001",
            "service": "IUMSCUTS0009",
            "callseqno": calseqno,
            "dgroup": "onl01",
            "dversion": "1.0",
            "busiseqno": calseqno,
            "Content-Type": "application/json"
        }
        data = {
            "input": {
                "custid": custid,
                "certtp": "101",
                "certno": certno,
                "out_user_id": "",
                "channalId": "JDJR",
            },
            "comm_req": {
                "xcopfg": "0",
                "inpucd": "985",
                "counts": "0",
                "busisq": calseqno,
                "corpno": "985",
                "xdcnfg": "1",
                "tranus": "9852001",
                "servtp": "TE",
                "servno": "004",
                "pageno": "1",
                "pgsize": "10",
                "tranbr": "985000",
                "channel_id": "JDJR"
            }
        }
        return Requester(headers=header, json=data)