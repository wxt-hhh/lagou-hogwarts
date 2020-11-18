from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.webdriver import WebDriver

"""
用来存放一些最基本的操作
1.实例化driver对象
2.find 方法
3.appium底层操作
"""


class baseView:
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find_id(self, attribute):
        return self.driver.find_element_by_id(attribute)

    def find_xpath(self, attribute):
        return self.driver.find_element_by_xpath(attribute)

    def id_click(self, attribute):
        return self.find_id(*attribute).click()

    def xpath_click(self, attribute):
        return self.find_xpath(attribute).click()

    def id_sendkeys(self, attribute, text):
        self.find_id(attribute).clear()
        return self.find_id(attribute).send_keys(text)

    def xpath_sendkeys(self, attribute, text):
        self.find_xpath(attribute).clear()
        return self.find_xpath(attribute).send_keys(text)

    def id_wait(self, attribute, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(self.find_id(attribute))
        except Exception as e:
            return e

    def xpath_wait(self, attribute, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(self.find_xpath(attribute))
        except Exception as e:
            return e

    def getText(self, attribute):
        return self.find_xpath(attribute).text

    # 获取toast
    def getToast(self):
        return self.find_xpath("//*[@class='android.widget.Toast']").text

    def appBack(self, num=1):
        for i in range(num):
            self.driver.back()
        return self
