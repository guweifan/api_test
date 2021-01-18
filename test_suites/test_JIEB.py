from api.channel.JieBei import JieBei_apply, ICMSLNTS0001,PATSJBSS1002
from api.SQL import get_applid, get_requestid


class TestApply:



    def test_jiebei_apply(self):
        '''蚂蚁借呗授信申请'''
        app = JieBei_apply()
        res = app.PATSJBSS1001().json()
        assert res["sys"]['erortx'] == "SUCCESS"


    def test_ICMSJKSS0002(self):
        '''影像件上传'''
        applyNo = '208084027184396882A'
        applyid = get_applid(applyno=applyNo)
        app = JieBei_apply()
        res = app.ICMSJKSS0002(applyNo=applyNo, applid=applyid).json()
        assert res["sys"]['erortx'] == "SUCCESS"


    def test_ICMSLNTS0001(self):
        '''富士通回调'''
        APPLID = "BO2020112400000773"
        requestid = get_requestid(APPLID)
        app = ICMSLNTS0001()
        res = app.ICMSLNTS0001(requestid).json()
        assert res["sys"]['erortx'] == "SUCCESS"

    def test_PATSJBSS1002(self):
        '''授信结果回调'''
        creditRate = ""
        checkStatus = "FAILURE"
        app = PATSJBSS1002()
        res = app.ADMIT_APPLY(creditRate=creditRate, checkStatus=checkStatus).json()
        assert res["sys"]['erortx'] == "SUCCESS"
