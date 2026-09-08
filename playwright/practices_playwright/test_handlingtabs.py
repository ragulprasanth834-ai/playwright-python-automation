from playwright.sync_api import Playwright


def test_handlingtab(playwright: Playwright):

    browser = playwright.chromium.launch(headless=False)

    context = browser.new_context()

    parent_page = context.new_page()

    parent_page.goto(
        "https://testautomationpractice.blogspot.com/p/playwrightpractice.html"
    )

    parent_page.wait_for_load_state("domcontentloaded")

    # Print parent page details
    print("Number of tabs before opening child:", len(context.pages))
    print("Title of parent page:", parent_page.title())
    print("URL of parent page:", parent_page.url)

    # Example: click a link/button that opens a new tab
    # Replace the locator below with the actual element on the page.
    with context.expect_page() as new_page_info:
        parent_page.locator("a[target='_blank']").first.click()

    child_page = new_page_info.value

    child_page.wait_for_load_state("domcontentloaded")

    # Get all pages/tabs
    all_pages = context.pages

    print("Number of tabs after opening child:", len(all_pages))
    print("Title of parent page:", all_pages[0].title())
    print("URL of child page:", all_pages[1].url)

    browser.close()