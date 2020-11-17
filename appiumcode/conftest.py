from typing import List
import pytest
from appiumcode.desired_caps import appiumStart
from appiumcode.getYML import get_yaml

# 自定义hook函数，pytest_collection_modifyitems，可以将收集上来的测试用例进行改写
# 控制用例执行顺序，自动添加标签，解决测试用例编码问题


def pytest_collection_modifyitems(session: "Session", config: "Config", items: List["Item"]):
    # items.reverse()
    # items 就是所有测试用例列表， item代表每个测试用例对象
    for item in items:
        """
        解决@pytest.mark.parametrize(ids=['零', '负数', '正数']) 中文编码问题
        """
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')

        # 添加自定义标签
        if 'add' in item.nodeid:
            item.add_marker(pytest.mark.add)
        elif 'div' in item.nodeid:
            item.add_marker(pytest.mark.div)


@pytest.fixture(scope="class", autouse=True)
def setup_class():
    data = get_yaml('devices.yml')
    appiumStart(data)


@pytest.fixture(scope="class", autouse=True)
def teardown_class():
    print('----------')
