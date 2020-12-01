import cx_Oracle as cx


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
    '''获取进件中心 applid'''
    # 设置ORACLE驱动位置
    os.environ['path'] = r'D:\\Program\\instantclient_19_8'
    # 建立与sit3进件中心数据库的连接
    con = cx.connect('icms', 'Add#180530', '10.182.211.207:1521/icms')
    cursor = con.cursor()
    cursor.execute("select requestid from icms.klnb_tele_check where applid=:applid", applid=applid)
    data = cursor.fetchone()
    return data[0]