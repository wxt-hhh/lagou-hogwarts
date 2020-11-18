from appium import webdriver
from appiumcode.page.pageMain import PageMain
from appium.webdriver.webdriver import WebDriver
from appiumcode.page.basepage import baseView


class App(baseView):
    driver: WebDriver

    def appStart(self, data):
        if self.driver == None:
            desired_caps = {}
            desired_caps['platformName'] = data['platformName']
            desired_caps['platformVersion'] = data['platformVersion']
            desired_caps['deviceName'] = data['deviceName']
            desired_caps['appPackage'] = data['appPackage']
            desired_caps['appActivity'] = data['appActivity']
            desired_caps['noReset'] = data['noReset']
            desired_caps['unicodeKeyboard'] = data['unicodeKeyboard']
            desired_caps['resetKeyboard'] = data['resetKeyboard']
            self.driver = webdriver.Remote(data['host'], desired_caps)
        else:
            # 如果应用在后台，执行打开操作；启动的是desired_caps里面定义的 activity
            # 等同于 adb shell am start -n 包名/activity
            self.driver.launch_app()
        self.driver.implicitly_wait(10)
        return self

    def appRestart(self):
        pass

    def appClosed(self):
        self.driver.quit()

    def appMain(self):
        return PageMain(self.driver)
