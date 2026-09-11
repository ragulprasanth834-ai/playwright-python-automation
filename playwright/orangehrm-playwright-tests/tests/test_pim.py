```python
import time

import pytest

from pages.dashboard_page import DashboardPage
from pages.pim_page import PimPage


@pytest.mark.regression
def test_add_new_employee(logged_in_page):
    dashboard_page = DashboardPage(logged_in_page)
    dashboard_page.go_to_module("PIM")

    pim_page = PimPage(logged_in_page)

    # Create a unique employee name for every test run
    first_name = f"Test{int(time.time())}"
    last_name = "Automation"
    full_name = f"{first_name} {last_name}"

    # Add employee
    pim_page.add_employee(first_name, last_name)

    # Verify employee was created successfully
    assert full_name in pim_page.get_employee_name()


@pytest.mark.regression
def test_search_employee_by_name(logged_in_page):
    dashboard_page = DashboardPage(logged_in_page)
    dashboard_page.go_to_module("PIM")

    pim_page = PimPage(logged_in_page)

    # Create a unique employee for this test
    first_name = f"Search{int(time.time())}"
    last_name = "Automation"
    full_name = f"{first_name} {last_name}"

    # Add employee
    pim_page.add_employee(first_name, last_name)

    # Go back to PIM employee list
    dashboard_page.go_to_module("PIM")

    # Search for the employee
    pim_page.search_by_name(full_name)

    # Verify that search returned at least one result
    assert pim_page.get_result_count() > 0

    # Verify the expected employee is present in the results
    pim_page.expect_employee_in_results(full_name)
```
