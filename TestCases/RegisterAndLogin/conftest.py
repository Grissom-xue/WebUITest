import pytest
from selenium import webdriver

from PageObjects.index_page import IndexPage
from TestDatas import Common_Datas
from PageObjects.login_page import LoginPage


driver = None


@pytest.fixture(scope="class")
def access_web():
    global driver
    # 前置条件[打开浏览器-->获取网页地址--》获取page对象]
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(Common_Datas.web_login_url)
    indexpage = IndexPage(driver)
    loginpage = LoginPage(driver)
    yield (driver, loginpage, indexpage)  # 用来return返回值
    # 后置条件【关闭浏览器】
    driver.quit()


@pytest.fixture()
def refresh_page():
    global driver
    yield
    # 刷新操作
    driver.refresh()
