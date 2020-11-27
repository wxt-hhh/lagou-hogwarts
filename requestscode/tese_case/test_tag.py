import pytest
from requestscode.page.get_token import GetToken
from requestscode.base.getYaml import getYml
import allure


@allure.feature('测试标签相关功能')
class TestTag:
    def setup_class(self):
        self.token = GetToken().get_access_token()
        print('开始测试')

    def teardown_class(self):
        print('测试结束')

    @allure.story('添加标签')
    @pytest.mark.parametrize('data', getYml('../data/add_tag.yml'), ids=['添加标签'])
    def test_add_tag(self, data):
        res = self.token.sendApi(data)
        pytest.assume(res['errcode'] == 0)
        pytest.assume(res['errmsg'] == 'created')
        pytest.assume(res['tagid'] == data['json']['tagid'])

    @allure.story('获取标签列表')
    @pytest.mark.parametrize('data', getYml('../data/get_taglist.yml'), ids=['获取标签列表'])
    def test_get_taglist(self, data):
        res = self.token.sendApi(data)
        pytest.assume(res['errcode'] == 0)
        pytest.assume(res['errmsg'] == 'ok')
        pytest.assume(res['taglist'] is not None)

    @allure.story('更新标签')
    @pytest.mark.parametrize('data', getYml('../data/update_tag.yml'), ids=['更新标签'])
    def test_update_tag(self, data):
        res = self.token.sendApi(data)
        pytest.assume(res['errcode'] == 0)
        pytest.assume(res['errmsg'] == 'updated')

    @allure.story('删除标签')
    @pytest.mark.parametrize('data', getYml('../data/del_tag.yml'), ids=['删除标签'])
    def test_del_tag(self, data):
        res = self.token.sendApi(data)
        pytest.assume(res['errcode'] == 0)
        pytest.assume(res['errmsg'] == 'deleted')



