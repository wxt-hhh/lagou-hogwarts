import pytest
from pytestcode.base import get_yaml


@pytest.mark.parametrize("data", get_yaml('cal.yml'), ids=['零', '负数', '正数'])
class TestCal:
    @pytest.mark.add
    def test_add(self, data, start_cal):
        assert data['add'] == start_cal.add(data['a'], data['b'])

    @pytest.mark.sub
    def test_sub(self, data, start_cal):
        assert data['sub'] == start_cal.sub(data['a'], data['b'])

    @pytest.mark.mul
    def test_mul(self, data, start_cal):
        assert data['mul'] == start_cal.mul(data['a'], data['b'])

    @pytest.mark.div
    def test_div(self, data, start_cal):
        # 判断b是否为0，如果为0打印异常
        if data['b'] == 0:
            raise ZeroDivisionError
        else:
            assert data['div'] == start_cal.div(data['a'], data['b'])
