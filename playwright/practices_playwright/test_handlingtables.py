from playwright.sync_api import Page, expect


# =========================================================
# TEST 1 - Count rows in the table
# =========================================================
def test_count_rows(practice_page1: Page):

    # Go to Web Table
    webtable_tab = practice_page1.get_by_text("Web Table", exact=True)

    expect(webtable_tab).to_be_visible()
    webtable_tab.click()

    # Locate table
    table1 = practice_page1.locator("#bookingTable")

    expect(table1).to_be_visible()

    # Locate rows
    rows = table1.locator("tbody tr")

    # Count rows
    rowcount = rows.count()

    print("Number of rows in table:", rowcount)

    # Header + 4 data rows = 5
    expect(rows).to_have_count(5)


# =========================================================
# TEST 2 - Count columns in the table
# =========================================================
def test_count_columns(practice_page1: Page):

    # Go to Web Table
    webtable_tab = practice_page1.get_by_text("Web Table", exact=True)

    expect(webtable_tab).to_be_visible()
    webtable_tab.click()

    # Locate table
    table1 = practice_page1.locator("#bookingTable")

    expect(table1).to_be_visible()

    # Locate header columns
    columns = table1.locator("tbody tr:first-child th")

    # Count columns
    column_count = columns.count()

    print("Number of columns in table:", column_count)

    # Verify column count
    expect(columns).to_have_count(4)


# =========================================================
# TEST 3 - Read data from second data row
# =========================================================
def test_read_second_row(practice_page1: Page):

    # Go to Web Table
    webtable_tab = practice_page1.get_by_text("Web Table", exact=True)

    expect(webtable_tab).to_be_visible()
    webtable_tab.click()

    # Locate rows
    table1 = practice_page1.locator("#bookingTable")
    rows = table1.locator("tbody tr")

    # Second data row
    # nth(0) = header
    # nth(1) = BK1001
    # nth(2) = BK1002
    secondrow_cells = rows.nth(2).locator("td")

    # Read text
    secondrow_text = secondrow_cells.all_inner_texts()

    print("Second row data:", secondrow_text)

    # Verify data
    expect(secondrow_cells).to_have_text(
        ["BK1002", "Mumbai to Goa", "3200", "Pending"]
    )

    # Print each cell
    for i, cell in enumerate(secondrow_text, start=1):
        print(f"Column {i}: {cell}")


# =========================================================
# TEST 4 - Read all data from table
# =========================================================
def test_read_all_table_data(practice_page1: Page):

    # Go to Web Table
    webtable_tab = practice_page1.get_by_text("Web Table", exact=True)

    expect(webtable_tab).to_be_visible()
    webtable_tab.click()

    # Locate table rows
    table1 = practice_page1.locator("#bookingTable")
    rows = table1.locator("tbody tr")

    # Get all rows
    all_rows = rows.all()

    # Read each row
    for row_number, row in enumerate(all_rows, start=1):

        # Get cells
        cols = row.locator("td").all_inner_texts()

        print(f"Row {row_number}: {cols}")