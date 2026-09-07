from playwright.sync_api import Page


def test_keyboardaction(practiceplaywright:Page):

    #locate input
    searchbox = practiceplaywright.locator("input[placeholder='Search products...']")
    searchbox.press("Control+A")
    searchbox.press("Backspace")
    practiceplaywright.wait_for_timeout(2000)
    searchbox.fill("omega3 tablets")
    searchbox.press("Enter")
    practiceplaywright.wait_for_timeout(5000)