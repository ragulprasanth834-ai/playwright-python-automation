from playwright.sync_api import expect, Page
import pytest

login_test_data = [
    ("laura.taylor123@example.com", "test123", "valid"),
    ("invaliduser@example.com", "test321", "invalid"),
    ("validuser@example.com", "testxyz", "invalid")
]

@pytest.mark.parametrize("email,password,validity", login_test_data)
def test_logindatadriven(email, password, validity, demowebshoploginpage: Page):

    # Fill the login form
    demowebshoploginpage.locator("#Email").fill(email)
    demowebshoploginpage.locator("#Password").fill(password)
    demowebshoploginpage.locator("input[value='Log in']").click()

    # Validation
    if validity == "valid":
        logout_text = demowebshoploginpage.locator(".ico-logout")
        expect(logout_text).to_have_text("Log out", timeout=5000)
    else:
        error_msg = demowebshoploginpage.locator("div.validation-summary-errors span")
        expect(error_msg).to_have_text(
            "Login was unsuccessful. Please correct the errors and try again."
        )
        expect(demowebshoploginpage).to_have_url("https://demowebshop.tricentis.com/login")
