from requestscode.base.getYaml import getYml
from requestscode.base.baseapi import baseApi


class GetToken(baseApi):
    def get_access_token(self):
        data = getYml('../data/id.yml')
        corpid = data['corpid']
        corpsecret = data['corpsecret']
        path = data['host'] + data['url'] + data['query'].format(f'{corpid}', f'{corpsecret}')
        r = self.session.request(method=data['method'], url=path)
        if r.status_code == 200:
            # 将access_token放入到session里面
            self.session.params.update({"access_token": r.json()['access_token']})
        return self
