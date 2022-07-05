from selenium.webdriver.common.by import By

from page_objects.base import PageObject

from page_objects.page_content import head, main_rates
from utils.webdriver import DriverManager


class Header(PageObject):
    CONTAINER = (By.CSS_SELECTOR, "div.header__main")

    LANGS = {
        "RU": (By.XPATH, "//span[text()='RU']"),
        "UZ": (By.XPATH, "//span[text()='UZ']"),
        "EN": (By.XPATH, "//span[text()='EN']")
    }
    MAIN_LINK = (By.XPATH, "//a[@class=\"header__link filter-link\"][@href=\"/ru/\"]")
    FOR_ME = (By.XPATH, "//span[@id=\"js-dynamic-menu--client-trigger\"]")
    FOR_BUSINESS = (By.XPATH, "//span[@id=\"js-dynamic-menu--business-trigger\"]")
    MORE = (By.CSS_SELECTOR, "a.header__link.filter-link.header-content-activator.d-f.ai-c")

    def __init__(self, webdriver, current_lang):
        super().__init__(
            webdriver,
            current_lang,
            container=self.CONTAINER
        )

    def check_for_me_text(self):
        self.check_text(self.FOR_ME, head["for_me"][self.current_lang])
        return self

    def check_for_business_text(self):
        self.check_text(self.FOR_BUSINESS, head["for_business"][self.current_lang])
        return self

    def check_more_text(self):
        self.check_text(self.MORE, head["more"][self.current_lang])
        return self

    def click_for_me(self):
        self.check_for_me_text().click(self.FOR_ME)

    def click_for_business(self):
        self.check_for_business_text().click(self.FOR_BUSINESS)

    def click_more(self):
        self.check_more_text().click(self.MORE)

    def change_lang(self, lang: str):
        self.actions.move_to_element(
            self.find(self.LANGS[self.current_lang])
        ).click(
            self.find(self.LANGS[lang])
        ).perform()
        super().change_lang(lang)


class ExchangeRates(PageObject):
    CONTAINER = (By.XPATH, "//div[@id=\"bank-rate\"]")
    CURRENCIES = ["USD", "EUR", "GBP", "RUB"]

    TITLE = (By.XPATH, "//div[@class=\"tickers-title\"]")
    TICKERS_LIST = (By.XPATH, "//div[@class=\"d-f ai-c tickers-content__list\"]")
    TICKER_INNER = (By.XPATH, "//div[@class=\"ticker__inner\"]")

    TICKERS_LINKS = (By.XPATH, "//div[@class=\"d-f ai-c tickers-other\"]")
    EXCHANGE_OFFICES = (By.XPATH, TICKERS_LINKS[1] + "//div[@class=\"tickers-link\"]")
    ALL_RATES = (By.XPATH, TICKERS_LINKS[1] + "//div[@class=\"btn-wrapper\"]")

    def __init__(self,
                 webdriver,
                 current_lang):
        super().__init__(
            webdriver,
            current_lang,
            container=self.CONTAINER
        )

    def check_title_text(self):
        self.check_text(self.TITLE, main_rates["tickers-title"][self.current_lang])
        return self

    def check_all_rates_text(self):
        self.check_text(self.ALL_RATES, main_rates["all_rates"][self.current_lang])
        return self

    def check_exchange_offices_text(self):
        self.check_text(self.EXCHANGE_OFFICES, main_rates["exchange_offices"][self.current_lang])
        return self

    def click_all_rates(self):
        self.check_all_rates_text()
        self.click(self.ALL_RATES)

    def click_exchange_offices(self):
        self.check_exchange_offices_text()
        self.click(self.EXCHANGE_OFFICES)

    def check_all_tickers(self):
        for currency in self.CURRENCIES:
            parent = self._ticker_parent(currency).get_attribute("class")
            change = self._ticker_change(currency).text

            if change.startswith("-"):
                assert parent.endswith("down"), \
                    self._assert_text(parent, change)

            if change.startswith("+"):
                assert parent.endswith("up"), \
                    self._assert_text(parent, change)
        return self

    def change_lang(self, lang):
        super().change_lang(lang)

    def _ticker_parent(self, currency):
        return self.find(
            (By.XPATH,
             self.TICKER_INNER[1] + f"//span[text()=\"{currency}\"]/../../../../..")
        )

    def _ticker_change(self, currency):
        return self.find(
            (By.XPATH,
             self.TICKER_INNER[1] + f"//span[text()=\"{currency}\"]/../../div[@class=\"ticker__yield\"]")
        )

    @staticmethod
    def _assert_text(v1, v2):
        return f"Класс элемента {v1} не соответствует значению {v2}"

