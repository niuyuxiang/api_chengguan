import pytest
from common.commonData import CommonData
from conftest import http
import allure

@allure.feature("用户信息列表显示模块")
class Test_save():
    def test_login_success(self):
        data={'pageSize':'30',
              'pageCurrent':'1',
              'nickname':'yxyyx',
              'username':'13593327122',
              }
        resp=http.post('/user/loadUserList',data)
        assert resp['code']==200
        assert resp['msg']=='操作成功'