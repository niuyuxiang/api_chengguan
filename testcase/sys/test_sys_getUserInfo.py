import pytest
from common.commonData import CommonData
from conftest import http

class Test_getUserInfo():
    def test_login_success(self):
        data={
            # "token": "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxNTkzNTE1NzA3MyIsInBhc3N3b3JkIjoiRTEwQURDMzk0OUJBNTlBQkJFNTZFMDU3RjIwRjg4M0UiLCJpZCI6MTMzLCJ1c2VyTmFtZSI6IjE1OTM1MTU3MDczIiwiZXhwIjoxNTU0NjIyMjY3LCJpYXQiOjE1NTQ1MzU4NjcsImp0aSI6ImNmOGRmMjdhLTc0NGQtNGYwZS04NTVmLTQwNDgxMjhkMWYyOCJ9.Qcylc5oEJWnUhstUL_l3dQXhe_8eRRGmx2jQkyjHT9Y"
        }
        resp=http.post('/sys/getUserInfo',data)
        assert resp['code']==200
        assert resp['msg']=='操作成功'
        # assert resp['object']['address']=='taiyuan'