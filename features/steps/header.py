from behave import *

from page_objects.exchange_rates import MainPage
from webdriver import DriverManager


@given("Open browser {browser} on {url} and set current language {lang}")
def open_browser(context, browser, url, lang):
    context.browser = browser
    context.driver = DriverManager().webdriver(browser)
    context.driver.get(url)
    context.main_page = MainPage(context.driver, lang)


@then("Check the texts of the functionality \"currency rates\" in the current language")
def check_currency_rates_texts(context):
    context.main_page.EXCHANGE_RATES.check_title_text()
    context.main_page.EXCHANGE_RATES.check_all_rates_text()
    context.main_page.EXCHANGE_RATES.check_exchange_offices_text()


@then("Change language to {language}")
def change_language(context, language):
    context.main_page.change_lang(language)


@then("Check the correspondence of indicators to changes in exchange rates")
def check_indicators(context):
    context.main_page.EXCHANGE_RATES.check_all_tickers()
