from playwright.sync_api import Playwright, expect


def test_auth(playwright: Playwright):

    browser = playwright.chromium.launch(headless=False)

    context = browser.new_context(
        http_credentials={
            "username": "user",
            "password": "pass"
        }
    )

    page = context.new_page()

    page.goto("https://authenticationtest.com/HTTPAuth/")

    print("URL:", page.url)
    print("TITLE:", page.title())
    print("H1:", page.locator("h1").inner_text())

    expect(page.locator("h1")).to_have_text("Login Success")

    browser.close()