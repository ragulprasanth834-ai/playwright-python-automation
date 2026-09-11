"""Page Object for the OrangeHRM Dashboard page."""

from playwright.sync_api import Page
from pages.base_page import BasePage


class DashboardPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.header = page.locator(".oxd-topbar-header-breadcrumb h6")
        self.user_dropdown = page.locator(".oxd-userdropdown-tab")
        self.logout_link = page.get_by_role("menuitem", name="Logout")
        self.sidebar_menu_item = lambda name: page.get_by_role("link", name=name)

    def is_loaded(self) -> bool:
        return self.is_visible(self.header)

    def get_header_text(self) -> str:
        return self.get_text(self.header)

    def logout(self):
        self.click(self.user_dropdown)
        self.click(self.logout_link)

    def go_to_module(self, module_name: str):
        self.click(self.sidebar_menu_item(module_name))
