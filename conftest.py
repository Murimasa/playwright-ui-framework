import os
import re
import pytest
import allure

pytest_plugins = ["fixtures.page_fixtures"]

AUTH_DIR = ".auth"
STATE_FILE = os.path.join(AUTH_DIR, "user_state.json")
TRACES_DIR = "test-results/traces"


@pytest.fixture(scope="session")
def session_storage_state(browser_type):
    os.makedirs(AUTH_DIR, exist_ok=True)
    state_file = os.path.join(AUTH_DIR, f"{browser_type.name}_user_state.json")

    if os.path.exists(state_file) and os.path.getsize(state_file) > 0:
        return state_file

    browser = browser_type.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://www.saucedemo.com/")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    page.wait_for_url("https://www.saucedemo.com/inventory.html")

    context.storage_state(path=state_file)

    context.close()
    browser.close()
    return state_file


@pytest.fixture
def auth_page(browser, session_storage_state, request):
    os.makedirs(TRACES_DIR, exist_ok=True)

    context = browser.new_context(storage_state=session_storage_state)
    context.add_cookies([
        {
            "name": "session-username",
            "value": "standard_user",
            "domain": "www.saucedemo.com",
            "path": "/",
        }
    ])

    # Запускаем запись трейса
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    page = context.new_page()
    yield page

    # Teardown: проверяем, упал ли тест
    # Если на ноде зафиксирован статус фейла
    failed = hasattr(request.node, "rep_call") and request.node.rep_call.failed

    if failed:
        # Очищаем имя от спецсимволов для безопасного сохранения пути
        clean_name = re.sub(r'[^\w\-_\.]', '_', request.node.name)
        trace_path = os.path.join(TRACES_DIR, f"{clean_name}_trace.zip")
        context.tracing.stop(path=trace_path)
        allure.attach.file(
            trace_path,
            name=f"trace_{clean_name}",
            extension="zip",
        )
    else:
        context.tracing.stop()

    context.close()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    # Записываем отчёт прямо на тест ДО вызова teardown фикстуры
    setattr(item, f"rep_{report.when}", report)

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page") or item.funcargs.get("auth_page")
        if page:
            screenshot_bytes = page.screenshot(full_page=True)
            allure.attach(
                screenshot_bytes,
                name=f"failure_{item.name}",
                attachment_type=allure.attachment_type.PNG,
            )