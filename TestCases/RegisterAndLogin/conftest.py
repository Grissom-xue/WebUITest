import pytest
from selenium import webdriver
"""
fixture(scope="class")
"""
@pytest.fixture(scope="class")
def access_web():
    #前置条件
    driver = webdriver.Chrome()
    driver.get("https://web.godap.com/login")
    yield
    #后置条件