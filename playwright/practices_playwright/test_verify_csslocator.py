from playwright.sync_api import Page, expect


def test_verify_csslocator(page: Page):
    page.goto("https://demowebshop.tricentis.com/simple-computer")

    logo = page.get_by_alt_text("Tricentis Demo Web Shop")
    expect(logo).to_be_visible()

    page.wait_for_timeout(3000)

    searchbox = page.locator("input#small-searchterms")
    searchbox.fill("simple computer")
    searchbox.press("Enter")

    page.wait_for_timeout(10000)

    computer = page.get_by_alt_text("Picture of Simple Computer")
    expect(computer).to_be_visible()