from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_step_one_page import CheckoutStepOnePage
from pages.checkout_step_two_page import CheckoutStepTwoPage


def test_complete_checkout_flow(
    login_page: LoginPage,
    inventory_page: InventoryPage,
    cart_page: CartPage,
    checkout_step_one_page: CheckoutStepOnePage,
    checkout_step_two_page: CheckoutStepTwoPage,
    page: Page,
):
    # 1. Authorize
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    # 2. Add product and open cart
    inventory_page.add_backpack_to_cart()
    inventory_page.go_to_cart()

    # 3. Proceed to checkout form
    cart_page.click_checkout()
    expect(page).to_have_url(checkout_step_one_page.URL)

    # 4. Fill customer details and continue
    checkout_step_one_page.fill_checkout_form("John", "Doe", "12345")
    expect(page).to_have_url(checkout_step_two_page.URL)

    # 5. Finish order
    checkout_step_two_page.click_finish()

    # 6. Verify successful completion header
    expect(checkout_step_two_page.complete_header).to_be_visible()
    expect(checkout_step_two_page.complete_header).to_have_text(
        "Thank you for your order!"
    )