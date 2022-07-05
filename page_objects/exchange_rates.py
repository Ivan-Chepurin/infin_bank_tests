from webdriver import DriverManager

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


if __name__ == "__main__":
    dm = DriverManager()
    dm.webdriver("chrome").get("https://infinbank.com/ru/")
    main = MainPage(dm.webdriver("chrome"), "RU")

    main.change_lang("UZ")
    main.HEADER.click_for_business()
    main.HEADER.click_for_me()
    main.HEADER.click_more()

    main.change_lang("EN")
    main.HEADER.click_for_business()
    main.HEADER.click_for_me()
    main.HEADER.click_more()

    main.change_lang("RU")
    main.HEADER.click_for_business()
    main.HEADER.click_for_me()
    main.HEADER.click_more()

    main.EXCHANGE_RATES.check_all_tickers()

    dm.close("chrome")
