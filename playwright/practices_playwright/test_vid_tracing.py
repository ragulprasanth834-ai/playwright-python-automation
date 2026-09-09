from playwright.sync_api import Playwright, expect


def test_vid_tracing(playwright: Playwright):

    browser = playwright.chromium.launch(headless=False)

    context = browser.new_context(
        record_video_dir="videos",
        record_video_size={
            "width": 1024,
            "height": 768
        }
    )

    # Start tracing
    context.tracing.start(
        screenshots=True,
        snapshots=True,
        sources=True
    )

    page = context.new_page()

    try:
        # Open DemoBlaze
        page.goto("https://demoblaze.com/")

        page.wait_for_timeout(5000)

        # Open Login popup
        page.locator("#login2").click()

        # Enter username
        page.locator("#loginusername").fill("pavanol")

        # Enter password
        page.locator("#loginpassword").fill("test@123")

        # Click Login
        page.locator("button[onclick='logIn()']").dblclick()

        # Wait for login response
        page.wait_for_timeout(3000)

        # Check login
        expect(page.locator("#logout2")).to_be_visible()
        expect(page.locator("#nameofuser")).to_contain_text(
            "Welcome pavanol"
        )

        print("Login successful")

    finally:
        # ALWAYS save trace, even if test fails
        context.tracing.stop(path="trace.zip")

        # Close context to finalize video
        context.close()

        browser.close()