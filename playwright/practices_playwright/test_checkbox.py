from playwright.sync_api import Page, expect


def test_checkbox1(practice_page: Page):

    smartphone_checkbox = practice_page.get_by_role(
        "row", name="Smartphone $10.99"
    ).get_by_role("checkbox")

    expect(smartphone_checkbox).to_be_visible()
    expect(smartphone_checkbox).to_be_enabled()
    expect(smartphone_checkbox).not_to_be_checked()

    smartphone_checkbox.check()

    expect(smartphone_checkbox).to_be_checked()


def test_checkbox2(practice_page: Page):

    laptop_checkbox = practice_page.get_by_role(
        "row", name="Laptop $19.99"
    ).get_by_role("checkbox")

    expect(laptop_checkbox).to_be_visible()
    expect(laptop_checkbox).to_be_enabled()
    expect(laptop_checkbox).not_to_be_checked()

    laptop_checkbox.check()

    expect(laptop_checkbox).to_be_checked()