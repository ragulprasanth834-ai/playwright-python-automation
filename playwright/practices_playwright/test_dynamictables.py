from playwright.sync_api import Page, expect


def test_dynamic_table(practiceplaywright: Page):

    # Get all headers to find the CPU column index
    headers = practiceplaywright.locator("#taskTable thead th").all()
    
    cpu_column_index = None
    for i, header in enumerate(headers):
        if "CPU" in header.inner_text():
            cpu_column_index = i
            break
    
    # Ensure we found the CPU column
    assert cpu_column_index is not None, "CPU column not found in the table"
    
    # Find Chrome row
    chrome_row = practiceplaywright.locator(
        "#taskTable tbody tr"
    ).filter(has_text="Chrome")
    
    # Get Chrome CPU value from the correct column
    cpu_load = chrome_row.locator("td").nth(cpu_column_index).inner_text()
    
    print("CPU load of Chrome ===>", cpu_load)
    
    # Get displayed CPU value
    displayed_cpu = practiceplaywright.locator(
        "p",
        has_text="CPU load of Chrome process:"
    ).locator("strong")
    
    print("Displayed CPU ===>", displayed_cpu.inner_text())
    
    # Compare
    expect(displayed_cpu).to_have_text(cpu_load)