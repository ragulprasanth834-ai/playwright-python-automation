from playwright.sync_api import expect, Playwright


def test_browsercontext(playwright: Playwright):

    browser = playwright.chromium.launch(headless=False)

    context = browser.new_context()

    page1 = context.new_page()

    page1.goto("https://playwright.dev/")

    page2 = context.new_page()

    page2.goto("https://www.selenium.dev/")
    text=page2.locator(".d-1.fw-bold")

    print("Page title:", page1.title(),page2.title())

    expect(page1).to_have_title("Fast and reliable end-to-end testing for modern web apps | Playwright")
    expect(text).to_have_text("Selenium automates browsers. That's it!")
    browser.close()