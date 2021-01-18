from api.channel.core import CORE,MIFI
from api.randstr import get_tel, generate_random_num,get_name
from api.identity import IdNumber


class Test_core:


    def test_qrclov(self):
        """查询客户额度总览"""
        app = CORE()
        idtfno = "362302198601095789"
        res = app.CORECLTS1048(idtfno=idtfno).json()
        assert res["sys"]['erortx'] == "SUCCESS"  # 断言

    def test_qryspy(self):
        """查询应收还款额"""
        app = CORE()
        res = app.CORELNTS2002().json()
        assert res["sys"]['erortx'] == "SUCCESS"  # 断言


    def test_JDJR(self):
        custac = "A000" + generate_random_num(8)    # 客户号
        idtfno = IdNumber.generate_id(1)            # 身份证
        name = get_name()                        # 客户名称
        phone = get_tel()                       # 手机号码
        crdlam = "8000"                         # 新增额度
        appday = "20201231"
        exordr = generate_random_num(8)         # 外部订单号
        ordrid = "000" + generate_random_num(10)

        """新增京东产品额度"""
        app = CORE()
        addcll_res = app.addcll(custac, idtfno, name, phone, ordrid, crdlam, appday).json()
        assert addcll_res["sys"]['erortx'] == "SUCCESS"  # 断言
        crdlno = addcll_res['output']['crdlno']  # 获取合同编号
        """额度占用"""
        apoccu_res = app.apoccu(crdlno, exordr, ordrid, appday).json()
        assert apoccu_res["sys"]['erortx'] == "SUCCESS"  # 断言


    def test_MIFI(self):
        custac = "A000" + generate_random_num(8)  # 客户号
        idtfno = IdNumber.generate_id(1)  # 身份证
        name = get_name()  # 客户名称
        phone = get_tel()  # 手机号码
        crdlam = "5000"  # 新增额度
        appday = "20201231"
        exordr = generate_random_num(8)  # 外部订单号
        ordrid = "000" + generate_random_num(10)

        """新增小米产品额度"""
        app = MIFI()
        addcll_res = app.addcll(custac, idtfno, name, phone, ordrid, crdlam, appday).json()
        assert addcll_res["sys"]['erortx'] == "SUCCESS"  # 断言
        crdlno = addcll_res['output']['crdlno']  # 获取合同编号
        """额度占用"""
        apoccu_res = app.apoccu(crdlno, exordr, ordrid, appday).json()
        assert apoccu_res["sys"]['erortx'] == "SUCCESS"  # 断言