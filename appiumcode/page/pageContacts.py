from appiumcode.page.basepage import baseView
from appiumcode.page.pageMemberInvite import PageMemberInvite


# 通讯录页面
class PageContacts(baseView):

    # 点击添加联系人
    def addContacts(self, attribute):
        self.xpath_click(attribute)
        return PageMemberInvite(self.driver)
