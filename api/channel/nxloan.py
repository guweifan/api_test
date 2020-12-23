from walnuts import RequestMapping, Method, Requester
from api.randstr import generate_random_num,get_tel,generate_random_str,get_time



@RequestMapping(path='{app.sit1_gateway}', method=Method.POST)
class TOUTIAO_nxloan:

    @RequestMapping(method=Method.POST)
    def addcll(self, custac, idtfno, name, phone, ordrid, crdlam, appday):
        """新增额度交易"""
        seqno = generate_random_num(17)
        merchn = "B0000008"
        header ={
            "dserviceId": "CORECLTS1037",
            "api_id": "CORECLTS1037",
            "country": "cn",
            "dapplication": "01001",
            "callseqno": seqno,
            "dgroup": "01",
            "dversion": "1.0",
            "busiseqno": seqno,
            "Content-Type": "application/json"
        }
        data = {
            "input":{
                "prodcd":"1001",
                "magena":"王二",
                "crcycd":"CNY",
                "custac":custac,
                "irflvl":"",
                "exusid":"",
                "intrvl":"",
                "irfltp":"0",
                "idtfno":idtfno,
                "dateam":"",
                "merchn": merchn, #合作商编号
                "exordr":"",
                "cardno":"",
                "idtftp":"101",
                "incftp":"",
                "custna":name,
                "abrtdt":"",
                "phonno":phone,
                "mageno":"34718659",
                "effedt":"20401117",
                "brchno":"",
                "appday": appday,
                "addlst":[
                    {
                        "bapdcd":"02040005",
                        "ordrid":ordrid,
                        "crdlam":crdlam,
                        "busino":"02040005",
                        "cllevl":"P",
                        "crdlno":"",
                        "cltpcd":"02040005"
                    }
                ],
            },
            "comm_req":{
                "xcopfg":"0",
                "inpucd":"985",
                "counts":"0",
                "busisq":seqno,
                "corpno":"985",
                "xdcnfg":"1",
                "tranus":"9852001",
                "servtp":"TE",
                "servno":"004",
                "pageno":"1",
                "pgsize":"10",
                "tranbr":"985000",
                "channel_id":"TOUTIAO"
            }
        }
        return Requester(headers=header, json=data)

    @RequestMapping(method=Method.POST)
    def apoccu(self, crdlno, exordr, ordrid, appday):
        """额度占用"""
        seqno = generate_random_num(17)
        header = {
            "dserviceId": "CORECLTS1045",
            "api_id": "CORECLTS1045",
            "country": "cn",
            "dapplication": "01001",
            "callseqno": seqno,
            "dgroup": "01",
            "dversion": "1.0",
            "busiseqno": seqno,
            "Content-Type": "application/json"
        }
        data = {
            "input": {
                "busisq": ordrid,
                "apocam": "1000",
                "occust": "A",
                "exordr": exordr,
                "crdlno": crdlno,
                "aplydt": appday
            },
            "comm_req": {
                "xcopfg": "0",
                "inpucd": "985",
                "counts": "0",
                "busisq": seqno,
                "corpno": "985",
                "xdcnfg": "1",
                "tranus": "9852001",
                "servtp": "TE",
                "servno": "004",
                "pageno": "1",
                "pgsize": "10",
                "tranbr": "985000",
                "channel_id": "TOUTIAO"
            }
        }
        return Requester(headers=header, json=data)

    @RequestMapping(method=Method.POST)
    def ybloan(self, name, custac, idtfno, ordrid, cntrno, acctno, exordr, appday, chcksq):
        """预放款"""
        seqno = generate_random_num(17)
        merchn = "B0000008"
        header = {
            "dserviceId": "CORELNTS1904",
            "api_id": "CORELNTS1904",
            "country": "cn",
            "dapplication": "01001",
            "callseqno": seqno,
            "dgroup": "01",
            "dversion": "1.0",
            "busiseqno": seqno,
            "Content-Type": "application/json"
        }
        data = {
            "input":{
                "rpacno": acctno,
                "irrvtp":"0",
                "acctbr":"076060301",
                "guarty":"4",
                "irflvl":"",
                "exusid":"",
                "chckdt": appday,
                "merchn": merchn,
                "exordr": exordr,
                "cgacno":"",
                "repyfm":"1MAD",
                "repyls":[

                ],
                "trgtbr":"",
                "ordrid": ordrid,
                "loandt": appday,
                "trgtfn":"",
                "pychnl":"E01",
                "irrvfm":"",
                "tocgrt":"",
                "irdyfg":"Y",
                "cntrno": cntrno,
                "acctna": name,
                "prodcd":"02040005",
                "period":"6M",
                "lnacno": acctno,
                "lnrtir":"27.375",
                "custac": custac,
                "crcycd":"CNY",
                "trgtac":"",
                "matudt":"",
                "schdtp":"3",
                "idtfno": idtfno,
                "corpno":"985",
                "idtftp":"101",
                "cardno": acctno,
                "incftp":"2",
                "tranam":"1000",
                "intrcd":"",
                "sprdid":"02040005",
                "trgtna":"",
                "chcksq": chcksq,
                "bkintr":"",
                "grprdy":"5"
            },
            "comm_req": {
                "xcopfg": "0",
                "inpucd": "985",
                "counts": "0",
                "busisq": seqno,
                "corpno": "985",
                "xdcnfg": "1",
                "tranus": "9852001",
                "servtp": "TE",
                "servno": "004",
                "pageno": "1",
                "pgsize": "10",
                "tranbr": "985000",
                "channel_id": "TOUTIAO"
            }
        }
        return Requester(headers=header, json=data)

    @RequestMapping(method=Method.POST)
    def nxloan(self, name, custac, idtfno, ordrid, cntrno, acctno, appday, chcksq):
        """放款"""
        seqno = generate_random_num(17)
        header = {
            "dserviceId": "CORELNTS1903",
            "api_id": "CORELNTS1903",
            "country": "cn",
            "dapplication": "01001",
            "callseqno": seqno,
            "dgroup": "01",
            "dversion": "1.0",
            "busiseqno": seqno,
            "Content-Type": "application/json"
        }
        data = {
            "input": {
                "rpacno": acctno,
                "irrvtp": "0",
                "acctbr": "076060301",
                "guarty": "4",
                "irflvl": "",
                "exusid": "",
                "chckdt": appday,
                "frstmd": "1",
                "cgacno": "",
                "repyfm": "1MAD",
                "repyls": [

                ],
                "trgtbr": "",
                "ordrid": ordrid,
                "loandt": appday,
                "trgtfn": "",
                "pychnl": "E01",
                "loanus": "",
                "irrvfm": "",
                "tocgrt": "",
                "irdyfg": "Y",
                "cntrno": cntrno,
                "sprdna": "头条钱包",
                "acctna": name,
                "prodcd": "02040005",
                "period": "12M",
                "lnacno": acctno,
                "lnrtir": "18",
                "custac": custac,
                "crcycd": "CNY",
                "trgtac": "",
                "matudt": "",
                "schdtp": "3",
                "idtfno": idtfno,
                "corpno": "985",
                "idtftp": "101",
                "cardno": acctno,
                "incftp": "2",
                "tranam": "1000",
                "intrcd": "",
                "sprdid": "02040005",
                "trgtna": "",
                "chcksq": chcksq,
                "bkintr": "",
                "grprdy": "5"
            },
            "comm_req": {
                "xcopfg": "0",
                "inpucd": "985",
                "counts": "0",
                "busisq": seqno,
                "corpno": "985",
                "xdcnfg": "1",
                "tranus": "9852001",
                "servtp": "TE",
                "servno": "004",
                "pageno": "1",
                "pgsize": "10",
                "tranbr": "985000",
                "channel_id": "TOUTIAO"
            }
        }
        return Requester(headers=header, json=data)



