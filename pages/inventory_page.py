from playwright.sync_api import Page, Locator
from pages.base_page import BasePage


class InventoryPage(BasePage):
    URL = "https://www.saucedemo.com/inventory.html"

    def __init__(self, page: Page):
        super().__init__(page)
        # Locators
        self.page_title: Locator = page.locator(".title")
        self.shopping_cart_link: Locator = page.locator(".shopping_cart_link")
        self.shopping_cart_badge: Locator = page.locator(".shopping_cart_badge")
        self.add_to_cart_backpack_btn: Locator = page.locator(
            "#add-to-cart-sauce-labs-backpack"
        )
        self.remove_backpack_btn: Locator = page.locator(
            "#remove-sauce-labs-backpack"
        )

    def add_backpack_to_cart(self):
        """Add Sauce Labs Backpack to the shopping cart."""
        self.add_to_cart_backpack_btn.click()

    def go_to_cart(self):
        """Click on the cart icon to navigate to the Cart page."""
        self.shopping_cart_link.click()

    def get_cart_badge_count(self) -> str:
        """Return the current item count displayed on the cart badge."""
        return self.shopping_cart_badge.inner_text()