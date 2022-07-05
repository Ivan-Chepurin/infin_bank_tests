from selenium.webdriver.remote.webdriver import WebDriver

from selenium.webdriver.common.action_chains import ActionChains


class PageObject:
    def __init__(self,
                 webdriver: WebDriver,
                 current_lang: str,
                 container: tuple = None):

        self.webdriver = webdriver
        self.actions = ActionChains(webdriver)
        self.current_lang = current_lang
        self.CONTAINER = container

    def container(self):
        return self.webdriver.find_element(
            self.CONTAINER[0], self.CONTAINER[1]
        )

    def find(self, locator):
        if self.CONTAINER:
            return self.container().find_element(locator[0], locator[1])
        return self.webdriver.find_element(locator[0], locator[1])

    def find_all(self, locator):
        if self.CONTAINER:
            return self.container().find_elements(locator[0], locator[1])
        return self.webdriver.find_elements(locator[0], locator[1])

    def click(self, locator):
        self.find(locator).click()

    def clear(self, locator):
        self.find(locator).clear()

    def write(self, text, locator):
        self.find(locator).send_keys(text)

    def check_text(self, locator, expected_value):
        assert self.find(locator).text == expected_value, \
            f"Текст элемента не совпадает с ожидаемым: {self.find(locator).text} != {expected_value}"

    def change_lang(self, lang):
        self.current_lang = lang


class EndpointPage(PageObject):

    def __init__(self,
                 webdriver,
                 current_lang,
                 url: str):
        super().__init__(
            webdriver,
            current_lang
        )
        self.URL = url % self.current_lang.lower()

    def check_url(self):
        assert self.webdriver.current_url == self.URL, \
            f"URL страницы '{self.webdriver.current_url}' не соответствует ожидаемому '{self.URL}'"
