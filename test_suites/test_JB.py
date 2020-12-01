from api.channel.JieBei import JieBei_apply,ICMSLNTS0001
from api.SQL import get_applid,get_requestid


class TestApply:



    def test_jiebei_apply(self):
        '''蚂蚁借呗授信申请'''
        app = JieBei_apply()
        res = app.PATSJBSS1001().text()
        assert 'SUCCESS' in res


    def test_ICMSJKSS0002(self):
        '''影像件上传'''
        applyNo = '886060681031781764A'
        applyid = get_applid(applyno=applyNo)
        app = JieBei_apply()
        res = app.ICMSJKSS0002(applyNo=applyNo, applid=applyid).text()
        assert 'SUCCESS' in res


    def test_ICMSLNTS0001(self):
        '''富士通回调'''
        APPLID = "BO2020112400000479"
        requestid = get_requestid(APPLID)
        app = ICMSLNTS0001()
        res = app.ICMSLNTS0001(requestid).text()
        assert 'SUCCESS' in res
