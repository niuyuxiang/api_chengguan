# import pytest
#
# @pytest.fixture()   #自定义用例
# def my_fixtures():
#     print("自定义 start")
#     yield
#     print("自定义 end")
#
# @pytest.mark.usefixtures('my_fixtures')   #执行特定用例
# def test_first():
#     print("我的第一个测试")
#     assert 1==1
#
# def test_two():
#     print("我的第二个测试")
#     assert 2==2
#
# def test_four():
#     print("这是第三个")
#     b=[1,2,3]
#     assert 3 in b
#
# if __name__=='__main__':
#     pytest.main(['-s'])
#
# #
# # @pytest.mark.usefixtures("my_fixtures")  #自定义
# # def test_three():
# #     print("第二个")
# #     assert 'a' in 'ab'

