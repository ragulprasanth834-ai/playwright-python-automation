from playwright.sync_api import Page,expect

def test_url(page:Page):
    page.goto("https://www.youtube.com/")
    expect(page).to_have_url("https://www.youtube.com/")
    page.wait_for_timeout(3000)