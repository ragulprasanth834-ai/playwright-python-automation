from playwright.sync_api import Page, expect
import pytest

@pytest.mark.skip
def test_dropdownoptions(practice_page1: Page):

    dropdown_tab = practice_page1.get_by_text("Dropdown", exact=True)

    expect(dropdown_tab).to_be_visible()
    dropdown_tab.click()

    practice_page1.wait_for_timeout(2000)

    # Locate all options
    dropdown_options = practice_page1.locator("#departCity option")

    # Get option count
    count = dropdown_options.count()
    print("Number of options:", count)

    # Get option text
    option_text = [
        text.strip()
        for text in dropdown_options.all_text_contents()
    ]

    print("Available options are =======>", option_text)

    # Verify
    expect(dropdown_options).to_have_count(5)


@pytest.mark.skip
def test_multiselectdropdown(practice_page1:Page):
    dropdown_tab = practice_page1.get_by_text("Dropdown", exact=True)

    expect(dropdown_tab).to_be_visible()
    dropdown_tab.click()

    practice_page1.wait_for_timeout(2000)

    # Locate all options
    dropdown_multiselect = practice_page1.locator("#services")
    dropdown_multiselect.select_option(["wifi","Airport pickup"])
    practice_page1.wait_for_timeout(10000)

def test_dropdownlis_sorted(practice_page1:Page):
    dropdown_tab = practice_page1.get_by_text("Dropdown", exact=True)

    expect(dropdown_tab).to_be_visible()
    dropdown_tab.click()

    practice_page1.wait_for_timeout(2000)
    # Locate all options
    dropdown_option = practice_page1.locator("#services>option")

    option_text =[text.strip() for text in dropdown_option.all_text_contents()]

    original_list = option_text
    sorted_list = sorted(option_text)

    print("original list ======> ",original_list)    
    print("sorted list ======> ",sorted_list)

    if original_list == sorted_list:
        print("The options are sorted ")
    else:
        print("The options are not sorted")  