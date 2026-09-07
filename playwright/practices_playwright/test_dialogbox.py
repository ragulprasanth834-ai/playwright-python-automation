from playwright.sync_api import Page,expect
import pytest
@pytest.mark.skip
def test_sampledilague(practiceplaywright:Page):
    practiceplaywright.on("dialog",lambda dialog:dialog.accept())

    #practiceplaywright.locator("#alertBtn").click()
    button = practiceplaywright.locator("#confirmBtn")
    button.click()
    

    expect(practiceplaywright.locator("#demo")).to_have_text("You pressed OK!")

    practiceplaywright.wait_for_timeout(10000)


def test_prompt(practiceplaywright:Page):
    name = "Ragul prasanth"
    practiceplaywright.on("dialog",lambda dialog:dialog.accept(name))

    
    button = practiceplaywright.locator("#promptBtn")
    button.click()
    
    practiceplaywright.wait_for_timeout(5000)
    text = practiceplaywright.locator("#demo")
    expect(text).to_have_text(f"Hello {name}! How are you today?")
    print(text)
    practiceplaywright.wait_for_timeout(3000)