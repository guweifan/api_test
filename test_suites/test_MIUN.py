from api.channel.MIUN import MIUN_apply



class TestApply:



    def test_MIUN_apply(self):
        '''小米联合贷授信申请'''
        app = MIUN_apply()
        res = app.miun_apply().text()
        # assert 'SUCCESS' in res



    def test_MIUN_apply(self):
        '''小米联合贷授信申请'''
        app = MIUN_apply()
        res = app.miun_pay().text()
        # assert 'SUCCESS' in res


















