from appiumcode.page.basepage import baseView


# 添加成员们页面
class PageMemberInvite(baseView):

    # 点击手动添加
    def menualContacts(self, attribute):
        from appiumcode.page.pageAddContacts import pageAddContacts
        self.xpath_click(attribute)
        return pageAddContacts(self.driver)
