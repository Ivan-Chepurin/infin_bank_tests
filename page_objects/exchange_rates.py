from utils.webdriver import DriverManager

from page_objects.base import PageObject
from page_objects.common_elements import Header, ExchangeRates


class MainPage(PageObject):

    def __init__(self, webdriver, current_lang):
        super().__init__(webdriver, current_lang)
        self.HEADER = Header(webdriver, current_lang)
        self.EXCHANGE_RATES = ExchangeRates(webdriver, current_lang)

    def change_lang(self, lang):
        super().change_lang(lang)
        self.HEADER.change_lang(lang)
        self.EXCHANGE_RATES.change_lang(lang)

