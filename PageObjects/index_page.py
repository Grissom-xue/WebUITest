from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class IndexPage:
    def __init__(self, driver):
        self.driver = driver

    # 进入登录页面
    def login_enter(self):
        login_goto_btn = "nav-bar-mname"
        # 点击请登陆
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.NAME, login_goto_btn)))
        self.driver.find_element_by_name(login_goto_btn).click()

    # 进入注册页面
    def register_enter(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.LINK_TEXT, "免费注册")))
        self.driver.find_element_by_link_text("免费注册").click()

    # 判断主页是否存在退出按钮
    def is_exit_logout_ele(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "sss")))
            return True
        except:
            return False

# 96