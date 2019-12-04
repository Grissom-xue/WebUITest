import time
import pytest
import unittest
from selenium import webdriver

from TestDatas.RegisterAndLogin import login_datas
from TestDatas import Common_Datas
from PageObjects.login_page import LoginPage


class TestLogin(unittest.TestCase):

    # 前置工作
    def setUp(self):
        # 打开浏览器
        self.driver = webdriver.Chrome()
        # 浏览器最大化
        self.driver.maximize_window()
        # 打开网站首页，URL从公共数据中取出
        self.driver.get(Common_Datas.web_login_url)

    # 后置工作
    def tearDown(self) -> None:
        # case完成之后睡眠两秒钟
        time.sleep(2)
        # 关闭浏览器
        self.driver.quit()

    def test_login_success(self):
        # 前置访问登录页面
        # 步骤 输入用户名密码
        lg = LoginPage(self.driver)
        lg.login(login_datas.success_data["user"], login_datas.success_data["passwd"])
        # 断言 首页当中能否找到退出这个元素
        # self.assertEqual()

    def test_login_user_wrongFormat(self):
        pass

if __name__ == '__main__':
    pass
