from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


def test_add_to_cart_and_verify_item(
    login_page: LoginPage,
    inventory_page: InventoryPage,
    cart_page: CartPage,
    page: Page,
):
    # 1. Login
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    # 2. Add product to cart and open cart
    inventory_page.add_backpack_to_cart()
    inventory_page.go_to_cart()

    # 3. Verify URL and cart contents
    expect(page).to_have_url(cart_page.URL)
    expect(cart_page.page_title).to_have_text("Your Cart")
    expect(cart_page.cart_item).to_be_visible()
    expect(cart_page.item_name).to_have_text("Sauce Labs Backpack")


def test_remove_item_from_cart(
    login_page: LoginPage,
    inventory_page: InventoryPage,
    cart_page: CartPage,
):
    # 1. Login and add item
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    inventory_page.add_backpack_to_cart()
    inventory_page.go_to_cart()

    # 2. Remove item
    cart_page.remove_backpack()

    # 3. Verify item is no longer visible
    expect(cart_page.cart_item).not_to_be_visible()