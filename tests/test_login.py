from playwright.sync_api import Page, expect
from pages.login_page import LoginPage


def test_successful_login(login_page: LoginPage, page: Page):
    # 1. Открываем страницу
    login_page.navigate()

    # 2. Выполняем вход
    login_page.login("standard_user", "secret_sauce")

    # 3. Проверяем, что нас перенаправило в каталог товаров
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")


def test_login_with_invalid_credentials(login_page: LoginPage):
    # 1. Открываем страницу
    login_page.navigate()

    # 2. Пробуем войти с неверным паролем
    login_page.login("standard_user", "wrong_password")

    # 3. Проверяем сообщение об ошибке
    expect(login_page.error_message).to_be_visible()
    expect(login_page.error_message).to_contain_text(
        "Username and password do not match"
    )