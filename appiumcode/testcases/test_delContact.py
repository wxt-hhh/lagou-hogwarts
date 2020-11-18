import pytest
from appiumcode.base.getYML import get_yaml


@pytest.mark.parametrize('name, phone', get_yaml('testData.yml')['del'],
                         ids=['删除联系人'])
def test_addcontact(name, phone, devices):
    """
    1.打开企业微信
    2.点击通讯录
    3.点击被删除的联系人
    4.点击编辑成员
    5.点击删除成员
    6.点击确定
    7.验证删除成功
    """
    print(name)
    print(phone)
