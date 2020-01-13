import pytest

from PageObjects.index_page import IndexPage
from TestDatas.RegisterAndLogin import login_datas


@pytest.mark.usefixtures("access_web")
@pytest.mark.usefixtures("refresh_page")
@pytest.mark.login
class TestLogin(object):

    # 测试登录成功
    @pytest.mark.somke
    def test_login_success(self, access_web):
        # 进入海外手机登录页面
        access_web[2].overseas_login_enter()
        # 输入用户名密码
        access_web[1].overseas_login(login_datas.success_data["user"], login_datas.success_data["passwd"])
        # 断言 首页当中能否找到尊敬的会员这个元素
        assert IndexPage(access_web[0]).is_exist_member_ele()

    # 测试用户名或者密码错误
    def test_login_user_wrong_format(self):
        pass

    # 测试用户名为空
    def test_login_no_user(self):
        pass

    # 测试密码为空
    def test_login_no_password(self):
        pass



if __name__ == '__main__':
    pass
