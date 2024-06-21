import pytest
from selene import browser, be, have


def test_positive_search():
    browser.open('')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_negative_search():
    browser.open('')
    browser.element('[name="q"]').should(be.blank).type('РВАРИРВАИСИЫВГСИШЫВИМРЫИВГМ').press_enter()
    browser.element('[class="card-section"]').should(have.text('По запросу РВАРИРВАИСИЫВГСИШЫВИМРЫИВГМ ничего не найдено'))



