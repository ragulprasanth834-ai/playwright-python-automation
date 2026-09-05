import pytest
from playwright.sync_api import Page


@pytest.fixture
def practice_page1(page:Page):
    page.goto("https://automatewithbipin.com/?utm_source=chatgpt.com")
    return page

@pytest.fixture
def orangehrm(page:Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    return page