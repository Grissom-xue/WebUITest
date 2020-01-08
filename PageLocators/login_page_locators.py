from selenium.webdriver.common.by import By


class LoginPageLocator:
    # 用户名输入框
    user_text = (By.ID, 'nloginname')
    # 密码输入框
    passwd_text = (By.ID, 'npwd')
    # 登录按钮
    login_btn = (By.ID, 'nsubmit')
    # 境外手机登录入口按钮
    overseas_login = (By.ID, 'overseas_login')

    # 海外手机国家码选择框
    overseas_country_code_choose = (By.ID, 'overcode')
    # 海外手机国家码-美国
    overseas_country_code_US = (By.LINK_TEXT, '美国')
    # 海外手机用户名输入框
    overseas_user_text = (By.ID, 'overphone')
    # 海外手机密码输入框
    overseas_passwd_text = (By.ID, 'overpwd')
    # 海外手机登录按钮
    overseas_login_btn = (By.ID, 'oversubmit')
