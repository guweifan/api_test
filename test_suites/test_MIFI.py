from api.MIFI import MIFI_apply



class TestApply:



    def test_MIFI_apply(self):
        '''小米金融授信申请'''
        app = MIFI_apply()
        res = app.mifi_apply().text()
        assert 'SUCCESS' in res


    def test_MIFI_pay(self):
        '''小米金融提现申请'''
        idnum = ''
        applyid = ''
        app = MIFI_apply()
        res = app.mifi_pay(idnum=idnum, applyId=applyid).text()
        assert 'SUCCESS' in res



    def test_MIFI_apply_query(self):
        '''小米金融授信结果查询'''
        applyNo = '4145860261'
        openId = '669411884'
        app = MIFI_apply()
        res = app.mifi_apply_query(applyNo=applyNo,openId=openId).text()
        assert 'SUCCESS' in res


    def test_MIFI_pay_query(self):
        '''小米金融用信结果查询'''
        paymentno = ''
        openid = ''
        app = MIFI_apply()
        res = app.mifi_pay_query(paymentNo=paymentno,openId=openid).text()
        assert 'SUCCESS' in res















