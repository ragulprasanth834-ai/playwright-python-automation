"""Page Object for the PIM (Employee list / Add Employee) module."""

from playwright.sync_api import Page, expect
from pages.base_page import BasePage


class PimPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        # Add Employee
        self.add_employee_button = page.get_by_role("button", name="Add")
        self.first_name_input = page.get_by_placeholder("First Name")
        self.last_name_input = page.get_by_placeholder("Last Name")
        self.save_button = page.get_by_role("button", name="Save")

        # Employee details
        self.employee_name_header = page.locator(
            ".orangehrm-edit-employee-name h6"
        )

        # Employee search
        self.search_employee_name = page.get_by_placeholder(
            "Type for hints..."
        )
        self.search_button = page.get_by_role("button", name="Search")
        self.employee_table_rows = page.locator(".oxd-table-card")

    def add_employee(self, first_name: str, last_name: str):
        """Add a new employee and wait for the employee details page."""

        self.click(self.add_employee_button)

        self.expect_visible(self.first_name_input)
        self.fill(self.first_name_input, first_name)
        self.fill(self.last_name_input, last_name)

        self.click(self.save_button)

        # Wait until the employee details page is loaded.
        self.expect_visible(self.employee_name_header)

    def get_employee_name(self) -> str:
        """Return the employee name displayed on the details page."""
        return self.get_text(self.employee_name_header)

    def search_by_name(self, name: str):
        """Search for an employee by name."""

        self.fill(self.search_employee_name, name)

        # OrangeHRM may display an autocomplete dropdown.
        # Escape closes it before clicking Search.
        self.page.keyboard.press("Escape")

        self.click(self.search_button)

        # Wait for the search request/results to finish.
        self.page.wait_for_load_state("networkidle")

    def get_result_count(self) -> int:
        """Return the number of employee rows currently displayed."""
        return self.employee_table_rows.count()

    def expect_employee_in_results(self, employee_name: str):
        """Verify that an employee with the given name appears in results."""

        employee_row = self.employee_table_rows.filter(
            has_text=employee_name
        )

        expect(employee_row.first).to_be_visible()