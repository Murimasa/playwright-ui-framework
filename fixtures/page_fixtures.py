import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_step_one_page import CheckoutStepOnePage
from pages.checkout_step_two_page import CheckoutStepTwoPage


@pytest.fixture
def login_page(page):
    """Clean, unauthenticated page for login tests."""
    return LoginPage(page)


@pytest.fixture
def inventory_page(auth_page):
    """Inventory page bound to pre-authenticated browser context."""
    return InventoryPage(auth_page)


@pytest.fixture
def cart_page(auth_page):
    """Cart page bound to pre-authenticated browser context."""
    return CartPage(auth_page)


@pytest.fixture
def checkout_step_one_page(auth_page):
    """Checkout Step One page bound to pre-authenticated browser context."""
    return CheckoutStepOnePage(auth_page)


@pytest.fixture
def checkout_step_two_page(auth_page):
    """Checkout Step Two page bound to pre-authenticated browser context."""
    return CheckoutStepTwoPage(auth_page)