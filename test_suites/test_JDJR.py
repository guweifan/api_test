from api.channel.JDJR import JDJR_apply
from api.database import database_icms, database_pats, database_iums


class TestApply:


    def test_PATSJDSS1001(self):
        """京东授信申请"""
        app = JDJR_apply()
        res = app.PATSJDSS1001().json()
        assert res["sys"]['erortx'] == "SUCCESS"


    def test_PATSJDSS1004(self):
        """实时授信额度查询"""
        app = JDJR_apply()
        res = app.PATSJDSS1004().json()
        assert res["sys"]['erortx'] == "SUCCESS"



    def test_PATSJDSS2001(self):
        """提现审核申请"""
        app = JDJR_apply()
        applyNo = "J7923662496"
        database_i = database_icms['sit4']
        res = app.PATSJDSS2001(applyNo, database_i).json()
        assert res["sys"]['erortx'] == "SUCCESS"

