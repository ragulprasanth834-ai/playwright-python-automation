from playwright.sync_api import Page, expect


def test_frames(page: Page):

    page.goto("https://ui.vision/demo/webtest/frames/")

    for frame in page.frames:

        print("Frame name:", frame.name)
        print("Frame URL:", frame.url)

        if frame.name == "frame1":

            inputbox = frame.locator("input[name='mytest']")

            inputbox.fill("welcome")

            expect(inputbox).to_have_value("welcome")

            break