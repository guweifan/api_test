import os
import cx_Oracle as cx
from api.database import database_pats,database_icms,database_iums,database_core

def get_applid(applyno):
    '''获取进件中心 applid'''
    # 设置ORACLE驱动位置
    os.environ['path'] = r'D:\\Program\\instantclient_19_8'
    # 建立与sit3进件中心数据库的连接
    # uat数据库地址:10.182.220.133
    con = cx.connect('icms', 'Add#180530', '10.182.211.207:1521/icms')
    cursor = con.cursor()
    cursor.execute("select applid from klnb_crdt_appl where applno=:applyno",applyno=applyno)
    data = cursor.fetchone()
    return data[0]

def get_requestid(applid):
    '''获取进件中心 requestid'''
    # 设置ORACLE驱动位置
    os.environ['path'] = r'D:\\Program\\instantclient_19_8'
    # 建立与sit3进件中心数据库的连接
    con = cx.connect('icms', 'Add#180530', '10.182.211.207:1521/icms')
    cursor = con.cursor()
    cursor.execute("select requestid from icms.klnb_tele_check where applid=:applid", applid=applid)
    data = cursor.fetchone()
    return data[0]


def get_cutinfo(applyno, database):
    '''获取客户信息'''
    # 设置ORACLE驱动位置
    os.environ['path'] = r'D:\\Program\\instantclient_19_8'
    con = cx.connect('icms', 'Add#180530', database)
    cursor = con.cursor()
    cursor.execute("select CUSTNA, IDTFNO, MOBINO, CUSTID from klnb_crdt_appl where applno=:applyno", applyno=applyno)
    data = cursor.fetchone()
    return data

def get_bank_card(OUT_USER_ID, database):
    """获取客户银行卡号"""
    # 设置ORACLE驱动位置
    os.environ['path'] = r'D:\\Program\\instantclient_19_8'
    # dev = '10.182.202.81:1521/um'
    con = cx.connect('iums', 'Add#180530', database)
    cursor = con.cursor()
    cursor.execute("select card_no from user_card_book where OUT_USER_ID=:OUT_USER_ID", OUT_USER_ID=OUT_USER_ID)
    data = cursor.fetchone()
    return data[0]

def get_userid(custid, database):
    """第三方客户号"""
    # 设置ORACLE驱动位置
    os.environ['path'] = r'D:\\Program\\instantclient_19_8'
    # dev = '10.182.202.81:1521/um'
    con = cx.connect('iums', 'Add#180530', database)
    cursor = con.cursor()
    cursor.execute("SELECT USERID FROM USER_INDV_INFO WHERE CUSTID =:CUSTID", CUSTID=custid)
    data = cursor.fetchone()
    return data[0]

def get_paymentno(applyno, database):
    """获取头条提现单号"""
    # 设置ORACLE驱动位置
    os.environ['path'] = r'D:\\Program\\instantclient_19_8'
    # sit2 = '10.182.211.131:1521/pats'
    # sit3 = '10.182.211.207:1521/pats'
    # dev = '10.182.202.81:1521/icms'
    con = cx.connect('pats', 'Add#180530', database)
    cursor = con.cursor()
    cursor.execute("select paymentno from POB_WITHDRAWAL_APPLY_CHILD_ORDER where applyno=:applyno", applyno=applyno)
    data = cursor.fetchone()
    return data[0]


def get_repaymentno(applyno, database):
    """获取头条提现单号"""
    # 设置ORACLE驱动位置
    os.environ['path'] = r'D:\\Program\\instantclient_19_8'
    # sit2 = '10.182.211.131:1521/pats'
    con = cx.connect('pats', 'Add#180530', database)
    cursor = con.cursor()
    cursor.execute("SELECT REPAYMENTNO FROM POB_REPAYMENT_CHILD_ORDER  WHERE APPLYNO=:applyno", applyno=applyno)
    data = cursor.fetchone()
    return data[0]

def get_TransReqSeqNo(ORDERNO):
    """获取支付网关回调流水"""
    # 设置ORACLE驱动位置
    os.environ['path'] = r'D:\\Program\\instantclient_19_8'
    sit2 = '10.182.211.131:1521/pats'
    sit3 = '10.182.211.207:1521/pats'
    # dev = '10.182.202.81:1521/icms'
    con = cx.connect('pats', 'Add#180530', sit3)
    cursor = con.cursor()
    cursor.execute("SELECT TRANSREQSEQNO FROM POB_PAYMENT_BOOK  WHERE CARDNO =:ORDERNO", ORDERNO=ORDERNO)
    data = cursor.fetchone()
    return data[0]

def get_ORDERNO(req_id):
    """获取支付网关回调流水"""
    # 设置ORACLE驱动位置
    os.environ['path'] = r'D:\\Program\\instantclient_19_8'
    sit2 = '10.182.211.131:1521/pats'
    # dev = '10.182.202.81:1521/icms'
    con = cx.connect('pats', 'Add#180530', sit2)
    cursor = con.cursor()
    cursor.execute("SELECT ORDERNO FROM POB_ORDER  WHERE IDEMPOTENTFIELD =:req_id", req_id=req_id)
    data = cursor.fetchone()
    return data[0]


if __name__ == '__main__':
    applyno = "J7923662496"
    database_i = database_iums['sit4']
    database_c = database_icms['sit4']
    custinfo = get_cutinfo(applyno,database_c)
    custinfo = get_userid(custinfo[3], database_i)
    print(custinfo)