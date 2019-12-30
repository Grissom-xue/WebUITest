import time
import unittest
from selenium import webdriver

from PageObjects.index_page import IndexPage
from TestDatas.RegisterAndLogin import login_datas
from TestDatas import Common_Datas
from PageObjects.login_page import LoginPage


class TestLogin(unittest.TestCase):

    # 所有case执行之前执行一次
    def setUpClass(self) -> None:
        # 打开浏览器
        self.driver = webdriver.Chrome()
        # 浏览器最大化
        self.driver.maximize_window()
        # 打开网站首页，URL从公共数据中取出
        self.driver.get(Common_Datas.web_login_url)

    # 每个用例执行前执行一次
    def setUp(self):
        self.lg = LoginPage(self.driver)

    # 每个用例执行之后执行一次
    def tearDown(self) -> None:
        # case完成之后睡眠两秒钟
        time.sleep(2)
        # 关闭浏览器
        self.driver.refresh()

    # 所有用例执行之后执行关闭浏览器
    def tearDownClass(self) -> None:
        self.driver.quit()

    # 测试登录成功
    def test_login_success(self):
        # 步骤 输入用户名密码
        self.lg.login(login_datas.success_data["user"], login_datas.success_data["passwd"])
        # 断言 首页当中能否找到退出这个元素
        self.assertTrue(IndexPage(self.driver).is_exit_logout_ele())

    # 测试用户名或者密码错误
    def test_login_user_wrongFormat(self):
        pass

    # 测试用户名为空
    def test_login_noUser(self):
        pass

    # 测试密码为空
    def test_login_noPassword(self):

        pass



if __name__ == '__main__':
    pass
