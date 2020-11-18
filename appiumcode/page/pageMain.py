from appiumcode.page.basepage import baseView
from appiumcode.page.pageContacts import PageContacts


# app首页
class PageMain(baseView):

    # 点击通讯录
    def contactActivity(self, attribute):
        self.xpath_click(attribute)
        return PageContacts(self.driver)
