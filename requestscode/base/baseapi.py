import requests


class baseApi:
    def __init__(self):
        self.session = requests.session()

    def sendApi(self, data: dict):
        return self.session.request(**data).json()
