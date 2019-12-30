from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageLocators.login_page_locators import LoginPageLocator
from Common.basepage import BasePage


class LoginPage(BasePage):

    def login(self, username, passwd):
        doc = "登陆页面_登陆功能"
        # 等待元素出现
        self.wait_ele_visible(LoginPageLocator.user_text, doc)
        # 输入用户名
        self.input_text(LoginPageLocator.user_text, username, doc)
        # 输入密码
        self.input_text(LoginPageLocator.passwd_text, passwd, doc)
        # 点击登录
        self.click_element(LoginPageLocator.login_btn, doc)

    def register(self, username, passwd):
        # 点击免费注册按钮
        # 点击新用户注册
        # 输入邮箱
        # 输入密码
        # 输入确认密码
        pass

    def get_error_msg(self):
        pass
