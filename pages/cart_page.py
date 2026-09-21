from playwright.sync_api import Page, Locator
from pages.base_page import BasePage


class CartPage(BasePage):
    URL = "https://www.saucedemo.com/cart.html"

    def __init__(self, page: Page):
        super().__init__(page)
        # Locators
        self.page_title: Locator = page.locator(".title")
        self.cart_item: Locator = page.locator(".cart_item")
        self.item_name: Locator = page.locator(".inventory_item_name")
        self.checkout_button: Locator = page.locator("#checkout")
        self.remove_button: Locator = page.locator(
            "#remove-sauce-labs-backpack"
        )

    def click_checkout(self):
        """Proceed to checkout step one."""
        self.checkout_button.click()

    def remove_backpack(self):
        """Remove backpack from cart."""
        self.remove_button.click()