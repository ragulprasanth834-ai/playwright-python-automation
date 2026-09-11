import pytest
from playwright.sync_api import expect

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from utils.config import Config


@pytest.mark.smoke
def test_login_with_valid_credentials(page:Page):
    login_page = LoginPage(page)
    login_page.open(Config.BASE_URL)
    login_page.login(Config.ADMIN_USERNAME, Config.ADMIN_PASSWORD)

    dashboard_page = DashboardPage(page)
    dashboard_page.expect_visible(dashboard_page.header)
    assert "Dashboard" in dashboard_page.get_header_text()


@pytest.mark.regression
def test_login_with_invalid_credentials(page):
    login_page = LoginPage(page)
    login_page.open(Config.BASE_URL)
    login_page.login("InvalidUser", "WrongPassword123")

    expect(login_page.error_message).to_be_visible()
    assert "Invalid credentials" in login_page.get_error_message()


@pytest.mark.regression
def test_login_with_empty_fields_shows_required_errors(page):
    login_page = LoginPage(page)
    login_page.open(Config.BASE_URL)
    login_page.click(login_page.login_button)

    required_errors = page.locator(".oxd-input-group__message")
    expect(required_errors.first).to_be_visible()
    assert required_errors.count() >= 2  # both username and password required


@pytest.mark.regression
def test_logout_returns_to_login_page(logged_in_page):
    dashboard_page = DashboardPage(logged_in_page)
    dashboard_page.logout()

    login_page = LoginPage(logged_in_page)
    login_page.expect_visible(login_page.login_button)
