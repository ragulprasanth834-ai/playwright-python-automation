import pytest
from pages.dashboard_page import DashboardPage


@pytest.mark.smoke
def test_dashboard_loads_after_login(logged_in_page):
    dashboard_page = DashboardPage(logged_in_page)
    assert dashboard_page.is_loaded()
    assert "Dashboard" in dashboard_page.get_header_text()


@pytest.mark.regression
@pytest.mark.parametrize(
    "module_name,expected_header",
    [
        ("Admin", "Admin"),
        ("PIM", "PIM"),
        ("Leave", "Leave"),
        ("Recruitment", "Recruitment"),
    ],
)
def test_sidebar_navigation(logged_in_page, module_name, expected_header):
    dashboard_page = DashboardPage(logged_in_page)
    dashboard_page.go_to_module(module_name)
    dashboard_page.expect_visible(dashboard_page.header)
    assert expected_header in dashboard_page.get_header_text()
