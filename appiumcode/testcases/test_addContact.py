import pytest
from appiumcode.base.getYML import get_yaml
from appiumcode.base.app import App


class TestAddContacts:
    data = get_yaml('../datas/devices.yml')

    def setup_class(self,):
        self.app = App()
        # 这里读设备写的有问题，需要再想想
        for i in range(len(self.data)):
            self.main = self.app.appStart(self.data[i]).appMain()

    def teardown_class(self):
        print('测试结束')
        self.app.appClosed()

    @pytest.mark.parametrize('name, phone', get_yaml('../datas/testData.yml')['add'],ids=['添加联系人', '添加第二个联系人'])
    def test_addcontact(self, name, phone):
        """
        1.打开企业微信
        2.点击通讯录
        3.点击添加成员
        4.点击手动输入添加
        5.输入必填信息
        6.点击保存
        7.验证添加成功
        """
        newname = self.main.contactActivity("//android.widget.TextView[@text='通讯录']")\
        .addContacts("//*[@text='添加成员']").menualContacts("//*[@text='手动输入添加']")\
        .usernameEdit("//*[@text='必填']", name)\
        .genderEdit("//*[@resource-id='com.tencent.wework:id/b5v']", "//*[@text='女']", "//*[@text='男']")\
        .phoneEdit("//*[@text='手机号']", phone).saveClick("//*[@text='保存']").appBack().getText(f"//*[@text='{name}']")

        print(newname)
        assert newname == f'{name}'

