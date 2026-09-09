from playwright.sync_api import Page, expect
import pytest

search_items = ["laptop", "camera", "smartphone", "monitor"]

@pytest.mark.parametrize("item", search_items)
def test_with_data(item, demowebshop: Page):# type: ignore
    # Fill the search input box with the given item
    demowebshop.locator("#small-searchterms").fill(item)# type: ignore
    
    # Click the Search button
    demowebshop.locator("input[value='Search']").click()
    
    # Assert that the first search result contains the search term (case-insensitive)
    first_result = demowebshop.locator("h2 a").first
    expect(first_result).to_contain_text(item, ignore_case=True)# type: ignore
