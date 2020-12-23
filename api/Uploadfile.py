import os
import tarfile
import paramiko
from api.randstr import get_date


#创建一个通道
private_dir = 'D:\\Python_work\\walnuts_api\\api_test\\img\\id_rsa_pc_zyxj_staging'

def readname(src_file):\
    # 获取影像件路径
    name = os.listdir(src_file)
    return src_file+name[0]

def rename(src_file,filename):
    # 修改文件名称
    oldname = readname(src_file)
    os.rename(oldname, src_file + filename)
    newname = readname(src_file)
    return newname


def upload(src_file, dsc_path):
    # 将影像件上传——10.182.211.137服务器
    transport = paramiko.Transport(('10.182.211.137', 22))
    transport.connect(username='root', password='root123')
    ssh = paramiko.SSHClient()
    ssh._transport = transport
    sftp = paramiko.SFTPClient.from_transport(transport)
    sftp.put(src_file, dsc_path)
    transport.close()

def upload_LXIN(src_file, dsc_path):
    # 将影像件上传——10.182.210.155服务器
    transport = paramiko.Transport(('10.182.210.155', 22222))
    transport.connect(username='lexin01', password='!Q2w3e4r')
    ssh = paramiko.SSHClient()
    ssh._transport = transport
    sftp = paramiko.SFTPClient.from_transport(transport)
    sftp.put(src_file, dsc_path)
    transport.close()

def upload_MI(src_file, dsc_path):
    # 影像件上传——小米服务器
    private = paramiko.RSAKey.from_private_key_file(private_dir)
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname='120.92.15.135', port=2222, username='pc_zyxj', pkey=private)
    transport = ssh.get_transport()
    sftp = paramiko.SFTPClient.from_transport(transport)
    sftp.put(src_file, dsc_path)
    transport.close()

# def mkdir(filename):
#     try:
#         ssh = paramiko.SSHClient()
#         ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#         ssh.connect(hostname, username=username, password=password)
#         sftp = ssh.open_sftp()
#         dir = "/upload/crpl_zhongyin/20201124/ocr/" + filename
#         sftp.mkdir(dir)
#         print("Create folder" + filename + "in remote hosts successfully!\n")
#         ssh.close()
#     except:
#         print("Create folder failure!\n")


def get_tar(applyNo):
    data = get_date()
    filename = applyNo + "_" + data + ".tar"
    tar = tarfile.open("D:\\Python_work\\walnuts_api\\api_test\\img\\"+ filename, "w")
    tar.add("D:\\Python_work\\walnuts_api\\api_test\\img\\1.jpg", arcname=applyNo + "_idcard_01.jpg")
    tar.add("D:\\Python_work\\walnuts_api\\api_test\\img\\2.jpg", arcname=applyNo + "_idcard_02.jpg")
    tar.add("D:\\Python_work\\walnuts_api\\api_test\\img\\3.jpg", arcname=applyNo + "_face.jpg")
    tar.close()
    return filename

def exec_commands(cmd):
    transport = paramiko.Transport(('10.182.211.137', 22))
    transport.connect(username='root', password='root123')
    ssh = paramiko.SSHClient()
    ssh._transport = transport
    stdin, stdout, stderr = ssh.exec_command(cmd)
    results = stdout.read()
    return results




if __name__ == "__main__":
    applyNo = "123456789"
    app = get_tar(applyNo)
    src = "D:\\Python_work\\walnuts_api\\api_test\\img\\" + app
    path = "/upload/LXIN/photo/20201202/" + app
    print(app)
    upload(src, path)
