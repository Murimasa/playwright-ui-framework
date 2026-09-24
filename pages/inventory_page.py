import allure
from playwright.sync_api import Page, Locator


class InventoryPage:
    URL = "https://www.saucedemo.com/inventory.html"

    def __init__(self, page: Page):
        self.page = page
        self.sort_select = page.locator("[data-test='product-sort-container']")
        self.inventory_item_names = page.locator("[data-test='inventory-item-name']")
        self.inventory_item_prices = page.locator("[data-test='inventory-item-price']")
        self.add_backpack_btn = page.locator("[data-test='add-to-cart-sauce-labs-backpack']")
        self.shopping_cart_badge = page.locator("[data-test='shopping-cart-badge']")
        self.shopping_cart_link = page.locator("[data-test='shopping-cart-link']")
        # Sidebar navigation controls
        self.burger_menu_btn = page.locator("#react-burger-menu-btn")
        self.menu_logout_link = page.locator("[data-test='logout-sidebar-link']")
        self.menu_reset_link = page.locator("[data-test='reset-sidebar-link']")
        self.menu_close_btn = page.locator("#react-burger-cross-btn")

    @allure.step("Open inventory page")
    def open(self, url: str | None = None):
        target_url = url or self.URL
        self.page.goto(target_url)

    @allure.step("Select sort option: {option_value}")
    def select_sort_option(self, option_value: str):
        # Options: 'az', 'za', 'lohi', 'hilo'
        self.sort_select.select_option(option_value)

    @allure.step("Get all product titles displayed on page")
    def get_item_names(self) -> list[str]:
        return self.inventory_item_names.all_text_contents()

    @allure.step("Get all product prices parsed as floats")
    def get_item_prices(self) -> list[float]:
        raw_prices = self.inventory_item_prices.all_text_contents()
        # Parse currency formatted strings like '$29.99' into float 29.99
        return [float(price.replace("$", "")) for price in raw_prices]

    @allure.step("Open sidebar burger menu")
    def open_burger_menu(self):
        self.burger_menu_btn.click()
        self.menu_logout_link.wait_for(state="visible")

    @allure.step("Reset application state via menu")
    def reset_app_state(self):
        self.open_burger_menu()
        self.menu_reset_link.click()
        self.menu_close_btn.click()

    @allure.step("Logout from application")
    def logout(self):
        self.open_burger_menu()
        self.menu_logout_link.click()

    @allure.step("Add Sauce Labs Backpack to cart")
    def add_backpack_to_cart(self):
        self.add_backpack_btn.click()

    @allure.step("Navigate to shopping cart")
    def go_to_cart(self):
        self.shopping_cart_link.click()