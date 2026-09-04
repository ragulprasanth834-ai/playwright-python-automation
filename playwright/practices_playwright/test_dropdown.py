from playwright.sync_api import Page, expect

def test_dropdown(practice_page1: Page):

    dropdown_tab = practice_page1.get_by_text("Dropdown", exact=True)

    expect(dropdown_tab).to_be_visible()
    dropdown_tab.click()

    practice_page1.wait_for_timeout(2000)

    departed = practice_page1.locator("#departCity")
    departed.select_option("Bengaluru")
    practice_page1.wait_for_timeout(5000)
    airline = practice_page1.locator("#airline")
    airline.select_option("airindia")
    practice_page1.wait_for_timeout(5000)