from playwright.sync_api import Page, Locator
from pages.base_page import BasePage


class CheckoutStepTwoPage(BasePage):
    URL = "https://www.saucedemo.com/checkout-step-two.html"

    def __init__(self, page: Page):
        super().__init__(page)
        # Locators
        self.page_title: Locator = page.locator(".title")
        self.finish_button: Locator = page.locator("#finish")
        self.complete_header: Locator = page.locator(".complete-header")

    def click_finish(self):
        """Click finish button to complete order."""
        self.finish_button.click()