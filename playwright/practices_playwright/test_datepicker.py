from playwright.sync_api import Page,expect
import pytest

@pytest.mark.skip
def selectdate(qaplayground,year,month,date,is_feature):
    pass

@pytest.mark.skip
def test_datepicker(qaplayground:Page):
    datepicker = qaplayground.locator("#dp-basic-input")
    is_fuature = False
    year = "2024"
    month ="october"
    date ="15"

    datepicker.click()
    selectdate(qaplayground,year,month,date,is_fuature)
    print("selected date ====> ",datepicker.input_value())     
    expect(datepicker).to_have_value("10/15/2024")
    qaplayground.wait_for_timeout(5000)



def test_date(qaplayground: Page):
    datepicker = qaplayground.locator("#dp-basic-input")
    
    # Using set_input_files for date input (works in some cases)
    datepicker.set_input_files("1999-11-10")
    
    # Verify
    expect(datepicker).to_have_value("1999-11-10")