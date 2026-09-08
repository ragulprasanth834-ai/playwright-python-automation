from playwright.sync_api import Playwright

def test_testpopus(playwright:Playwright):

    browser = playwright.chromium.launch(headless=False)

    contex = browser.new_context()

    page = contex.new_page()

    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")

    page.on("popup",lambda popup:popup.wait_for_load_state())

    page.locator("#PopUp").click()

    page.wait_for_timeout(5000)

    allpopup = contex.pages

    print(f"total popus is ====> {len(allpopup)}")

    page.wait_for_timeout(3000)

    for i in allpopup:
        title = i.title()
        print(title)

    contex.close()

    browser.close()
