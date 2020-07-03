import pytest
from pytestcode.base import get_yaml


@pytest.mark.parametrize("data", get_yaml('cal.yml'))
class TestCal:
    def test_add(self, start_cal, data):
        a = data['a']
        b = data['b']
        assert a + b == start_cal.add(a, b)

    @pytest.mark.sub
    def test_sub(self, start_cal, data):
        a = data['a']
        b = data['b']
        assert a - b == start_cal.sub(a, b)

    @pytest.mark.mul
    def test_mul(self, start_cal, data):
        a = data['a']
        b = data['b']
        assert a * b == start_cal.mul(a, b)

    @pytest.mark.div
    def test_div(self, start_cal, data):
        a = data['a']
        b = data['b']
        # 尝试捕捉b是否为0，如果为0则抛出异常
        try:
            b == 0
        except ZeroDivisionError as e:
            print(e)
        else:
            assert a / b == start_cal.div(a, b)
