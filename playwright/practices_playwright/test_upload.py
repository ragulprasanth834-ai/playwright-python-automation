from playwright.sync_api import Page, expect



def test_uploadsinglefile(practiceplaywright: Page):
    practiceplaywright.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
    
    practiceplaywright.locator("#singleFileInput").set_input_files("rext1.txt")
    practiceplaywright.locator("form[id='singleFileForm'] button[type='submit']").click()
    
    status = practiceplaywright.locator("#singleFileStatus")
    expect(status).to_contain_text("rext1.txt")


def test_uploadmultiplefile(practiceplaywright: Page):
    practiceplaywright.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
    
    files = ["rext1.txt", "rext2.txt"]
    practiceplaywright.locator("#multipleFilesInput").set_input_files(files)
    practiceplaywright.locator("form[id='multipleFilesForm'] button[type='submit']").click()
    
    msg = practiceplaywright.locator("#multipleFilesStatus")
    expect(msg).to_contain_text("rext1.txt")
    expect(msg).to_contain_text("rext2.txt")