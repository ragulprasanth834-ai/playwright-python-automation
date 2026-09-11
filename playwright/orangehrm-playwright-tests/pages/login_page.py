"""Page Object for the OrangeHRM Login page."""

from playwright.sync_api import Page
from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.username_input = page.get_by_placeholder("Username")
        self.password_input = page.get_by_placeholder("Password")
        self.login_button = page.get_by_role("button", name="Login")
        self.error_message = page.locator(".oxd-alert-content-text")
        self.forgot_password_link = page.get_by_text("Forgot your password?")

    def open(self, base_url: str):
        self.navigate(f"{base_url}/web/index.php/auth/login")

    def login(self, username: str, password: str):
        self.fill(self.username_input, username)
        self.fill(self.password_input, password)
        self.click(self.login_button)

    def get_error_message(self) -> str:
        return self.get_text(self.error_message)
