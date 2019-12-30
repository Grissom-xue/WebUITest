import os
import logging
from datetime import datetime

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Common import dir_config


# 封装基本函数- 执行日志/异常处理/失败截图
# 页面公共部分


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def wait_ele_visible(self, locator, timeout=15, poll_frequency=0.5, doc=""):
        """
        等待元素可见
        @param locator: 元素定位，元祖
        @param timeout: 等待超时时间
        @param poll_frequency: 产找的频率
        @param doc: 模块名_页面名称_操作名称
        """
        logging.info("等待元素{0} 可见".format(locator))
        try:
            # 开始等待时间
            start_time = datetime.now()
            WebDriverWait(self.driver, timeout, poll_frequency).until(EC.visibility_of_element_located(locator))
            # 结束时间
            end_time = datetime.now()
            # 耗时
            consume_time = end_time-start_time
            logging.info("等待结束，一共耗时：{0} ".format(consume_time))
        except:
            logging.exception("元素等待失败！")
            self.save_screenshot(doc)
            raise

    # 等待元素存在
    def wait_ele_presence(self):
        pass

    # 查找元素
    def get_element(self, locator, doc=""):
        logging.info("查找元素：{}".format(locator))
        try:
            return self.driver.find_element(*locator)
        except:
            logging.exception("查找元素失败！")
            self.save_screenshot(doc)
            raise

    # 点击操作
    def click_element(self, locator, doc):
        ele = self.get_element(locator, doc)
        try:
            ele.click()
        except:
            logging.exception("点击失败！")
            self.save_screenshot(doc)
            raise

    # 输入文本
    def input_text(self, locator, text, doc=""):
        ele = self.get_element(locator, doc)
        try:
            ele.input(text)
        except:
            logging.exception("输入文本失败！")
            self.save_screenshot(doc)
            raise

    # 获取元素的文本内容
    def get_text(self, locator, doc=""):
        ele = self.get_element(locator, doc)
        try:
            return ele.text
        except:
            logging.exception("获取元素文本失败！")
            self.save_screenshot(doc)
            raise

    # 获取元素属性
    def get_ele_attribute(self, locator, attr, doc=""):
        ele = self.get_element(locator, doc)
        try:
            return ele.get_attribute(locator, doc)
        except:
            logging.exception("获取元素属性失败！")
            self.save_screenshot(doc)
            raise

    # alert 处理
    def alert_action(self):
        pass

    # iframe 切换
    def switch_iframe(self, iframe_reference):
        pass

    # 上传操作
    def upload_file(self):
        pass

    # 截图操作
    def save_screenshot(self, name):
        # 图片名称：页面名称_模块名称_操作名称_秒级时间.png
        file_path = dir_config.screenshot_dir + name
        self.driver.save_screenshot(file_path)
        logging.info("截取网页成功。文件路径为")
