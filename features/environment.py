from behave import fixture
from utils.webdriver import DriverManager


@fixture
def selenium_browser_chrome(context):
    context.driver = None
    yield context.driver
    
    context.driver.close()


def after_scenario(context, scenario):
    DriverManager().close(context.browser)
