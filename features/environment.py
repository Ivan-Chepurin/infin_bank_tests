from behave import fixture
from webdriver import DriverManager


@fixture
def selenium_browser_chrome(context):
    # -- HINT: @behave.fixture is similar to @contextlib.contextmanager
    context.driver = None
    yield context.driver
    # -- CLEANUP-FIXTURE PART:
    context.driver.quit()


def after_scenario(context, scenario):
    DriverManager().close(context.browser)
