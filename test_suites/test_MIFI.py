from api.channel.MIFI import MIFI_apply



class TestApply:



    def test_MIFI_apply(self):
        '''小米金融授信申请'''
        app = MIFI_apply()
        res = app.mifi_apply().text()
        assert 'SUCCESS' in res


    def test_MIFI_pay(self):
        '''小米金融提现申请'''
        idnum = '150202199005207674'
        applyid = 'BO2020101400004412'
        app = MIFI_apply()
        res = app.mifi_pay(idnum=idnum, applyId=applyid).text()
        assert 'SUCCESS' in res



    def test_MIFI_apply_query(self):
        '''小米金融授信结果查询'''
        applyNo = 'GU0947930069'
        openId = '678962972'
        app = MIFI_apply()
        res = app.mifi_apply_query(applyNo=applyNo,openId=openId).text()
        assert 'SUCCESS' in res


    def test_MIFI_pay_query(self):
        '''小米金融用信结果查询'''
        paymentno = 'pay1242271777'
        openid = '678962972'
        app = MIFI_apply()
        res = app.mifi_pay_query(paymentNo=paymentno,openId=openid).text()
        assert 'SUCCESS' in res















