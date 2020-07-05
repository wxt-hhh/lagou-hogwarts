import pytest

from pytestcode.base import get_yaml
from pytestcode.calculator import Calculator


@pytest.fixture(scope='class', autouse=True)
def start_cal():
    print('开始计算')
    yield Calculator()
    print('结束计算')
