from appium import webdriver


def appiumStart(data):
    desired_caps = {}
    desired_caps['platformName'] = data['platformName']
    desired_caps['platformVersion'] = data['platformVersion']
    desired_caps['deviceName'] = data['deviceName']
    desired_caps['appPackage'] = data['appPackage']
    desired_caps['appActivity'] = data['appActivity']
    desired_caps['noReset'] = data['noReset']
    driver = webdriver.Remote(data['host'], desired_caps)
    driver.implicitly_wait(10)

# appiumStart()
