# import requests
# import json
# proxies={'http':'http://localhost:8888'}
# # headers={'Content-Type':'application/json;charset=utf-8'}
# headers={}
# headers['Content-Type']='application/json;charset=utf-8'
#
# resp=requests.post(url="http://192.168.1.203:8083/sys/login",
#                    proxies=proxies,
#                    data='{"userName":"18210034706","password":"123456"}',
#                    headers=headers)
#
# assert resp.status_code==200
# resp_dict=json.loads(resp.text)   #json转python中的字典。
# token=resp_dict['object']['token']   #获取token
# print(token)
# headers['token']=token   #把token加到headers_dict里面
# print(headers)
#
# data={'token':token}   #创建一个data的字典，添加了token数据
# data_json=json.dumps(data)  #将python对象转成json
#
# resp1=requests.post(url="http://192.168.1.203:8083/sys/getUserInfo",
#                     proxies=proxies,
#                     data=data_json,
#                     headers=headers)
# # print(resp.text)
# # print(resp.headers)
# # print(resp.cookies)


import requests         #调用requests库
import json      #调用json转换
from common.commonData import CommonData
class HttpUtil:          #创建HttpUtil类
    def __init__(self):
        self.http=requests.session()
        self.headers={'Content-Type':'application/json;charset=utf-8'}
    def post(self,path,data):
        proxies=CommonData.proxies   #获取全局变量proxies
        host=CommonData.host      #获取全局变量的host
        data_json=json.dumps(data)     #把data参数转化为json格式
        if CommonData.token is not None:    #排断token格式是否为空，不为空则复制，为空则不复制
            self.headers['token']=CommonData.token
        resp_login=self.http.post(url=host+path,   #发起post请求
                proxies=proxies,
                data=data_json,
                headers=self.headers)
        print(resp_login)
        assert resp_login.status_code==200   #校验码返回是否200
        resp_json=resp_login.text
        resp_dict=json.loads(resp_json)
        return resp_dict
