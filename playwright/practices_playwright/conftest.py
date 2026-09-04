import pytest
from playwright.sync_api import Page


@pytest.fixture
def practice_page(page: Page):
    page.goto("https://automatewithbipin.com/?utm_source=chatgpt.com")
    return page

@pytest.fixture
def practice_page1(page:Page):
    page.goto("https://automatewithbipin.com/?utm_source=chatgpt.com")
    return page