# import pytest
#
# @pytest.fixture()
# def my_fixtures():
#     print("spec start")
#     yield
#     print("spec end")
#
# class Test_class:
#     def test_first(this):
#         print("我的第一个测试")
#         assert 1==1
#
#     def test_two(this):
#         print("我的第二个测试")
#         assert 2==2
#
#     @pytest.mark.debug    #执行特别用例
#     @pytest.mark.usefixtures("my_fixtures")   #执行自定义用例
#     def test_three(this):
#         print("第三个测试用例")
#         assert 'a' in 'ab'
#
#     def test_four(this):
#         print("这是第四个")
#         b=[1,2,3]
#         assert 3 in b