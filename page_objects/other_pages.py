from page_objects.base import PageObject, EndpointPage
from page_objects.common_elements import Header


class CurrencyExchangeOffices(EndpointPage):
    def __init__(self,
                 webdriver,
                 current_lang):
        super().__init__(
            webdriver,
            current_lang,
            "https://infinbank.com/%s/private/exchange_offices/"
        )
        self.HEADER = Header(webdriver, current_lang)


class AllRates(EndpointPage):
    def __init__(self,
                 webdriver,
                 current_lang):
        super().__init__(
            webdriver,
            current_lang,
            "https://infinbank.com/%s/private/exchange-rates/"
        )
        self.HEADER = Header(webdriver, current_lang)



