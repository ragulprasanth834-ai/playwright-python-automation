from playwright.sync_api import Page, expect


# ---------------------------------------------------------
# TEST 1: Login and navigate to PIM
# ---------------------------------------------------------
def test_navigate_to_pim(orangehrm: Page):

    # Login
    orangehrm.locator("input[name='username']").fill("Admin")
    orangehrm.locator("input[name='password']").fill("admin123")
    orangehrm.locator("button[type='submit']").click()

    # Verify login completed
    expect(
        orangehrm.get_by_role("heading", name="Dashboard")
    ).to_be_visible()

    # Click PIM
    orangehrm.get_by_role("link", name="PIM").click()

    # Verify PIM page
    expect(
        orangehrm.get_by_role("heading", name="PIM")
    ).to_be_visible()


# ---------------------------------------------------------
# TEST 2: Open the dropdown
# ---------------------------------------------------------
def test_open_dropdown(orangehrm: Page):

    # Login
    orangehrm.locator("input[name='username']").fill("Admin")
    orangehrm.locator("input[name='password']").fill("admin123")
    orangehrm.locator("button[type='submit']").click()

    # Verify login completed
    expect(
        orangehrm.get_by_role("heading", name="Dashboard")
    ).to_be_visible()

    # Go to PIM
    orangehrm.get_by_role("link", name="PIM").click()

    # Verify PIM page
    expect(
        orangehrm.get_by_role("heading", name="PIM")
    ).to_be_visible()

    # Open dropdown
    orangehrm.locator("form i").nth(2).click()

    # Locate dropdown
    options = orangehrm.locator("div[role='listbox']")

    # Verify dropdown is visible
    expect(options).to_be_visible()


# ---------------------------------------------------------
# TEST 3: Verify number of listboxes
# ---------------------------------------------------------
def test_dropdown_count(orangehrm: Page):

    # Login
    orangehrm.locator("input[name='username']").fill("Admin")
    orangehrm.locator("input[name='password']").fill("admin123")
    orangehrm.locator("button[type='submit']").click()

    # Verify login completed
    expect(
        orangehrm.get_by_role("heading", name="Dashboard")
    ).to_be_visible()

    # Go to PIM
    orangehrm.get_by_role("link", name="PIM").click()

    # Verify PIM page
    expect(
        orangehrm.get_by_role("heading", name="PIM")
    ).to_be_visible()

    # Open dropdown
    orangehrm.locator("form i").nth(2).click()

    # Locate listbox
    options = orangehrm.locator("div[role='listbox']")

    # Verify visible
    expect(options).to_be_visible()

    # Get count
    count = options.count()

    print("Number of listboxes:", count)

    # Verify expected count
    expect(options).to_have_count(1)


# ---------------------------------------------------------
# TEST 4: Get all dropdown options
# ---------------------------------------------------------
def test_get_all_dropdown_options(orangehrm: Page):

    # Login
    orangehrm.locator("input[name='username']").fill("Admin")
    orangehrm.locator("input[name='password']").fill("admin123")
    orangehrm.locator("button[type='submit']").click()

    # Verify login completed
    expect(
        orangehrm.get_by_role("heading", name="Dashboard")
    ).to_be_visible()

    # Go to PIM
    orangehrm.get_by_role("link", name="PIM").click()

    # Verify PIM page
    expect(
        orangehrm.get_by_role("heading", name="PIM")
    ).to_be_visible()

    # Open dropdown
    orangehrm.locator("form i").nth(2).click()

    # Locate individual options
    options = orangehrm.locator(
        "div[role='listbox'] div[role='option']"
    )

    # Verify at least one option is visible
    expect(options.first).to_be_visible()

    # Get all option text
    listoptions = [
        text.strip()
        for text in options.all_text_contents()
    ]

    # Print all options
    for i, option in enumerate(listoptions, start=1):
        print(f"Option {i}: {option}")


# ---------------------------------------------------------
# TEST 5: Select Finance Manager
# ---------------------------------------------------------
def test_select_finance_manager(orangehrm: Page):

    # Login
    orangehrm.locator("input[name='username']").fill("Admin")
    orangehrm.locator("input[name='password']").fill("admin123")
    orangehrm.locator("button[type='submit']").click()

    # Verify login completed
    expect(
        orangehrm.get_by_role("heading", name="Dashboard")
    ).to_be_visible()

    # Go to PIM
    orangehrm.get_by_role("link", name="PIM").click()

    # Verify PIM page
    expect(
        orangehrm.get_by_role("heading", name="PIM")
    ).to_be_visible()

    # Open dropdown
    orangehrm.locator("form i").nth(2).click()

    # Locate dropdown options
    options = orangehrm.locator(
        "div[role='listbox'] div[role='option']"
    )

    # Verify dropdown is visible
    expect(options.first).to_be_visible()

    # Find and click Finance Manager
    for i in range(options.count()):

        text = options.nth(i).inner_text().strip()

        if text == "Finance Manager":
            options.nth(i).click()
            break