import os
import paramiko

#创建一个通道
hostname = '10.182.211.137'
username = 'root'
password = 'root123'
# dsc_path = '/credit/img/20201030/'
src_file = 'D:\\Python_work\\walnuts_api\\api_test\\resources\\'
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
    transport = paramiko.Transport((hostname, 22))
    transport.connect(username=username, password=password)
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

def mkdir(filename):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname, username=username, password=password)
        sftp = ssh.open_sftp()
        dir = "/upload/crpl_zhongyin/20201124/ocr/" + filename
        sftp.mkdir(dir)
        print("Create folder" + filename + "in remote hosts successfully!\n")
        ssh.close()
    except:
        print("Create folder failure!\n")



if __name__ == "__main__":
    filename = "test112"
    mkdir(filename)
    dir = "/upload/crpl_zhongyin/20201124/ocr/" + filename + "/vip_img01.txt"
    img1 = 'D:\\Python_work\\walnuts_api\\api_test\\resources\\vip_img01.txt'
    img2 = 'D:\\Python_work\\walnuts_api\\api_test\\resources\\vip_img02.txt'
    img3 = 'D:\\Python_work\\walnuts_api\\api_test\\resources\\vip_img03.txt'
    upload(img1, dir)
    # upload(img2, dir)
    # upload(img3, dir)
