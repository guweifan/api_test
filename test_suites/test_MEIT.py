from api.channel.MEIT import MEIT


class TestLxin:



    def test_PATSMTSS1001(self):
        '''美团授信申请'''
        app = MEIT()
        res = app.PATSMTSS1001().json()
        assert 'SUCCESS' in res
        # assert res["sys"]['erortx'] == "SUCCESS"