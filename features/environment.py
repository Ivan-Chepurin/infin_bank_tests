from behave import fixture
from utils.webdriver import DriverManager


@fixture
def selenium_browser_chrome(context):
    # -- HINT: @behave.fixture is similar to @contextlib.contextmanager
    context.driver = None
    yield context.driver
    # -- CLEANUP-FIXTURE PART:
    context.driver.close()


def after_scenario(context, scenario):
    DriverManager().close(context.browser)
