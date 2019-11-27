
class BasePage:
    def __init__(self, driver):
        self.driver = driver

    # 等待元素可见
    def wait_eleVisible(self):
        pass

    def get_element(self):
        pass

    def save_screenshot(self):
        filepath =
        try:
            self.driver.sava_screenshot(filePath)
