import pytest
from playwright.sync_api import sync_playwright

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from utils.config import Config


@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p


@pytest.fixture(scope="function")
def browser(playwright_instance):
    # headless=False lets you watch the browser while developing/debugging.
    browser = playwright_instance.chromium.launch(headless=True, slow_mo=0)
    yield browser
    browser.close()


@pytest.fixture(scope="function")
def context(browser):
    context = browser.new_context(viewport={"width": 1440, "height": 900})
    yield context
    context.close()


@pytest.fixture(scope="function")
def page(context):
    page = context.new_page()
    yield page
    page.close()


@pytest.fixture(scope="function")
def logged_in_page(page):
    """Returns a page that is already authenticated as Admin, dropped on the dashboard."""
    login_page = LoginPage(page)
    login_page.open(Config.BASE_URL)
    login_page.login(Config.ADMIN_USERNAME, Config.ADMIN_PASSWORD)

    dashboard_page = DashboardPage(page)
    dashboard_page.expect_visible(dashboard_page.header)
    return page
