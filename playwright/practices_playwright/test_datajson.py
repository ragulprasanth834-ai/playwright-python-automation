import json
import pytest
from playwright.sync_api import expect, Page

# Load test data from JSON file
with open("test.json", "r") as f:
    login_test_data = json.load(f)

@pytest.mark.parametrize("data", login_test_data)
def test_logindatadriven(data, demowebshoploginpage: Page):# type: ignore
    email = data["email"]# type: ignore
    password = data["password"]# type: ignore
    validity = data["validity"]# type: ignore

    # Fill the login form
    demowebshoploginpage.locator("#Email").fill(email)# type: ignore
    demowebshoploginpage.locator("#Password").fill(password)# type: ignore
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
