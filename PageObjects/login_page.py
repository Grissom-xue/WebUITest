from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def login(self, username, passwd):
        user_text = 'nloginname'
        passwd_text = 'npwd'
        login_btn = 'nsubmit'
        # 输入邮箱
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.ID, user_text)))
        self.driver.find_element_by_id(user_text).send_keys(username)
        # 输入密码
        self.driver.find_element_by_id(passwd_text).send_keys(passwd)
        # 点击登陆
        self.driver.find_element_by_id(login_btn).click()

    def register(self, username, passwd):
        # 点击免费注册按钮
        # 点击新用户注册
        # 输入邮箱
        # 输入密码
        # 输入确认密码
        pass

    def get_errorMsg(self):
        pass