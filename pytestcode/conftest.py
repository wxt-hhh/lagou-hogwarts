from typing import List
import pytest

from pytestcode.base import get_yaml
from pytestcode.calculator import Calculator


@pytest.fixture(scope='class', autouse=True)
def start_cal():
    print('开始计算')
    yield Calculator()
    print('结束计算')


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


# def pytest_addoption(parser):
#     mygroup = parser.getgroup("title")
#     mygroup.addoption(
#         "--env",  # 注册一个命令行选项
#         default='test',
#         dest='env',
#         help='set your run env'
#     )


@pytest.fixture(scope='session')
def cmdoption(request):
    """
    自定义命令行参数，完成数据化逻辑处理
    """
    global env_data
    myenv = request.config.getoption("--env", default='st')
    if myenv == 'test':
        print("获取测试数据")
        env_data = get_yaml('datas/test.yml')
    elif myenv == 'dev':
        print('获取dev数据')
        env_data = get_yaml('datas/dev.yml')
    elif myenv == 'st':
        print('获取st数据')
        env_data = get_yaml('datas/st.yml')
    return env_data

# def pytest_generate_tests(metafunc:"Metafunc") -> None:
#     """
#     可以实现自定义动态参数化方案或者扩展
#     """
#     if "param" in metafunc.fixturenames:
#         metafunc.parametrize("param", metafunc.module.par_to_test, ids=metafunc.module.case, scope="function")
