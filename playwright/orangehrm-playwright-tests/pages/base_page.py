"""Base Page Object — common helpers shared by every page class."""

from playwright.sync_api import Page, expect


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self, url: str):
        self.page.goto(url)

    def click(self, locator):
        locator.click()

    def fill(self, locator, text: str):
        locator.fill(text)

    def get_text(self, locator) -> str:
        return locator.text_content().strip()

    def is_visible(self, locator) -> bool:
        return locator.is_visible()

    def wait_for_url_contains(self, fragment: str, timeout: int = 10000):
        self.page.wait_for_url(f"**/*{fragment}*", timeout=timeout)

    def expect_visible(self, locator, timeout: int = 10000):
        expect(locator).to_be_visible(timeout=timeout)

    def expect_text(self, locator, text: str, timeout: int = 10000):
        expect(locator).to_have_text(text, timeout=timeout)

    def screenshot(self, name: str):
        self.page.screenshot(path=f"reports/screenshots/{name}.png")
