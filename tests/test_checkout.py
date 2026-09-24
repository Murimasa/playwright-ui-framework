import pytest
import allure
from playwright.sync_api import expect
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_step_one_page import CheckoutStepOnePage
from pages.checkout_step_two_page import CheckoutStepTwoPage


@allure.feature("Checkout Flow")
class TestCheckout:

    @allure.story("Positive End-to-End Purchase")
    def test_complete_checkout_flow(
        self,
        inventory_page: InventoryPage,
        cart_page: CartPage,
        checkout_step_one_page: CheckoutStepOnePage,
        checkout_step_two_page: CheckoutStepTwoPage,
    ):
        with allure.step("1. Open catalog and add Backpack to cart"):
            inventory_page.open("https://www.saucedemo.com/inventory.html")
            inventory_page.add_backpack_to_cart()
            inventory_page.go_to_cart()

        with allure.step("2. Proceed to Checkout Step One"):
            cart_page.click_checkout()
            expect(cart_page.page).to_have_url(checkout_step_one_page.URL)

        with allure.step("3. Fill checkout credentials"):
            checkout_step_one_page.fill_checkout_form("John", "Doe", "12345")
            expect(checkout_step_one_page.page).to_have_url(checkout_step_two_page.URL)

        with allure.step("4. Finish order and verify confirmation message"):
            checkout_step_two_page.click_finish()
            expect(checkout_step_two_page.complete_header).to_be_visible()
            expect(checkout_step_two_page.complete_header).to_have_text(
                "Thank you for your order!"
            )

    @allure.story("Form Validation Errors")
    @pytest.mark.parametrize(
        "first_name, last_name, postal_code, expected_error",
        [
            ("", "Doe", "12345", "Error: First Name is required"),
            ("John", "", "12345", "Error: Last Name is required"),
            ("John", "Doe", "", "Error: Postal Code is required"),
        ],
        ids=["missing_first_name", "missing_last_name", "missing_postal_code"],
    )
    def test_checkout_form_validation(
        self,
        inventory_page: InventoryPage,
        cart_page: CartPage,
        checkout_step_one_page: CheckoutStepOnePage,
        first_name: str,
        last_name: str,
        postal_code: str,
        expected_error: str,
    ):
        with allure.step("1. Navigate to checkout form"):
            inventory_page.open("https://www.saucedemo.com/inventory.html")
            inventory_page.add_backpack_to_cart()
            inventory_page.go_to_cart()
            cart_page.click_checkout()

        with allure.step(f"2. Submit form with invalid inputs: '{first_name}', '{last_name}', '{postal_code}'"):
            checkout_step_one_page.fill_checkout_form(first_name, last_name, postal_code)

        with allure.step(f"3. Verify error message: '{expected_error}'"):
            expect(checkout_step_one_page.error_message).to_be_visible()
            expect(checkout_step_one_page.error_message).to_have_text(expected_error)