@RequestMapping(path='{app.sit3_gateway}', method=Method.POST)
class JDJR_nxloan:

    @RequestMapping(method=Method.POST)
    def addcll(self, custac, idtfno, name, phone, ordrid, crdlam, appday):
        """新增额度交易"""
        seqno = generate_random_num(17)
        merchn = "B0000008"
        header ={
            "dserviceId": "CORECLTS1037",
            "api_id": "CORECLTS1037",
            "country": "cn",
            "dapplication": "01001",
            "callseqno": seqno,
            "dgroup": "01",
            "dversion": "1.0",
            "busiseqno": seqno,
            "Content-Type": "application/json"
        }
        data = {
            "input":{
                "prodcd":"1001",
                "magena":"王二",
                "crcycd":"CNY",
                "custac":custac,
                "irflvl":"",
                "exusid":"",
                "intrvl":"",
                "irfltp":"0",
                "idtfno":idtfno,
                "dateam":"",
                "merchn": merchn, #合作商编号
                "exordr":"",
                "cardno":"",
                "idtftp":"101",
                "incftp":"",
                "custna":name,
                "abrtdt":"",
                "phonno":phone,
                "mageno":"34718659",
                "effedt":"20401117",
                "brchno":"",
                "appday": appday,
                "addlst":[
                    {
                        "bapdcd":"0204",
                        "ordrid":ordrid,
                        "crdlam":crdlam,
                        "busino":"0204",
                        "cllevl":"P",
                        "crdlno":"",
                        "cltpcd":"02040014"
                    }
                ],
            },
            "comm_req":{
                "xcopfg":"0",
                "inpucd":"985",
                "counts":"0",
                "busisq":seqno,
                "corpno":"985",
                "xdcnfg":"1",
                "tranus":"9852001",
                "servtp":"TE",
                "servno":"004",
                "pageno":"1",
                "pgsize":"10",
                "tranbr":"985000",
                "channel_id":"JDJR"
            }
        }
        return Requester(headers=header, json=data)

    @RequestMapping(method=Method.POST)
    def apoccu(self, crdlno, exordr, ordrid, appday):
        """额度占用"""
        seqno = generate_random_num(17)
        header = {
            "dserviceId": "CORECLTS1045",
            "api_id": "CORECLTS1045",
            "country": "cn",
            "dapplication": "01001",
            "callseqno": seqno,
            "dgroup": "01",
            "dversion": "1.0",
            "busiseqno": seqno,
            "Content-Type": "application/json"
        }
        data = {
            "input": {
                "busisq": ordrid,
                "apocam": "1000",
                "occust": "A",
                "exordr": exordr,
                "crdlno": crdlno,
                "aplydt": appday
            },
            "comm_req": {
                "xcopfg": "0",
                "inpucd": "985",
                "counts": "0",
                "busisq": seqno,
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
    def ybloan(self, name, custac, idtfno, ordrid, cntrno, acctno, exordr, appday, chcksq):
        """预放款"""
        seqno = generate_random_num(17)
        merchn = "B0000008"
        header = {
            "dserviceId": "CORELNTS1904",
            "api_id": "CORELNTS1904",
            "country": "cn",
            "dapplication": "01001",
            "callseqno": seqno,
            "dgroup": "01",
            "dversion": "1.0",
            "busiseqno": seqno,
            "Content-Type": "application/json"
        }
        data = {
            "input":{
                "rpacno": acctno,
                "irrvtp":"0",
                "acctbr":"076060301",
                "guarty":"4",
                "irflvl":"",
                "exusid":"",
                "chckdt": appday,
                "merchn": merchn,
                "exordr": exordr,
                "cgacno":"",
                "repyfm":"1MAD",
                "repyls":[

                ],
                "trgtbr":"",
                "ordrid": ordrid,
                "loandt": appday,
                "trgtfn":"",
                "pychnl":"JDJR",
                "irrvfm":"",
                "tocgrt":"",
                "irdyfg":"Y",
                "cntrno": cntrno,
                "acctna": name,
                "prodcd":"0204",
                "period":"6M",
                "lnacno": acctno,
                "lnrtir":"27.375",
                "custac": custac,
                "crcycd":"CNY",
                "trgtac":"",
                "matudt":"",
                "schdtp":"3",
                "idtfno": idtfno,
                "corpno":"985",
                "idtftp":"101",
                "cardno": acctno,
                "incftp":"2",
                "tranam":"1000",
                "intrcd":"",
                "sprdid":"0204",
                "trgtna":"",
                "chcksq": chcksq,
                "bkintr":"",
                "grprdy":"5"
            },
            "comm_req": {
                "xcopfg": "0",
                "inpucd": "985",
                "counts": "0",
                "busisq": seqno,
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
    def nxloan(self, name, custac, idtfno, ordrid, cntrno, acctno, appday, chcksq):
        """放款"""
        seqno = generate_random_num(17)
        header = {
            "dserviceId": "CORELNTS1903",
            "api_id": "CORELNTS1903",
            "country": "cn",
            "dapplication": "01001",
            "callseqno": seqno,
            "dgroup": "01",
            "dversion": "1.0",
            "busiseqno": seqno,
            "Content-Type": "application/json"
        }
        data = {
            "input": {
                "rpacno": acctno,
                "irrvtp": "0",
                "acctbr": "076060301",
                "guarty": "4",
                "irflvl": "",
                "exusid": "",
                "chckdt": appday,
                "frstmd": "1",
                "cgacno": "",
                "repyfm": "1MAD",
                "repyls": [

                ],
                "trgtbr": "",
                "ordrid": ordrid,
                "loandt": appday,
                "trgtfn": "",
                "pychnl": "JDJR",
                "loanus": "",
                "irrvfm": "",
                "tocgrt": "",
                "irdyfg": "Y",
                "cntrno": cntrno,
                "sprdna": "微贷款",
                "acctna": name,
                "prodcd": "0204",
                "period": "12M",
                "lnacno": acctno,
                "lnrtir": "27.375",
                "custac": custac,
                "crcycd": "CNY",
                "trgtac": "",
                "matudt": "",
                "schdtp": "3",
                "idtfno": idtfno,
                "corpno": "985",
                "idtftp": "101",
                "cardno": acctno,
                "incftp": "2",
                "tranam": "1000",
                "intrcd": "",
                "sprdid": "0204",
                "trgtna": "",
                "chcksq": chcksq,
                "bkintr": "",
                "grprdy": "5"
            },
            "comm_req": {
                "xcopfg": "0",
                "inpucd": "985",
                "counts": "0",
                "busisq": seqno,
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