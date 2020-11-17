from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.webdriver import WebDriver


class baseView():

    def __init__(self, driver: None):
        self.driver = driver

    def find_id(self, attribute):
        return self.driver.find_element_by_id(*attribute)

    def find_xpath(self, attribute):
        return self.driver

    def id_click(self, attribute):
        return self.find_id(*attribute).click()

    def xpath_click(self, attribute):
        return self.find_xpath(attribute).click()

    def id_sendkeys(self, attribute, text):
        self.id_click(attribute).clear()
        return self.id_click(attribute).send_keys(text)

    def xpath_sendkeys(self, attribute, text):
        self.xpath_click(attribute)
        return self.xpath_click(attribute).send_keys(text)

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

