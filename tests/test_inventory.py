import pytest
import allure
from playwright.sync_api import expect
from pages.inventory_page import InventoryPage


@allure.feature("Catalog Inventory")
class TestInventory:

    @allure.story("Catalog Sorting")
    @pytest.mark.parametrize(
        "sort_value, check_type, expected_order",
        [
            ("az", "name", False),    # Name: A to Z (ascending)
            ("za", "name", True),     # Name: Z to A (descending)
            ("lohi", "price", False), # Price: Low to High (ascending)
            ("hilo", "price", True),  # Price: High to Low (descending)
        ],
        ids=["name_a_to_z", "name_z_to_a", "price_low_to_high", "price_high_to_low"]
    )
    def test_catalog_sorting(
        self,
        inventory_page: InventoryPage,
        sort_value: str,
        check_type: str,
        expected_order: bool,
    ):
        # 1. Navigate to catalog and apply chosen sorting option
        inventory_page.open()
        inventory_page.select_sort_option(sort_value)

        # 2. Extract values and verify against Python standard sort
        if check_type == "name":
            actual_names = inventory_page.get_item_names()
            sorted_names = sorted(actual_names, reverse=expected_order)
            assert actual_names == sorted_names, f"Sorting mismatch: {actual_names} != {sorted_names}"
        elif check_type == "price":
            actual_prices = inventory_page.get_item_prices()
            sorted_prices = sorted(actual_prices, reverse=expected_order)
            assert actual_prices == sorted_prices, f"Sorting mismatch: {actual_prices} != {sorted_prices}"

    @allure.story("Burger Menu Actions")
    def test_reset_app_state_clears_cart(self, inventory_page: InventoryPage):
        # 1. Open catalog and add an item to the shopping cart
        inventory_page.open()
        inventory_page.add_backpack_btn.click()
        expect(inventory_page.shopping_cart_badge).to_have_text("1")

        # 2. Reset app state via sidebar menu
        inventory_page.reset_app_state()

        # 3. Verify shopping cart badge is reset and detached
        expect(inventory_page.shopping_cart_badge).to_have_count(0)

    @allure.story("Burger Menu Actions")
    def test_logout_redirects_to_login_page(self, inventory_page: InventoryPage):
        # 1. Open catalog and trigger logout sequence
        inventory_page.open()
        inventory_page.logout()

        # 2. Verify redirect back to authentication form
        expect(inventory_page.page).to_have_url("https://www.saucedemo.com/")
        expect(inventory_page.page.locator("#login-button")).to_be_visible()