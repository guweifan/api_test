from api.channel.LXIN import LXIN


class TestLxin:



    def test_PATSCMSS5005(self):
        '''乐信授信申请'''
        app = LXIN()
        res = app.PATSCMSS5005().text()
        assert 'SUCCESS' in res