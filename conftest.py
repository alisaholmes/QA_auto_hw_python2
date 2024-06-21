from selene import browser, be, have
import pytest


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.base_url='https://google.com'
    browser.config.timeout = 10
    browser.config.driver_name = 'firefox'
    browser.config.window_height = 1024
    browser.config.window_width = 600

    yield

    browser.quit()
    print("Закрываем браузер!")
