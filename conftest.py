import pytest
import os
from playwright.sync_api import sync_playwright
from utilities.config import Config
from utilities.os_utils import get_screenshots_dir, ensure_dir_exists

@pytest.fixture(scope="session")
def config():
    return Config()

@pytest.fixture(scope="session")
def browser_context(config):
    with sync_playwright() as p:
        browser_type = getattr(p, config.browser)
        browser = browser_type.launch(headless=config.headless)
        context = browser.new_context()
        yield context
        browser.close()

@pytest.fixture(scope="function")
def page(browser_context):
    page = browser_context.new_page()
    yield page
    page.close()

def pytest_configure(config):
    """Setup test configuration before running tests"""
    ensure_dir_exists(get_screenshots_dir())

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Take screenshot on test failure"""
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        if "page" in item.funcargs:
            page = item.funcargs["page"]
            screenshot_path = os.path.join(
                get_screenshots_dir(),
                f"failed_{item.name}.png"
            )
            page.screenshot(path=screenshot_path)