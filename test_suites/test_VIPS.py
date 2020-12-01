from api.channel.VIPS import openAccount



class TestcreditApply:


    def test_pay(self):
        '''唯品会借款申请'''
        app = openAccount()
        res = app.creditApply()
        # assert 'SUCCESS' in res