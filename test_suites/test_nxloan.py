from api.channel.nxloan import TOUTIAO_nxloan, JDJR_nxloan, LXIN_nxloan, QUNR_nxloan
from api.identity import IdNumber
from api.randstr import get_name, get_tel, generate_random_num



class Test_Nxloan:

    def test_nxloan_toutiao(self):
        """头条产品贷款放款"""
        name = get_name()
        custac = "802" + generate_random_num(9)     # 客户号
        idtfno = IdNumber.generate_id(1)            # 身份证
        # name = "戎妨"
        # custac = "802552601960"
        # idtfno = "532325198911302890"
        phone = get_tel()                           # 手机号码
        crdlam = "5000"                             # 新增额度
        tranam = "1000"                             # 占用和放款金额
        appday = "20210331"                         # 申请日期
        acctno = "622205" + generate_random_num(8)  # 银行账号
        exordr = generate_random_num(8)             # 外部订单号
        ordrid = "000" + generate_random_num(10)    # 订单号
        chcksq = "LN" + generate_random_num(8)      # 网贷流水

        app = TOUTIAO_nxloan()
        addcll_res = app.addcll(custac, idtfno, name, phone, ordrid, crdlam, appday).json()
        assert addcll_res["sys"]['erortx'] == "SUCCESS"     # 断言
        crdlno = addcll_res['output']['crdlno']             # 获取额度编号
        cntrno = addcll_res['output']['crdlno']
        # cntrno = crdlno = "7010000000213"
        apoccu_res = app.apoccu(crdlno, exordr, ordrid, appday, tranam).json()
        assert apoccu_res["sys"]['erortx'] == "SUCCESS"     # 断言
        ybloan_res = app.ybloan(name, custac, idtfno, ordrid, cntrno, acctno, exordr, appday, chcksq, tranam).json()
        assert ybloan_res["sys"]['erortx'] == "SUCCESS"     # 断言
        nxloan_res = app.nxloan(name, custac, idtfno, ordrid, cntrno, acctno, appday, chcksq, tranam).json()
        assert nxloan_res["sys"]['erortx'] == "SUCCESS"     # 断言


    def test_nxloan_JDJR(self):
        """京东产品贷款放款"""
        name = get_name()
        custac = "802" + generate_random_num(9)     # 客户号
        idtfno = IdNumber.generate_id(1)            # 身份证
        phone = get_tel()                           # 手机号码
        crdlam = "5000"                             # 新增额度
        appday = "20210330"                         # 申请日期
        acctno = "622205" + generate_random_num(8)  # 银行账号
        exordr = generate_random_num(8)             # 外部订单号
        ordrid = "000" + generate_random_num(10)    # 订单号
        chcksq = "LN" + generate_random_num(8)      # 网贷流水

        app = JDJR_nxloan()
        """新增额度交易"""
        addcll_res = app.addcll(custac, idtfno, name, phone, ordrid, crdlam, appday).json()
        assert addcll_res["sys"]['erortx'] == "SUCCESS"     # 断言
        crdlno = addcll_res['output']['crdlno']             # 获取额度编号
        cntrno = addcll_res['output']['crdlno']
        """额度占用"""
        apoccu_res = app.apoccu(crdlno, exordr, ordrid, appday).json()
        assert apoccu_res["sys"]['erortx'] == "SUCCESS"     # 断言
        """预放款"""
        ybloan_res = app.ybloan(name, custac, idtfno, ordrid, cntrno, acctno, exordr, appday, chcksq).json()
        assert ybloan_res["sys"]['erortx'] == "SUCCESS"     # 断言
        """放款"""
        nxloan_res = app.nxloan(name, custac, idtfno, ordrid, cntrno, acctno, appday, chcksq).json()
        assert nxloan_res["sys"]['erortx'] == "SUCCESS"     # 断言


    def test_LXIN_nxloan(self):
        """乐信产品贷款放款"""
        name = get_name()
        custac = "802" + generate_random_num(9)         # 客户号
        idtfno = IdNumber.generate_id(1)                # 身份证
        phone = get_tel()                               # 手机号码
        crdlam = "5000"                                 # 新增额度
        appday = "20201226"                             # 申请日期
        acctno = "622205" + generate_random_num(8)      # 银行账号
        exordr = generate_random_num(8)                 # 外部订单号
        ordrid = "000" + generate_random_num(10)        # 订单号
        chcksq = "LN" + generate_random_num(8)          # 网贷流水

        app = LXIN_nxloan()
        """新增额度交易"""
        addcll_res = app.addcll(custac, idtfno, name, phone, ordrid, crdlam, appday).json()
        assert addcll_res["sys"]['erortx'] == "SUCCESS"  # 断言
        crdlno = addcll_res['output']['crdlno']  # 获取合同编号
        cntrno = addcll_res['output']['crdlno']
        """额度占用"""
        apoccu_res = app.apoccu(crdlno, exordr, ordrid, appday).json()
        assert apoccu_res["sys"]['erortx'] == "SUCCESS"  # 断言
        """预放款"""
        ybloan_res = app.ybloan(name, custac, idtfno, ordrid, cntrno, acctno, exordr, appday, chcksq).json()
        assert ybloan_res["sys"]['erortx'] == "SUCCESS"  # 断言
        """放款"""
        nxloan_res = app.nxloan(name, custac, idtfno, ordrid, cntrno, acctno, appday, chcksq).json()
        assert nxloan_res["sys"]['erortx'] == "SUCCESS"  # 断言


    def test_nxloan_QUNR(self):
        """去哪儿产品贷款放款"""
        name = get_name()
        custac = "802" + generate_random_num(9)     # 客户号
        idtfno = IdNumber.generate_id(1)            # 身份证
        phone = get_tel()                           # 手机号码
        crdlam = "5000"                             # 新增额度
        appday = "20210130"                         # 申请日期
        acctno = "622205" + generate_random_num(8)  # 银行账号
        exordr = generate_random_num(8)             # 外部订单号
        ordrid = "000" + generate_random_num(10)    # 订单号
        chcksq = "LN" + generate_random_num(8)      # 网贷流水

        app = QUNR_nxloan()
        """新增额度交易"""
        addcll_res = app.addcll(custac, idtfno, name, phone, ordrid, crdlam, appday).json()
        assert addcll_res["sys"]['erortx'] == "SUCCESS"     # 断言
        crdlno = addcll_res['output']['crdlno']             # 获取合同编号
        cntrno = addcll_res['output']['crdlno']
        """额度占用"""
        apoccu_res = app.apoccu(crdlno, exordr, ordrid, appday).json()
        assert apoccu_res["sys"]['erortx'] == "SUCCESS"     # 断言
        """预放款"""
        ybloan_res = app.ybloan(name, custac, idtfno, ordrid, cntrno, acctno, exordr, appday, chcksq).json()
        assert ybloan_res["sys"]['erortx'] == "SUCCESS"     # 断言
        """放款"""
        nxloan_res = app.nxloan(name, custac, idtfno, ordrid, cntrno, acctno, appday, chcksq).json()
        assert nxloan_res["sys"]['erortx'] == "SUCCESS"     # 断言