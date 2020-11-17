import pytest
from appiumcode.base import baseView
from appiumcode.desired_caps import appiumStart
from appiumcode.getYML import get_yaml


@pytest.fixture(scope="class", autouse=True)
class WeChat(baseView):
    def setup_class(self):
        data = get_yaml('devices.yml')
        appiumStart(data)

    def teardown_class(self):
        self.driver.quit()
