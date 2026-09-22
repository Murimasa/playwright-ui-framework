import os
import pytest
import allure

pytest_plugins = ["fixtures.page_fixtures"]

AUTH_DIR = ".auth"
STATE_FILE = os.path.join(AUTH_DIR, "user_state.json")


@pytest.fixture(scope="session")
def session_storage_state(browser_type):
    """
    Authenticates once per test session and persists state to a JSON state file.
    """
    os.makedirs(AUTH_DIR, exist_ok=True)

    browser = browser_type.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://www.saucedemo.com/")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    page.wait_for_url("https://www.saucedemo.com/inventory.html")

    # Ensure SauceDemo session cookies are saved
    context.storage_state(path=STATE_FILE)

    context.close()
    browser.close()
    return STATE_FILE


@pytest.fixture
def auth_page(browser, session_storage_state):
    """
    Provides an isolated browser context pre-populated with saved authentication state.
    Injects session cookie to keep SauceDemo in authenticated state.
    """
    context = browser.new_context(storage_state=session_storage_state)
    # Add SauceDemo explicit session cookie
    context.add_cookies([
        {
            "name": "session-username",
            "value": "standard_user",
            "domain": "www.saucedemo.com",
            "path": "/",
        }
    ])
    page = context.new_page()
    yield page
    context.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page") or item.funcargs.get("auth_page")
        if page:
            screenshot_bytes = page.screenshot(full_page=True)
            allure.attach(
                screenshot_bytes,
                name=f"failure_{item.name}",
                attachment_type=allure.attachment_type.PNG,
            )