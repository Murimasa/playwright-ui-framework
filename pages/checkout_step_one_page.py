from playwright.sync_api import Page, Locator
from pages.base_page import BasePage


class CheckoutStepOnePage(BasePage):
    URL = "https://www.saucedemo.com/checkout-step-one.html"

    def __init__(self, page: Page):
        super().__init__(page)
        # Locators
        self.page_title: Locator = page.locator(".title")
        self.first_name_input: Locator = page.locator("#first-name")
        self.last_name_input: Locator = page.locator("#last-name")
        self.postal_code_input: Locator = page.locator("#postal-code")
        self.continue_button: Locator = page.locator("#continue")
        self.error_message: Locator = page.locator("[data-test='error']")

    def fill_checkout_form(
        self, first_name: str, last_name: str, postal_code: str
    ):
        """Fill in buyer details and click Continue."""
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.postal_code_input.fill(postal_code)
        self.continue_button.click()