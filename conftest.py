# import pytest
# import requests
# import json
#
# http=requests.session()
#
# @pytest.fixture(scope='session',autouse='True')    #全局变量
# def session_fisture():
#     proxies={'http':'http://localhost:8888'}
#     # headers={'Content-Type':'application/json;charset=utf-8'}
#     headers={}
#     headers['Content-Type']='application/json;charset=utf-8'
#
#     resp_login=requests.post(url="http://192.168.1.203:8083/sys/login",
#                        proxies=proxies,
#                        data='{"userName":"18210034706","password":"123456"}',
#                        headers=headers)
#
#     resp_dict=json.loads(resp_login.text)   #json转python中的字典
#     token=resp_dict['object']['token']   #获取token
#
#     assert resp_login.status_code==200
#     print("登录成功")
#     yield
#     headers['token']=token   #把token加到headers_dict里面
#     data={'token':token}   #创建一个data的字典，添加了token数据
#     data_json=json.dumps(data)  #将python对象转成json
#
#     resp_quit=requests.post(url="http://192.168.1.203:8083/sys/logout",
#                              proxies=proxies,
#                              data=None,
#                              headers=headers)
#     assert resp_quit.status_code==200



# @pytest.fixture(scope='module',autouse='True')
# def module_fisture():
#     print("module……")
#
# @pytest.fixture(scope='class',autouse='True')
# def class_fisture():
#     print("class……")
# #
# @pytest.fixture(scope='function',autouse='True')
# def function_fisture():
#     print("function……")

# @pytest.fixture(scope='session',autouse='False')
# def session_fisture():
#     print("登录成功……")

# @pytest.fixture(scope='module',autouse='False')
# def module_fisture():
#     print("module……")

# import pytest
# from util.httpUtil import HttpUtil
# from common.commonData import CommonData
# http=HttpUtil()
#
# @pytest.fixture(scope='session',autouse='True')    #全局变量
# def session_fixture():
#     path="/sys/login"
#     data={'userName':CommonData.mobile,
#           'password':CommonData.password
#           }
#     resp_login=http.post(path,data)
#     CommonData.token=resp_login['object']['token']
    # yield
    # headers['token']=token
    # resp_login=resp_login.post(url="http://192.168.1.203:8083/sys/login",
    #                            proxies=proxies,
    #                            data='{"userName":"18210034706","password":"123456"}',
    #                            headers=headers)
    # assert resp.status_code==200


import pytest
from util.httpUtil import HttpUtil
from common.commonData import CommonData
http=HttpUtil()

@pytest.fixture(scope='session',autouse='True')    #全局变量
def session_fixture():
    path="/sys/login"
    data={'userName':CommonData.mobile,
          'password':CommonData.password
          }
    resp_login=http.post(path,data)
    CommonData.token=resp_login['object']['token']