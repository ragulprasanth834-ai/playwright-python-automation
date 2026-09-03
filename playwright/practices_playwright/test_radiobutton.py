from playwright.sync_api import Page, expect


def test_radio_button_visible(practice_page: Page):

    radiobutton1 = practice_page.locator("input[value='express']")
    radiobutton2 = practice_page.locator("input[value='express']")

    expect(radiobutton1).to_be_visible()
    expect(radiobutton2).to_be_visible()


def test_radio_button_unchecked(practice_page: Page):

    radiobutton1 = practice_page.locator("input[value='express']")
    radiobutton2 = practice_page.locator("input[value='express']")

    expect(radiobutton1).not_to_be_checked()
    expect(radiobutton2).not_to_be_checked()


def test_checking_radio_button(practice_page: Page):

    radiobutton2 = practice_page.locator("input[value='express']")

    radiobutton2.check()

    expect(radiobutton2).to_be_checked()