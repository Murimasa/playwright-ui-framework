import pytest
import allure
from playwright.sync_api import expect
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_step_one_page import CheckoutStepOnePage
from pages.checkout_step_two_page import CheckoutStepTwoPage


@allure.feature("Cart and Checkout Navigation")
class TestCart:

    @allure.story("Cart Management")
    def test_add_to_cart_and_verify_item(
        self,
        inventory_page: InventoryPage,
        cart_page: CartPage,
    ):
        with allure.step("1. Open catalog"):
            inventory_page.open("https://www.saucedemo.com/inventory.html")

        with allure.step("2. Add product to cart and open cart"):
            inventory_page.add_backpack_to_cart()
            inventory_page.go_to_cart()

        with allure.step("3. Verify URL and cart contents"):
            expect(cart_page.page).to_have_url(cart_page.URL)
            expect(cart_page.page_title).to_have_text("Your Cart")
            expect(cart_page.cart_item).to_be_visible()
            expect(cart_page.item_name).to_have_text("Sauce Labs Backpack")

    @allure.story("Cart Management")
    def test_remove_item_from_cart(
        self,
        inventory_page: InventoryPage,
        cart_page: CartPage,
    ):
        with allure.step("1. Open catalog and add Backpack"):
            inventory_page.open("https://www.saucedemo.com/inventory.html")
            inventory_page.add_backpack_to_cart()
            inventory_page.go_to_cart()

        with allure.step("2. Remove item from cart"):
            cart_page.remove_backpack()

        with allure.step("3. Verify item is removed and cart badge disappears"):
            expect(cart_page.cart_item).not_to_be_visible()
            expect(inventory_page.shopping_cart_badge).to_have_count(0)

    @allure.story("Checkout Navigation")
    def test_cancel_on_checkout_step_one_returns_to_cart(
        self,
        inventory_page: InventoryPage,
        cart_page: CartPage,
        checkout_step_one_page: CheckoutStepOnePage,
    ):
        with allure.step("1. Open cart and click Checkout"):
            inventory_page.open("https://www.saucedemo.com/inventory.html")
            inventory_page.add_backpack_to_cart()
            inventory_page.go_to_cart()
            cart_page.click_checkout()
            expect(checkout_step_one_page.page).to_have_url(checkout_step_one_page.URL)

        with allure.step("2. Click Cancel on Step One"):
            checkout_step_one_page.page.locator("[data-test='cancel']").click()

        with allure.step("3. Verify redirect back to Cart page"):
            expect(cart_page.page).to_have_url(cart_page.URL)

    @allure.story("Checkout Navigation")
    def test_cancel_on_checkout_step_two_returns_to_inventory(
        self,
        inventory_page: InventoryPage,
        cart_page: CartPage,
        checkout_step_one_page: CheckoutStepOnePage,
        checkout_step_two_page: CheckoutStepTwoPage,
    ):
        with allure.step("1. Reach Checkout Step Two"):
            inventory_page.open("https://www.saucedemo.com/inventory.html")
            inventory_page.add_backpack_to_cart()
            inventory_page.go_to_cart()
            cart_page.click_checkout()
            checkout_step_one_page.fill_checkout_form("John", "Doe", "12345")
            expect(checkout_step_two_page.page).to_have_url(checkout_step_two_page.URL)

        with allure.step("2. Click Cancel on Step Two"):
            checkout_step_two_page.page.locator("[data-test='cancel']").click()

        with allure.step("3. Verify redirect back to Inventory page"):
            expect(inventory_page.page).to_have_url("https://www.saucedemo.com/inventory.html")