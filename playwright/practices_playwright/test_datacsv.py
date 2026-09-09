import csv
import pytest
from playwright.sync_api import expect, Page

# Load test data from CSV file
login_test_data = []
with open("login_test_data.csv", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        login_test_data.append((row["email"], row["password"], row["validity"]))# type:ignore

@pytest.mark.parametrize("email,password,validity", login_test_data)# type:ignore
def test_logindatadriven(email, password, validity, demowebshoploginpage: Page):# type:ignore

    # Fill the login form
    demowebshoploginpage.locator("#Email").fill(email)# type:ignore
    demowebshoploginpage.locator("#Password").fill(password)# type:ignore
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
