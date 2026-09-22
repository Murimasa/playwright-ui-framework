import pytest
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage


def test_successful_login(login_page: LoginPage, page: Page):
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")


@pytest.mark.parametrize(
    "username, password, expected_error",
    [
        (
            "locked_out_user",
            "secret_sauce",
            "Epic sadface: Sorry, this user has been locked out.",
        ),
        (
            "",
            "secret_sauce",
            "Epic sadface: Username is required",
        ),
        (
            "standard_user",
            "",
            "Epic sadface: Password is required",
        ),
        (
            "invalid_user",
            "invalid_password",
            "Epic sadface: Username and password do not match any user in this service",
        ),
    ],
    ids=["locked_out", "empty_username", "empty_password", "invalid_credentials"],
)
def test_login_negative(
    login_page: LoginPage, username: str, password: str, expected_error: str
):
    login_page.navigate()
    login_page.login(username, password)

    expect(login_page.error_message).to_be_visible()
    expect(login_page.error_message).to_have_text(expected_error)