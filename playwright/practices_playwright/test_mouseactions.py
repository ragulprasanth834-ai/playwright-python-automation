from playwright.sync_api import Page,expect
import pytest

@pytest.mark.skip
def test_mousehover(practiceplaywright: Page):
    
    practiceplaywright.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
    practiceplaywright.wait_for_load_state("networkidle")
    pointme = practiceplaywright.locator("button:has-text('Point Me')")
    pointme.hover()
    practiceplaywright.wait_for_timeout(2000)
    laptop = practiceplaywright.locator("div[id='HTML3'] a:nth-child(2)")
    laptop.hover()
    practiceplaywright.wait_for_timeout(2000)
    laptop.click()
@pytest.mark.skip
def test_doubleclick(practiceplaywright:Page):
    btn = practiceplaywright.locator("button[ondblclick='myFunction1()']")
    btn.dblclick()
    practiceplaywright.wait_for_timeout(3000)
    text = practiceplaywright.locator("#field2")
    expect(text).to_have_value("Hello World!")

def test_draganddrop(practiceplaywright:Page):

    source = practiceplaywright.locator("div[id='draggable'] p")
    target = practiceplaywright.locator("#droppable")
    source.drag_to(target)
'''

def test_right_left_middle(practiceplaywright:Page):
    btn = practiceplaywright.locator("button[ondblclick='myFunction1()']")
    btn.click(button="left") 
    btn.click(button="right")
    btn.click(button="middle")
    practiceplaywright.wait_for_timeout(3000)
    text = practiceplaywright.locator("#field2")
    expect(text).to_have_value("Hello World!")
'''