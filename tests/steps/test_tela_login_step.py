from pytest_bdd.parsers import parse

from pytest_bdd import given, when, then, scenarios
from playwright.sync_api import expect
from pytest_playwright.pytest_playwright import Page

scenarios('../features/tela_login.feature')

username = 'standard_user'
password = 'secret_sauce'


@given("Estou na pagina do google")
def step_acesso_pagina_googlel(browser: Page):
    browser.goto('https://www.google.com.br/')


@when(parse("farei uma pesquisa usando o meu nome"), converters=dict(texto=str))
def step_impl(browser: Page):
    browser.locator('[name="q"]').fill('Rafael')
    browser.keyboard.press('Enter')


@then(parse("farei uma validação para saber se o meu nome existe"), converters=dict(texto=str))
def step_impl(browser: Page):
    expect(browser.get_by_text('Rafael'))


# -----------------------------------------------------------------------------

@given("Estou na pagina de login saucedemo")
def step_impl(browser: Page):
    browser.goto('https://www.saucedemo.com/')


@when("Preencho o username e password")
def step_impl(browser: Page):
    browser.locator('[type="text"]').fill(username)
    browser.locator('[type="password"]').fill(password)


@then("faço login")
def step_impl(browser: Page):
    button_login = browser.locator('[type="submit"]')
    button_login.click()
