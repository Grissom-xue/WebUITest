from PageLocators.login_page_locators import LoginPageLocator
from Common.basepage import BasePage


class LoginPage(BasePage):

    def overseas_login(self, username, passwd):
        doc = "登陆页面_登陆功能"
        # 等待海外手机号的用户名输入框出现
        self.wait_ele_visible(LoginPageLocator.overseas_user_text, doc=doc)
        # 选择美国国家码
        self.click_element(LoginPageLocator.overseas_country_code_choose, doc)
        self.wait_ele_visible(LoginPageLocator.overseas_country_code_US, doc=doc)
        self.click_element(LoginPageLocator.overseas_country_code_US, doc)
        # 输入用户名
        self.input_text(LoginPageLocator.overseas_user_text, username, doc)
        # 输入密码
        self.input_text(LoginPageLocator.overseas_passwd_text, passwd, doc)
        # 点击登录
        self.click_element(LoginPageLocator.overseas_login_btn, doc)

    def register(self, username, passwd):
        # 点击免费注册按钮
        # 点击新用户注册
        # 输入邮箱
        # 输入密码
        # 输入确认密码
        pass

    def get_error_msg(self):
        pass
