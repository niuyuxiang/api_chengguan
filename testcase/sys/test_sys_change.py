import pytest
import allure
from common.commonData import CommonData
from conftest import http

@allure.feature("修改密码模块")
class Test_login_change(object):

    @allure.story("修改密码成功")
    # @pytest.mark.usefixtures('recoveryPwd')
    def test_password_change(self):
        data={'userId':133,
            'userName':CommonData.mobile,
              'oldPwd':CommonData.password,
              'password':'654321'
              }
        resp=http.post('/sys/changePwd',data)
        assert resp['code']==200
        assert resp['msg']=='操作成功'
    def test_password_change1(self):
        data={'userId':133,
            'userName':CommonData.mobile,
            'oldPwd':'654321',
            'password':CommonData.password
            }
        resp=http.post('/sys/changePwd',data)
        assert resp['code']==200
        assert resp['msg']=='操作成功'


