import pytest
from playwright.sync_api import Page


@pytest.fixture
def practice_page(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
    return page