import requests        #导入requests包
url = 'http://172.16.94.161:3000/#/home'
strhtml = requests.get(url)        #Get方式获取网页数据
print(strhtml.text)
