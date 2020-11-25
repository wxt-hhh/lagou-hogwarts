import requests
from requestscode.getYaml import getYml
import pytest


class TestWework:
    # 创建一个session对象
    session = requests.session()

    @pytest.mark.parametrize('data', getYml('./data/id.yml'), ids=['获取access_token'])
    def test_get_access_token(self, data):
        corpid = data['corpid']
        corpsecret = data['corpsecret']
        path = data['host'] + data['url'] + data['query'].format(f'{corpid}', f'{corpsecret}')
        r = self.session.request(method=data['method'], url=path)
        if r.status_code == 200:
            print(r.json()['access_token'])
            # 将access_token放入到session里面
            self.session.params.update({"access_token": r.json()['access_token']})
        else:
            print(f'获取token失败：{r.text}')
        pytest.assume(r.status_code == 200)
        pytest.assume(r.json()['errcode'] == 0)
        pytest.assume(r.json()['errmsg'] == 'ok')

    @pytest.mark.parametrize('data', getYml('./data/add.yml'), ids=['添加联系人'])
    def test_add_contacts(self, data):
        new_data = {
            "userid": data["userid"],
            "name": data["name"],
            "mobile": data["mobile"],
            "department": data["department"]
        }
        path = data['host'] + data['url']
        r = self.session.request(method=data['method'], url=path, json=new_data)
        if r.json()['errcode'] == 0:
            # 将userid放入到session里面
            self.session.params.update({"userid": data['userid']})
        else:
            print(f'创建联系人失败{r.text}')
        pytest.assume(r.status_code == 200)
        pytest.assume(r.json()['errcode'] == 0)
        pytest.assume('created' in r.json()['errmsg'])

    @pytest.mark.parametrize('data', getYml('./data/get.yml'), ids=['查询联系人'])
    def test_get_contacts(self, data):
        path = data['host'] + data['url']
        r = self.session.request(method=data['method'], url=path)
        if r.json()['errcode'] == 0:
            print(f'查询到联系人{r.json()["name"]}')
        else:
            print(f'没有查到联系人{r.text}')
        pytest.assume(r.status_code == 200)
        pytest.assume(r.json()['errcode'] == 0)
        pytest.assume(r.json()['errmsg'] == 'ok')

    @pytest.mark.parametrize('data', getYml('./data/update.yml'), ids=['修改联系人'])
    def test_update_contacts(self, data):
        new_data = {
            "userid": data['userid'],
            "name": data['name']
        }
        path = data['host'] + data['url']
        r = self.session.request(method=data['method'], url=path, json=new_data)
        if r.json()['errcode'] == 0:
            print('修改联系人姓名成功')
        else:
            print(f'未修改成功{r.text}')
        pytest.assume(r.status_code == 200)
        pytest.assume(r.json()['errcode'] == 0)
        pytest.assume(r.json()['errmsg'] == 'updated')

    @pytest.mark.parametrize('data', getYml('./data/del.yml'), ids=['删除联系人'])
    def test_del_contacts(self, data):
        path = data['host'] + data['url']
        r = self.session.request(method=data['method'], url=path)
        if r.json()['errcode'] == 0:
            print('删除练习人成功')
        else:
            print(f'未能删除联系人{r.text}')
        pytest.assume(r.status_code == 200)
        pytest.assume(r.json()['errcode'] == 0)
        pytest.assume(r.json()['errmsg'] == 'deleted')
