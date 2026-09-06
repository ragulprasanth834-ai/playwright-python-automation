from playwright.sync_api import Page


def test_verify_pagedestinationtable(assertqa: Page):

    page_number = 1

    while True:

        print(f"\n=== Page {page_number} ===")

        rows = assertqa.locator("table tbody tr")

        print(f"Found {rows.count()} rows")

        for i in range(rows.count()):
            print(f"Row {i + 1}: {rows.nth(i).inner_text()}")

        # Check pagination
        print("Pagination text:", assertqa.get_by_text(
            f"Page {page_number} of 3"
        ).inner_text())

        # Find Next button
        next_button = assertqa.locator("button[data-cy='pagination-next'] svg")

        print("Next button count:", next_button.count())

        # If Next button does not exist, stop
        if next_button.count() == 0:
            print("No Next button. Finished.")
            break

        # If Next button is disabled, stop
        if next_button.is_disabled():
            print("Next button is disabled. Finished.")
            break

        # Click Next
        next_button.click()

        # Wait for next page data
        assertqa.wait_for_timeout(500)

        page_number += 1