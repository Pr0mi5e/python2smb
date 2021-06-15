import schedule
import time
import requests
import socket
import rsa
import base64
import random

base_url = "https://we.chinaedu.net/volbeacon"
user_list = [
    {
        "user_name": "gaoxiang1_dl",
        "password": "123456"
    },
    {
        "user_name": "dingru",
        "password": "dingru0515"
    }
]
# 任务字典 key未执行任务的时间点，value未登录用户信息{user_name: String, password: String}
task_dict = {}
# 任务列表，保存每天的登录任务
job_list = []


def _str2key(s):
    # 对字符串解码
    b_str = base64.b64decode(s)

    if len(b_str) < 162:
        return False

    hex_str = ''

    # 按位转换成16进制
    for x in b_str:
        h = hex(x)[2:]
        h = h.rjust(2, '0')
        hex_str += h

    # 找到模数和指数的开头结束位置
    m_start = 29 * 2
    e_start = 159 * 2
    m_len = 128 * 2
    e_len = 3 * 2

    modulus = hex_str[m_start:m_start + m_len]
    exponent = hex_str[e_start:e_start + e_len]

    return modulus, exponent


# 加密
def rsa_encrypt(s, pubkey_str):
    key = _str2key(pubkey_str)
    modulus = int(key[0], 16)
    exponent = int(key[1], 16)
    pubkey = rsa.PublicKey(modulus, exponent)
    return base64.b64encode(rsa.encrypt(s.encode(), pubkey)).decode()


# 登录
def login(login_id, password_encryption, user_name):
    url = "/login/login.do?execute=1"
    data = {
        "loginType": (None, 1),
        "type": (None, 1),
        "administrativeCode": (None, 210200),
        "ip": (None, ip),
        "cityName": (None, "辽宁省大连市"),
        "abc": (None, user_name),
        "loginId": (None, login_id),
        "passwordEncryption": (None, password_encryption)
    }
    res = requests.post(base_url + url, files=data)
    if res.status_code == 200:
        print(user_name + "登录成功！")


# 获取公钥
def login_encrypt(task_time):
    url = "/common/loginEncrypt.do"
    res = requests.post(base_url + url)
    public_rsa_key = res.json()['publicRSAKey']
    login_id = res.json()['loginId']
    user = task_dict[task_time]
    password_encryption = rsa_encrypt(user["password"], public_rsa_key)
    print(user["password"])
    user_name = user["user_name"]
    print(password_encryption, login_id)
    login(login_id, password_encryption, user_name)


# 获取ip
hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)


# 随机时间
def round_time():
    h = random.randint(9, 10)
    m = random.randint(0, 59)
    task_time = str(h).zfill(2) + ":" + str(m).zfill(2)
    # task_time = "13:28"
    return task_time


# 取消前一日的定时任务
def cancel_job():
    for job in job_list:
        schedule.cancel_job(job)
    job_list.clear()


# 初始化任务
def init_job():
    cancel_job()
    task_dict.clear()
    for user in user_list:
        task_time = round_time()
        print("今天" + task_time + "登录用户" + user["user_name"])
        task_dict[task_time] = user
        job = schedule.every().day.at(task_time).do(login_encrypt, task_time)
        job_list.append(job)


# init_job()
schedule.every().day.at("08:48").do(init_job)
while True:
    schedule.run_pending()
    time.sleep(1)

