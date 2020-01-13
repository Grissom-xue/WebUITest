from selenium.webdriver.common.by import By


class IndexPageLocator:
    # 免费注册按钮
    register_btn = (By.LINK_TEXT, "免费注册")
    #  请登录按钮
    login_goto_btn = (By.NAME, 'nav-bar-mname')
    # 尊敬的会员
    member_btn = (By.LINK_TEXT, "尊敬的会员")
