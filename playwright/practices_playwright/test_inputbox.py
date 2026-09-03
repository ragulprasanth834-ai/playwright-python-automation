from playwright.sync_api import Page, expect


def test_check_visibility(practice_page: Page):
    text_box = practice_page.locator("#username")

    expect(text_box).to_be_visible()


def test_check_enabled(practice_page: Page):
    text_box = practice_page.locator("#username")

    expect(text_box).to_be_enabled()


def test_enter_text(practice_page: Page):
    text_box = practice_page.locator("#username")

    text_box.fill("Ragul")

    expect(text_box).to_have_value("Ragul")