from api.channel.MUCF import CreditApply, Query_mingwen



class TestcreditApply:


    def test_apply(self):
        '''招联授信申请'''
        app = CreditApply()
        res = app.creditApply().json()
        # assert res["sys"]['erortx'] == "SUCCESS"  # 断言



    def test_query(self):
        app = Query_mingwen()
        applyNo = "test202011100000000001"
        res = app.queryApply(applyNo=applyNo).text()