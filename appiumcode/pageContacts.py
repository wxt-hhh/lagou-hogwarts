from appiumcode.base import baseView
from appiumcode.pageMain import PageMain


class PageContacts(baseView):

    def messageAcitvity(self, attribute):
        self.xpath_click(attribute)
        return PageMain(self.driver)
