from api.channel.JDJR import JDJR_apply


class TestApply:


    def test_PATSJDSS1001(self):
        """京东授信申请"""
        app = JDJR_apply()
        res = app.PATSJDSS1001().text()
        app.PATSJDSS1004().text()
        assert 'SUCCESS' in res



    def test_PATSJDSS1004(self):
        """实时授信额度查询"""
        app = JDJR_apply()
        res = app.PATSJDSS1004().text()
        assert 'SUCCESS' in res