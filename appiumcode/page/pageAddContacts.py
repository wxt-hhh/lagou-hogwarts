from appiumcode.page.basepage import baseView
import time


# 成员编辑页面
class pageAddContacts(baseView):

    # 编辑用户名
    def usernameEdit(self, attribute, text):
        self.xpath_sendkeys(attribute, text)
        return self

    # 选择用户性别
    def genderEdit(self, attribute, attribute1, attribute2):
        genders = self.find_xpath(attribute).text
        print(genders)
        self.xpath_click(attribute)
        if genders == '男':
            self.xpath_click(attribute2)
        else:
            self.xpath_click(attribute1)
        return self

    # 编辑手机号
    def phoneEdit(self, attribute, text):
        self.xpath_sendkeys(attribute, text)
        return self

    # 保存
    def saveClick(self, attribute):
        from appiumcode.page.pageMemberInvite import PageMemberInvite
        self.xpath_click(attribute)
        return PageMemberInvite(self.driver)

