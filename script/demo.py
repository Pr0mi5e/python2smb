#!/usr/bin/python
# run 'python -m pip install pysmb' to install pysmb

from smb.SMBConnection import SMBConnection
import zipfile
import os
import time

host = '172.16.98.12' # 远程主机IP
username = 'chinaedu' # 用户名
password = 'chinaedu' # 密码
share_device = 'guola' # 主机分享文件夹
zip_file_name = '/dist.zip'

# 本地路径配置
backup_file_path = 'D:/backup/oneYuanPurchase' # 备份文件路径
project_path = 'E:/h5/oneYuanPurchase/dist' # 项目路径
zip_file = project_path + zip_file_name # 本地压缩文件

# 远程主机路径配置
origin_sub_path = '/oneYuanPurchase' # 主机项目文件夹相对路径
origin_path = '//' + host + '/' +  share_device + origin_sub_path # 主机项目绝对路径
origin_zip_file = origin_sub_path + zip_file_name # 主机压缩文件相对路径


# 构建项目
print('开始构建项目')
os.system('npm run build')

# 压缩
def zip( projectPath, zipFile ):
    print('开始压缩dist文件夹')
    file_list = []
    for root, dirs, files in os.walk(projectPath):
        for name in files:
            file_list.append(os.path.join(root, name))
    zf = zipfile.ZipFile(zipFile, 'w', zipfile.ZIP_DEFLATED)
    for path in file_list:
        print('添加压缩文件：' + path)
        zf.write(path, path.replace(projectPath, ''))
    zf.close()
    return

# 解压
def unzip_file(zip_src, dist_dir):
    r = zipfile.is_zipfile(zip_src)
    if r:
        fz = zipfile.ZipFile(zip_src, 'r')
        for file in fz.namelist():
            fz.extract(file, dist_dir)
    else:
        print('This is not zip')
    return

# 本地项目dist压缩
zip(project_path, zip_file)

# 连接主机
conn = SMBConnection(username, username, 'any', '', use_ntlm_v2 = True)
assert conn.connect(host, 139) # smb服务器地址
if conn:
   print(host + '连接成功~')
else:
   print("failed to connect")

# 压缩远程文件
def walk_path(path):
    for p in conn.listPath(share_device, origin_sub_path + path):
        if p.filename != '.' and p.filename != '..':
            parent_path = path
            if not parent_path.endswith('/'):
                parent_path += '/'

            if p.isDirectory:
                walk_path(parent_path + p.filename)
            else:
                if not p.filename.endswith('dist.zip'):
                    print(parent_path + p.filename)
                    origin_zf.write(origin_path + parent_path + p.filename, parent_path + p.filename)
    return

origin_zf = zipfile.ZipFile(origin_path + zip_file_name, 'w', zipfile.ZIP_DEFLATED)
print('开始备份远程文件')
walk_path('/')
origin_zf.close()

# 下载
if not os.path.exists(backup_file_path):
    os.makedirs(backup_file_path)
timestamp = time.time()
backup_path = backup_file_path + '/dist_' + str(timestamp) + '.zip'
downloadFile = open(backup_path, 'wb')
conn.retrieveFile(share_device, origin_zip_file, downloadFile)
downloadFile.close()
print('备份成功!备份文件路径：' + backup_path)

# 上传
print('即将开始上传压缩文件...')
uploadFile = open(zip_file, 'rb')
conn.storeFile(share_device, origin_zip_file, uploadFile)
uploadFile.close()
print('上传zip成功')

unzip_file(origin_path + zip_file_name, origin_path)
print('远程zip解压完成~')
