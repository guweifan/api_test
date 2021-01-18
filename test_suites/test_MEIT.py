from api.channel.MEIT import MEIT


class TestMeit:


    def test_PATSMTSS1001(self):
        '''美团授信申请'''
        app = MEIT()
        res = app.PATSMTSS1001().json()
        assert res["sys"]['erortx'] == "SUCCESS"


    def test_PATSMTSS1002(self):
        """授信结果查询"""
        app = MEIT()
        res = app.PATSMTSS1002().json()
        assert res["sys"]['erortx'] == "SUCCESS"


    def test_PATSMTSS2001(self):
        """借款申请"""
        app = MEIT()
        res = app.PATSMTSS2001().json()
        assert res["sys"]['erortx'] == "SUCCESS"