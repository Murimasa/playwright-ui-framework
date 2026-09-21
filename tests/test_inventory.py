from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_inventory_page_header(
    login_page: LoginPage, inventory_page: InventoryPage
):
    # 1. Login to reach the inventory page
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    # 2. Verify products header is visible and has correct text
    expect(inventory_page.page_title).to_be_visible()
    expect(inventory_page.page_title).to_have_text("Products")


def test_add_item_to_cart(
    login_page: LoginPage, inventory_page: InventoryPage
):
    # 1. Login
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    # 2. Add item to cart
    inventory_page.add_backpack_to_cart()

    # 3. Verify cart badge displays '1'
    expect(inventory_page.shopping_cart_badge).to_be_visible()
    expect(inventory_page.shopping_cart_badge).to_have_text("1")

    # 4. Verify the button switched to 'Remove'
    expect(inventory_page.remove_backpack_btn).to_be_visible()