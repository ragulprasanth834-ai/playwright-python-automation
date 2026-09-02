from playwright.sync_api import Page,expect

def test_url(page:Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    expect(page).to_have_url("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

def test_login(page:Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.wait_for_timeout(3000)
    page.get_by_placeholder("Username").fill("admin")
    page.get_by_placeholder("Password").fill("admin123")
    page.get_by_role("button",name="login").click()

    page.wait_for_timeout(10000)
    expect(page.get_by_role("heading",name="Dashboard")).to_be_visible()
    
