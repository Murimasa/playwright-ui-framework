from playwright.sync_api import Page, Locator
from pages.base_page import BasePage


class LoginPage(BasePage):
    URL = "https://www.saucedemo.com/"

    def __init__(self, page: Page):
        super().__init__(page)
        # Локаторы элементов
        self.username_input: Locator = page.locator("#user-name")
        self.password_input: Locator = page.locator("#password")
        self.login_button: Locator = page.locator("#login-button")
        self.error_message: Locator = page.locator("[data-test='error']")

    def navigate(self):
        """Открыть страницу авторизации."""
        self.open(self.URL)

    def login(self, username: str, password: str):
        """Заполнить форму и нажать Submit."""
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()