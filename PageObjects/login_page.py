from Common.basepage import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, passwd):
        pass