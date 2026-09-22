import pytest
from playwright.sync_api import expect
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_step_one_page import CheckoutStepOnePage
from pages.checkout_step_two_page import CheckoutStepTwoPage


def test_complete_checkout_flow(
    inventory_page: InventoryPage,
    cart_page: CartPage,
    checkout_step_one_page: CheckoutStepOnePage,
    checkout_step_two_page: CheckoutStepTwoPage,
):
    inventory_page.open("https://www.saucedemo.com/inventory.html")
    inventory_page.add_backpack_to_cart()
    inventory_page.go_to_cart()

    cart_page.click_checkout()
    expect(cart_page.page).to_have_url(checkout_step_one_page.URL)

    checkout_step_one_page.fill_checkout_form("John", "Doe", "12345")
    expect(checkout_step_one_page.page).to_have_url(checkout_step_two_page.URL)

    checkout_step_two_page.click_finish()
    expect(checkout_step_two_page.complete_header).to_be_visible()
    expect(checkout_step_two_page.complete_header).to_have_text(
        "Thank you for your order!"
    )


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
    inventory_page: InventoryPage,
    cart_page: CartPage,
    checkout_step_one_page: CheckoutStepOnePage,
    first_name: str,
    last_name: str,
    postal_code: str,
    expected_error: str,
):
    inventory_page.open("https://www.saucedemo.com/inventory.html")
    inventory_page.add_backpack_to_cart()
    inventory_page.go_to_cart()
    cart_page.click_checkout()

    checkout_step_one_page.fill_checkout_form(first_name, last_name, postal_code)

    expect(checkout_step_one_page.error_message).to_be_visible()
    expect(checkout_step_one_page.error_message).to_have_text(expected_error)