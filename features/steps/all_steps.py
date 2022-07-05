from behave import *

from page_objects.exchange_rates import MainPage
from page_objects.other_pages import CurrencyExchangeOffices, AllRates
from utils.webdriver import DriverManager


@given("Open browser {browser} on {url} and set current language {lang}")
def open_browser(context, browser, url: str, lang: str):
    context.browser = browser
    context.driver = DriverManager().webdriver(browser)
    context.driver.get(url.replace("lang", lang.lower()))

    context.main_page = MainPage(context.driver, lang)
    context.EXCHANGE_OFFICES = CurrencyExchangeOffices(context.driver, lang)
    context.ALL_RATES = AllRates(context.driver, lang)


@when("Change language to {language}")
def change_language(context, language):
    context.main_page.change_lang(language)


@when("Click all rates button")
def click_all_rates(context):
    context.main_page.EXCHANGE_RATES.click_all_rates()


@when("Click exchange offices link")
def click_exchange_offices(context):
    context.main_page.EXCHANGE_RATES.click_exchange_offices()


@then("Check the correspondence of indicators to changes in exchange rates")
def check_indicators(context):
    context.main_page.EXCHANGE_RATES.check_all_tickers()


@then("Check exchange offices link text in current language")
def check_exchange_offices_link_text(context):
    context.main_page.EXCHANGE_RATES.check_exchange_offices_text()


@then("Check \"currency rates\" title text in current language")
def check_title_text(context):
    context.main_page.EXCHANGE_RATES.check_title_text()


@then("Check all rates button text in current language")
def check_all_rates_button_text(context):
    context.main_page.EXCHANGE_RATES.check_all_rates_text()


@then("Check url Check the url on the \"all rates\" page")
def check_all_rates_url(context):
    context.ALL_RATES.check_url()


@then("Check url Check the url on the \"currency exchange offices\" page")
def check_all_rates_url(context):
    context.EXCHANGE_OFFICES.check_url()
