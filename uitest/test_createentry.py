import re
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto("https://playwright.dev/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Playwright"))

def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/")

    # Click the get started link.
    page.get_by_role("link", name="Get started").click()

    # Expects page to have a heading with the name of Installation.
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()


def test_login(page: Page):
    #browser = p.chromium.launch()
    #page = browser.new_page()
    #launch browserstack demo
    page.goto("https://bstackdemo.com/")
    #click on sign button
    page.click('#signin')
    #select Username
    page.get_by_text("Select Username").click()
    page.locator("#react-select-2-option-0-0").click()
    #select Password
    page.get_by_text("Select Password").click()
    page.locator("#react-select-3-option-0-0").click()
    #click login
    page.get_by_role("button", name="Log In").click()
    #verify user have logged in
    assert page.get_by_text("demouser").is_visible()