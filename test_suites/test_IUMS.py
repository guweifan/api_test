from api.channel.IUMS import IUMS



class TestApply:


    def test_IUMSCUTS0010(self):
        '''绑卡签约信息登记'''
        app = IUMS()
        res = app.IUMSCUTS0010().text()
        assert 'SUCCESS' in res


    def test_IUMSCUTS0010_2(self):
        '''绑卡解约信息登记'''
        app = IUMS()
        custna = "庾鳒"
        certno = "510303198706236659"
        cardno = "6216613431287596204"
        res = app.IUMSCUTS0010_2(custna,certno,cardno).text()
        assert 'SUCCESS' in res



    def test_IUMSCUTS0011(self):
        """查询卡信息"""
        app = IUMS()
        cardno = "6216613431287596204"
        res = app.IUMSCUTS0011(cardno).text()
        assert 'SUCCESS' in res


    def test_IUMSCUTS0009(self):
        """绑卡签约信息查询"""
        app = IUMS()
        certno = "510303198706236659"
        custid = "B00000003511"
        res = app.IUMSCUTS0009(certno=certno, custid=custid).text()
        assert 'SUCCESS' in res
