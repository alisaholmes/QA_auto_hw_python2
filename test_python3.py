import pytest
from selene import browser, be, have

@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.base_url='https://google.com'
    browser.config.timeout = 10
    browser.config.driver_name = 'firefox'
    browser.config.window_height = 1024
    browser.config.window_width = 600

    yield
    print("Закрываем браузер!")

    # driver_options = webdriver.ChromeOptions()
    # driver_options.page_load_strategy = 'eager'

def test_positiv_search():
    browser.open('')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_negative_search():
    browser.open('')
    browser.element('[name="q"]').should(be.blank).type('РВАРИРВАИСИЫВГСИШЫВИМРЫИВГМ').press_enter()
    browser.element('[class="card-section"]').should(have.text('По запросу РВАРИРВАИСИЫВГСИШЫВИМРЫИВГМ ничего не найдено'))



