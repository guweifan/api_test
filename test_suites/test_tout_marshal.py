from api.channel.TOUT_marshal import TOUT_marshal
from api.identity import IdNumber
from api.database import database_icms, database_pats, database_iums
from api.base import get_image_03_base, get_image_02_base, get_image_01_base
from api.randstr import generate_random_num, getStrAsMD5


class TestTout:

    def test_PATSTTSS1001(self):
        """   """
        app = TOUT_marshal()
        account_id = 7945120702607
        identity = IdNumber.generate_id(2)
        """头条资质预审接口"""
        idmd5 = getStrAsMD5(identity)
        identity_res = app.PATSTTSS1007(idmd5).json()           # 报文加密
        prequalification_res = app.prequalification(identity_res).json()        # 发送加密请求
        assert prequalification_res["msg"] == "成功"  # 断言
        unmarshal_res = app.unmarshal(prequalification_res).json()              # 解密响应报文
        assert unmarshal_res["status"] == 1  # 断言

        """头条额度申请提交"""
        res = app.PATSTTSS1001(account_id, identity).json()  # 报文加密
        creditApply_res = app.creditApply(res).json()  # 发送加密请求
        unmarshal_res = app.unmarshal(creditApply_res).json()  # 解密响应报文
        assert unmarshal_res["status"] == 1  # 断言

    def test_PATSTTSS1008(self):
        app = TOUT_marshal()
        """生成accountid"""
        account_id = int(generate_random_num(13))
        """影像件上传"""
        img_01 = get_image_01_base()                    # 国徽面
        img_02 = get_image_02_base()                    # 人脸面
        img_03 = get_image_03_base()                    # 手持证件
        img_01_res = app.PATSTTSS1008(account_id, img_02, "1.jpg", "03").json()     # 报文加密
        image1Upload_res = app.imageUpload(img_01_res).json()                       # 发送加密请求
        assert image1Upload_res["code"] == "0"  # 断言
        # unmarshal_res = app.unmarshal(image1Upload_res).json()  # 解密响应报文

        img_02_res = app.PATSTTSS1008(account_id, img_01, "2.jpg", "70").json()
        image2Upload_res = app.imageUpload(img_02_res).json()  # 发送加密请求
        assert image2Upload_res["code"] == "0"  # 断言
        # unmarshal_res = app.unmarshal(image2Upload_res).json()  # 解密响应报文

        img_03_res = app.PATSTTSS1008(account_id, img_03, "3.jpg", "40").json()
        image3Upload_res = app.imageUpload(img_03_res).json()  # 发送加密请求
        assert image3Upload_res["code"] == "0"  # 断言
        # unmarshal_res = app.unmarshal(image3Upload_res).json()  # 解密响应报文




    def test_PATSTTSS1003(self):
        """额度申请进度查询"""
        app = TOUT_marshal()
        account_id = 3254204772653933
        res = app.PATSTTSS1003(account_id).json()       # 报文加密
        creditInquiry_res = app.creditInquiry(res).json()    # 发送加密的请求报文
        assert creditInquiry_res["msg"] == "成功"  # 断言
        app.unmarshal(creditInquiry_res).json()  # 解密响应报文


    def test_PATSTTSS1004(self):
        """头条账户额度信息查询"""
        app = TOUT_marshal()
        account_id = 3254204772653933
        res = app.PATSTTSS1004(account_id).json()
        accountInfo_res = app.accountInfo(res).json()
        assert accountInfo_res["msg"] == "成功"  # 断言
        app.unmarshal(accountInfo_res).json()  # 解密响应报文


    def test_PATSTTSS8003(self):
        """息费计算"""
        app = TOUT_marshal()
        account_id = 735219254116
        res = app.PATSTTSS8003(account_id).json()
        loansCalc_res = app.loansCalc(res).json()  # 发送加密的请求报文
        assert loansCalc_res['msg'] == '成功'  # 断言
        app.unmarshal(loansCalc_res).json()  # 解密响应报文
        # assert res['sys']['erorcd'] == 'AAAAAAAAAA'  # 断言



    def test_PATSTTSS1009(self):
        """账户信息更新接口"""
        app = TOUT_marshal()
        account_id = 735219254116
        name = "姜獙"
        identity = "150223198705165126"
        res = app.PATSTTSS1009(account_id, name, identity).json()  # 请求报文加密
        accountUpdate_res = app.accountUpdate(res).json()       # 发送加密的请求报文
        assert accountUpdate_res['msg'] == '成功'  # 断言
        app.unmarshal(accountUpdate_res).json()  # 解密响应报文



    def test_PATSTTSS1006(self):
        """补件信息提交(联系人补充)"""
        app = TOUT_marshal()
        account_id = 3254204772653933
        res = app.PATSTTSS1006(account_id).json()                   # 报文加密
        creditSupplement_res = app.creditSupplement(res).json()     # 发送加密请求
        assert creditSupplement_res['msg'] == '成功'  # 断言
        app.unmarshal(creditSupplement_res).json()  # 解密响应报文


    def test_PATSTTSS1011(self):
        """头条绑卡签约触发短信"""
        account_id = 3254204772653933
        app = TOUT_marshal()
        database = database_icms['sit3']
        res = app.PATSTTSS1011(account_id, database).json()     # 请求报文加密
        sendBindcardCheckCode_res = app.sendBindcardCheckCode(res).json()   # 发送加密请求报文
        assert sendBindcardCheckCode_res['msg'] == '成功'  # 断言
        pop = app.unmarshal(sendBindcardCheckCode_res).json()  # 解密响应报文
        assert pop['status'] == 1  # 断言

        """头条校验验证码并绑定银行卡"""
        token = pop['sms_token']
        token_res = app.PATSTTSS1012(account_id, token).json()          # 请求报文加密
        generalBindcard_res = app.generalBindcard(token_res).json()     # 发送加密请求报文
        unmarshal_res = app.unmarshal(generalBindcard_res).json()  # 解密响应报文
        assert unmarshal_res['status'] == 1  # 断言


    def test_PATSTTSS1010(self):
        """支持银行卡列表查询"""
        app = TOUT_marshal()
        res = app.PATSTTSS1010().json()        # 报文加密
        generalBanks_res = app.generalBanks(res).json()     # 发送加密的请求报文
        assert res['msg'] == '成功'  # 断言
        app.unmarshal(generalBanks_res).json()  # 解密响应报文


    def test_PATSTTSS2001(self):
        """头条借款申请接口"""
        app = TOUT_marshal()
        account_id = 1044303482850
        bank_account = "6221511610795344963"
        res = app.PATSTTSS2001(account_id, bank_account).json()     # 报文加密
        loansApply_res = app.loansApply(res).json()             # 发送加密请求报文
        assert loansApply_res['msg'] == '成功'  # 断言
        app.unmarshal(loansApply_res).json()              # 解密响应报文



    def test_PATSTTSS2002(self):
        """借款进度查询"""
        app = TOUT_marshal()
        account_id = 1044303482850
        req_id = 2852733773
        res = app.PATSTTSS2002(account_id, req_id).json()       # 报文加密
        loansInquiry_res = app.loansInquiry(res).json()         # 发送加密请求
        assert loansInquiry_res['msg'] == '成功'  # 断言
        app.unmarshal(loansInquiry_res).json()  # 解密响应报文


    def test_PATSTTSS3003(self):
        """用户借款查询结果"""
        app = TOUT_marshal()
        account_id = "TT975985939841"
        res = app.PATSTTSS3003(account_id).json()

        assert res['sys']['erorcd'] == 'AAAAAAAAAA'  # 断言


    def test_PATSTTSS3004(self):
        """借款详情"""
        app = TOUT_marshal()
        account_id = 1044303482850
        req_id = 2852733773
        res = app.PATSTTSS3004(account_id, req_id).json()     # 报文加密
        loansDetail_res = app.loansDetail(res).json()           # 发送加密的请求报文
        assert loansDetail_res['msg'] == '成功'  # 断言
        app.unmarshal(loansDetail_res).json()                   # 解密响应报文




    def test_PATSTTSS3001(self):
        """头条还款申请"""
        app = TOUT_marshal()
        account_id = 1044303482850
        req_id = 2852733773
        bank_account = "6221511610795344963"
        res = app.PATSTTSS3001(account_id, req_id, bank_account).json()     # 报文加密
        repaySubmit_res = app.repaySubmit(res).json()           # 发送加密请求
        assert repaySubmit_res['msg'] == '成功'  # 断言
        app.unmarshal(repaySubmit_res).json()



    def test_PATSTTSS3005(self):
        """LPR利率查询"""
        app = TOUT_marshal()
        account_id = "1220210105034"
        res = app.PATSTTSS3005(account_id).json()
        assert res['sys']['erorcd'] == 'AAAAAAAAAA'  # 断言



    def test_PATSTTSS8001(self):
        """头条还款计划查询"""
        app = TOUT_marshal()
        account_id = 735219254116
        req_id = 9092691008
        res = app.PATSTTSS8001(account_id, req_id).json()
        repayPlan_res = app.repayPlan(res).json()  # 发送加密的请求报文
        assert repayPlan_res['msg'] == '成功'  # 断言
        app.unmarshal(repayPlan_res).json()  # 解密响应报文



    def test_PATSTTSS8002(self):
        """头条还款试算"""
        app = TOUT_marshal()
        account_id = 735219254116
        req_id = 7977628203
        res = app.PATSTTSS8002(account_id, req_id).json()       # 报文加密
        trialPrepay_res = app.trialPrepay(res).json()   # 发送加密请求
        assert trialPrepay_res['msg'] == '成功'  # 断言
        app.unmarshal(trialPrepay_res).json()


    def test_PATSTTSS4007(self):
        """头条还款记录列表查询接口"""
        app = TOUT_marshal()
        account_id = "TT669955338791"
        res = app.PATSTTSS4007(account_id).json()
        assert res['sys']['erorcd'] == 'AAAAAAAAAA'  # 断言


    def test_PATSTTSS4008(self):
        """本月账单查询"""
        app = TOUT_marshal()
        account_id = 1044303482850
        res = app.PATSTTSS4008(account_id).json()           # 报文加密
        repayCurbill_res = app.repayCurbill(res).json()     # 发送加密请求
        assert repayCurbill_res['msg'] == '成功'  # 断言
        app.unmarshal(repayCurbill_res).json()


    def test_PATSTTSS4009(self):
        """头条还款进度查询接口"""
        app = TOUT_marshal()
        account_id = 735219254116
        req_id = 9092691008
        repay_id = "388749757701"
        res = app.PATSTTSS4009(account_id, req_id, repay_id).json()     # 报文加密
        repayProgress_res = app.repayProgress(res).json()           # 发送加密报文
        assert repayProgress_res['msg'] == '成功'  # 断言
        app.unmarshal(repayProgress_res).json()

