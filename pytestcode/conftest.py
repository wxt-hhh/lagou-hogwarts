import pytest

from pytestcode.calculator import Calculator


@pytest.fixture(scope='class')
def start_cal():
    print('开始计算')
    yield Calculator()
    print('结束计算')
