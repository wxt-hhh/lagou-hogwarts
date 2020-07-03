from appium import webdriver


def appium():
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '10'
    desired_caps['deviceName'] = '30a4c252'
    desired_caps['appPackage'] = 'com.android.settings'
    desired_caps['appActivity'] = 'com.android.settings.Settings'
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
    driver.quit()


appium()
