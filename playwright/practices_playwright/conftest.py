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

@pytest.fixture
def assertqa(page:Page):
    page.goto("https://assertqa.com/practice/webtables?utm_source=chatgpt.com")
    return page
@pytest.fixture
def practiceplaywright(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
    return page
@pytest.fixture
def qaplayground(page:Page):
    page.goto("https://qaplayground.com/practice/date-picker?utm_source=chatgpt.com")
    return page
@pytest.fixture
def Amazon_page(page:Page):
    page.goto("https://www.amazon.in/s?k=join+amazon+prime&adgrpid=1327112148528381&hvadid=82944842492529&hvbmt=bb&hvdev=c&hvlocphy=155464&hvnetw=o&hvqmt=b&hvtargid=kwd-82945393014646%3Aloc-90&hydadcr=5626_2502674&mcid=3861a9d242543041b997efa1f39279d3&msclkid=2488a19f783612e6bc85cb01321996da&tag=msndeskstdin-21&ref=pd_sl_9ntprzamt3_b")
    return page
