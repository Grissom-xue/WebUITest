from selenium.webdriver.common.by import By


class LoginPageLocator:
    # 用户名输入框
    user_text = (By.ID, 'nloginname')
    # 密码输入框
    passwd_text = (By.ID, 'npwd')
    # 登录按钮
    login_btn = (By.ID, 'nsubmit')