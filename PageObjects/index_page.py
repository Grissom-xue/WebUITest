from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Common.basepage import BasePage
from PageLocators.index_page_locators import IndexPageLocator
from PageLocators.login_page_locators import LoginPageLocator


class IndexPage(BasePage):

    # 进入海外手机登录页面
    def overseas_login_enter(self):
        doc = "首页_进入海外手机登录页面"
        # 等待请登录按钮出现
        self.wait_ele_visible(IndexPageLocator.login_goto_btn, doc=doc)
        # 点击请登录按钮
        self.click_element(IndexPageLocator.login_goto_btn, doc)
        # 等待境外手机按钮出现
        self.wait_ele_visible(LoginPageLocator.overseas_login, doc=doc)
        # 点击境外手机按钮
        self.click_element(LoginPageLocator.overseas_login, doc)

    # 进入注册页面
    def register_enter(self):
        doc = "首页_进入注册页面"
        # 等待免费注册按钮出现
        self.wait_ele_visible(IndexPageLocator.register_btn, doc=doc)
        # 点击免费注册按钮
        self.click_element(IndexPageLocator.register_btn, doc)

    # 判断主页是否存在尊敬的会员按钮
    def is_exist_member_ele(self):
        doc = "首页_判断首页是否存在尊敬的会员按钮"
        try:
            self.wait_ele_visible(IndexPageLocator.member_btn, doc=doc)
            return True
        except:
            return False

# 96