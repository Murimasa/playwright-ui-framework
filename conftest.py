import allure
import pytest
from playwright.sync_api import Page

pytest_plugins = [
    "fixtures.page_fixtures",
]


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    # We only care about failures during the actual test call
    if rep.when == "call" and rep.failed:
        page: Page = item.funcargs.get("page")
        if page:
            allure.attach(
                page.screenshot(full_page=True),
                name=f"failure_{item.name}",
                attachment_type=allure.attachment_type.PNG,
            )