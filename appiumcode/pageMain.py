from appiumcode.base import baseView
from appiumcode.pageContacts import PageContacts


class PageMain(baseView):

    def contactActivity(self, attribute):
        self.xpath_click(attribute)
        return PageContacts(self.driver)
