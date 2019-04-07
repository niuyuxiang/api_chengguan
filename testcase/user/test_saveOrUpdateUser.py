import pytest
from common.commonData import CommonData
from conftest import http
import random

import allure

@allure.feature("新增用户模块")
class Test_saveOrUpdateUser():
    @allure.story("新增用户成功")
    def test_saveOrUpdateUser(self):
        nickname=str(random.randint(10000000,100000000))
        mobile='139'+nickname
        data={
            'nickName':nickname,
              'userName':mobile,
              "telNo": "",
              "email": "",
              "address": "",
              "roleIds": "",
              "regionId": 1,
              "regionLevel": 1
        }
        resp=http.post('/user/saveOrUpdateUser',data)
        assert resp['code']==200
        assert resp['msg']=='操作成功'
        login_data={'userName':mobile,'password':CommonData.password}
        resp2=http.post('/sys/login',login_data)
        assert resp2['code']==200
        assert resp2['msg']=='操作成功'






