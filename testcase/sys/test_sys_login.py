import pytest
import allure
from common.commonData import CommonData
from conftest import http

@allure.feature("登录模块")
class Test_login():

    @allure.story("登录成功")
    def test_login_success(self):
        data={'userName':CommonData.mobile,
                'password':CommonData.password
        }
        resp=http.post('/sys/login',data)
        assert resp['code']==200
        assert resp['msg']=='操作成功'
        # assert resp['object']['userId']==133
    def test_login_fail(self):
        data={'userName':CommonData.mobile,
              'password':'1234567890'
              }
        resp=http.post('/sys/login',data)
        assert resp['code']==410
        assert resp['msg']=='用户名或密码错误'
    def test_login_fail2(self):
        data={'userName':'123333333333334',
              'password':CommonData.password
        }
        resp=http.post('/sys/login',data)
        assert resp['code']==301
        assert resp['msg']=='用户不存在'
    def test_login_fail3(self):
        data={'userName':'',
             'password':CommonData.password
        }
        resp=http.post('/sys/login',data)
        assert resp['code']==3010
        assert resp['msg']=='此账户禁止登录'
    def test_login_fail4(self):
        data={
             'password':CommonData.password
        }
        resp=http.post('/sys/login',data)
        assert resp['code']==301