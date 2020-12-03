from api.demo import CreditApply



class TestcreditApply:


    def test_apply(self):
        '''招联授信申请'''
        app = CreditApply()
        res = app.creditApply()
        assert 'SUCCESS' in res
        # return res