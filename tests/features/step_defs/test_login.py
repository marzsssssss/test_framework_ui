import os
from playwright.sync_api import expect
from pytest_bdd import scenarios, given, when, then, parsers
from dotenv import load_dotenv

from page.locators.pre_auth.locators import SignIn, SignInCode
from config.links import Links

load_dotenv()

scenarios('../scenarios/login.feature')

@given('Открыта страница логина')
def step_open_login(page):
    page.goto(Links.LOGIN_PAGE)
    
@when(parsers.parse('Пользователь вводит номер телефона и код "{code}"'))
def step_write_test_credit(page, code):
    sign_in = SignIn(page)
    sign_in_code = SignInCode(page)

    sign_in.input_phone.fill(f"{os.getenv('TEST_PHONE')}")
    sign_in.button_send_code.click()

    sign_in_code.input_code.fill(code)
    sign_in_code.button_submit.click()

@then('Он видит главную страницу')
def step_expect(page):
    expect(page).to_have_url(Links.ACCOUNTS_PAGE)