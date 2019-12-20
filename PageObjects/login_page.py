from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from  PageLocators.login_page_locators import LoginPageLocator

class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def login(self, username, passwd):
        # user_text = 'nloginname'
        # passwd_text = 'npwd'
        # login_btn = 'nsubmit'
        # # 输入邮箱
        # WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.ID, user_text)))
        # self.driver.find_element_by_id(user_text).send_keys(username)
        # # 输入密码
        # self.driver.find_element_by_id(passwd_text).send_keys(passwd)
        # # 点击登陆
        # self.driver.find_element_by_id(login_btn).click()
        # 通过将元素定位封装到单独的文件中去，实现定位元素的复用
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(*LoginPageLocator.user_text))
        # 输入用户名
        self.driver.find_element(*LoginPageLocator.user_text).send_keys(username)
        # 输入密码
        self.driver.find_element(*LoginPageLocator.passwd_text).send_keys(passwd)
        # 点击登录
        self.driver.find_element(*LoginPageLocator.login_btn).click()

    def register(self, username, passwd):
        # 点击免费注册按钮
        # 点击新用户注册
        # 输入邮箱
        # 输入密码
        # 输入确认密码
        pass

    def get_errorMsg(self):
        pass
    # iOS.a80f9bcca3611108a7c221ccb95c8ed9.dttalk