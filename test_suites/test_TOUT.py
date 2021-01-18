from api.channel.TOUT import TOUT
from api.identity import IdNumber
from api.database import database_icms, database_pats, database_iums
from api.base import get_image_03_base, get_image_02_base, get_image_01_base
from api.randstr import generate_random_num, getStrAsMD5


class TestTout:

    def test_PATSTTSS1001(self):
        """   """
        app = TOUT()
        account_id = int(generate_random_num(13))
        identity = IdNumber.generate_id(2)
        """头条资质预审接口"""
        idmd5 = getStrAsMD5(identity)
        identity_res = app.PATSTTSS1007(idmd5).json()
        assert identity_res['output']['status'] == "1"  # 断言
        """影像件上传"""
        img_01 = get_image_01_base()                    # 国徽面
        img_02 = get_image_02_base()                    # 人脸面
        img_03 = get_image_03_base()                    # 手持证件
        img_01_res = app.PATSTTSS1008(account_id, img_02, "1.jpg", "03").json()
        assert img_01_res["sys"]['erorcd'] == "AAAAAAAAAA"  # 断言
        img_02_res = app.PATSTTSS1008(account_id, img_01, "2.jpg", "70").json()
        assert img_02_res["sys"]['erorcd'] == "AAAAAAAAAA"  # 断言
        img_03_res = app.PATSTTSS1008(account_id, img_03, "3.jpg", "40").json()
        assert img_03_res["sys"]['erorcd'] == "AAAAAAAAAA"  # 断言
        """头条授信申请"""
        res = app.PATSTTSS1001(account_id, identity).json()
        assert res["sys"]['erorcd'] == "AAAAAAAAAA"  # 断言


    def test_PATSTTSS1003(self):
        """额度申请进度查询"""
        app = TOUT()
        account_id = "6468871206465"
        res = app.PATSTTSS1003(account_id).json()
        assert res["sys"]['erorcd'] == "AAAAAAAAAA"  # 断言


    def test_PATSTTSS1004(self):
        """头条账户额度信息查询"""
        app = TOUT()
        account_id = "6468871206465"
        res = app.PATSTTSS1004(account_id).json()
        assert res["sys"]['erorcd'] == "AAAAAAAAAA"  # 断言


    def test_PATSTTSS1009(self):
        """账户信息更新接口"""
        app = TOUT()
        account_id = "3345995578711"
        name = "郗崽捽"
        identity = "530402198306237962"
        res = app.PATSTTSS1009(account_id, name, identity).json()
        assert res['sys']['erorcd'] == 'AAAAAAAAAA'  # 断言


    def test_PATSTTSS1006(self):
        """补件信息提交(借款提交前调⽤)"""
        app = TOUT()
        account_id = "2772817343649"
        res = app.PATSTTSS1006(account_id).json()
        assert res['sys']['erorcd'] == 'AAAAAAAAAA'  # 断言


    def test_PATSTTSS1011(self):
        """头条绑卡签约触发短信"""
        account_id = "2772817343649"
        app = TOUT()
        database = database_icms['sit2']
        res = app.PATSTTSS1011(account_id, database).json()
        assert res['output']['status'] == '1'  # 断言

        """头条校验验证码并绑定银行卡"""
        token = res['output']['sms_token']
        token_res = app.PATSTTSS1012(account_id, token).json()
        assert token_res['output']['status'] == '1'  # 断言


    def test_PATSTTSS1010(self):
        """支持银行卡列表查询"""
        app = TOUT()
        res = app.PATSTTSS1010().json()
        assert res['sys']['erorcd'] == 'AAAAAAAAAA'  # 断言


    def test_PATSTTSS2001(self):
        """头条借款申请接口"""
        app = TOUT()
        account_id = "2772817343649"
        database = database_iums['sit2']
        res = app.PATSTTSS2001(account_id, database).json()
        assert res['sys']['erorcd'] == 'AAAAAAAAAA'  # 断言


    def test_PATSPYSS1001(self):
        """支付网关回调"""
        app = TOUT()
        account_id = "TT975985939841"
        res = app.PATSPYSS1001(account_id).json()
        assert res['sys']['erorcd'] == 'AAAAAAAAAA'  # 断言


    def test_PATSTTSS2002(self):
        """借款进度查询"""
        app = TOUT()
        account_id = "TT975985939841"
        database = database_pats['sit3']
        res = app.PATSTTSS2002(account_id, database).json()
        assert res['sys']['erorcd'] == 'AAAAAAAAAA'  # 断言


    def test_PATSTTSS3003(self):
        """用户借款查询结果"""
        app = TOUT()
        account_id = "TT975985939841"
        res = app.PATSTTSS3003(account_id).json()
        assert res['sys']['erorcd'] == 'AAAAAAAAAA'  # 断言


    def test_PATSTTSS3004(self):
        """借款详情"""
        app = TOUT()
        account_id = "2772817343649"
        database = database_pats['sit2']
        res = app.PATSTTSS3004(account_id, database).json()
        assert res['sys']['erorcd'] == 'AAAAAAAAAA'  # 断言



    def test_PATSTTSS3001(self):
        """头条还款申请"""
        app = TOUT()
        account_id = "959595880339"
        database_P = database_pats['sit6']
        database_i = database_iums['sit6']
        res = app.PATSTTSS3001(account_id, database_P, database_i).json()
        assert res['sys']['erorcd'] == 'AAAAAAAAAA'  # 断言


    def test_PATSTTSS8003(self):
        """息费计算"""
        app = TOUT()
        account_id = "122021034105045"
        res = app.PATSTTSS8003(account_id).json()
        assert res['sys']['erorcd'] == 'AAAAAAAAAA'  # 断言


    def test_PATSTTSS3005(self):
        """LPR利率查询"""
        app = TOUT()
        account_id = "1220210105034"
        res = app.PATSTTSS3005(account_id).json()
        assert res['sys']['erorcd'] == 'AAAAAAAAAA'  # 断言



    def test_PATSTTSS8001(self):
        """头条还款计划查询"""
        app = TOUT()
        account_id = "TT933822103927"
        res = app.PATSTTSS8001(account_id).json()
        assert res['sys']['erorcd'] == 'AAAAAAAAAA'  # 断言


    def test_PATSTTSS8002(self):
        """头条还款试算"""
        app = TOUT()
        account_id = "TT933822103927"
        res = app.PATSTTSS8002(account_id).json()
        assert res['sys']['erorcd'] == 'AAAAAAAAAA'  # 断言


    def test_PATSTTSS4007(self):
        """头条还款记录列表查询接口"""
        app = TOUT()
        account_id = "TT669955338791"
        res = app.PATSTTSS4007(account_id).json()
        assert res['sys']['erorcd'] == 'AAAAAAAAAA'  # 断言


    def test_PATSTTSS4008(self):
        """本月账单查询"""
        app = TOUT()
        account_id = "TT933822103927"
        res = app.PATSTTSS4008(account_id).json()
        assert res['sys']['erorcd'] == 'AAAAAAAAAA'  # 断言


    def test_PATSTTSS4009(self):
        """头条还款进度查询接口"""
        app = TOUT()
        account_id = "2023101041593"
        database_p = database_pats['sit2']
        res = app.PATSTTSS4009(account_id, database_p).json()
        assert res['sys']['erorcd'] == 'AAAAAAAAAA'  # 断言