import pytest
from TestDatas.RegisterAndLogin import login_datas
from TestDatas import Common_Datas
from PageObjects.login_page import LoginPage
from selenium import webdriver
# @pytest.mark.usefixtures("access_web")
# @pytest.mark.usefixtures("refresh_page")
class TestLogin:

    # fixture的函数名称用来接收它的返回值，返回值是一个元组
    # @pytest.mark.smoke
    # def test_login_success(self, access_web):
        # access_web[1] = (loginPage = LoginPage(driver))
        # access_web[0] = driver
        # access_web[1].login(login_datas.success_data["user"], login_datas.success_data["passwd"])
        # assert

    # @pytest.mark.usefixtures("setUp")
    def test_login_success(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(Common_Datas.web_login_url)
        lg = LoginPage(driver)
        lg.login(login_datas.success_data["user"], login_datas.success_data["passwd"])

