import pytest
from pytestcode.base import get_yaml


# 调用cmdoption读取环境
def test_env(cmdoption):
    print(f'{cmdoption}')


@pytest.mark.parametrize("data", get_yaml('cal.yml'), ids=['零', '负数', '正数'])
class Test_Cal:
    @pytest.mark.run(order=4)
    @pytest.mark.dependency(depends=['mul'])
    def test_div(self, data, start_cal):
        # 判断b是否为0，如果为0打印异常
        if data['b'] == 0:
            print(ZeroDivisionError)
        else:
            assert data['div'] == start_cal.div(data['a'], data['b'])

    @pytest.mark.run(order=1)
    @pytest.mark.dependency(name='add')
    def test_add(self, data, start_cal):
        assert data['add'] == start_cal.add(data['a'], data['b'])
        # 验证与sub测试用例的依赖关系，如果add失败则不会执行sub
        # assert 1 == start_cal.add(data['a'], data['b'])

    @pytest.mark.run(order=3)
    @pytest.mark.dependency(name='mul')
    def test_mul(self, data, start_cal):
        assert data['mul'] == start_cal.mul(data['a'], data['b'])
        # 验证与div测试用例的依赖关系，如果mul失败则不会执行div
        # assert 1 == start_cal.add(data['a'], data['b'])

    @pytest.mark.run(order=2)
    @pytest.mark.dependency(depends=['add'])
    def test_sub(self, data, start_cal):
        assert data['sub'] == start_cal.sub(data['a'], data['b'])
