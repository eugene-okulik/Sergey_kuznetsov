from playwright.sync_api import Page, expect, Dialog, BrowserContext


def test_check_alert(page: Page):
    def alert_accept(alert: Dialog):
        alert.accept()

    page.on('dialog', alert_accept)
    page.goto("https://www.qa-practice.com/elements/alert/confirm")
    page.get_by_role('link', name="Click").click()
    text = page.locator("#result-text")
    expect(text).to_have_text("Ok")


def test_new_tab(page: Page, context: BrowserContext):
    page.goto('https://www.qa-practice.com/elements/new_tab/button')
    link = page.locator("#new-page-button")
    with context.expect_page() as new_page_event:
        link.click()
    new_page = new_page_event.value
    result = new_page.locator('#result-text')
    expect(result).to_have_text('I am a new page in a new tab')
    new_page.close()
    expect(link).not_to_be_disabled()


def test_color_change(page: Page):
    page.goto('https://demoqa.com/dynamic-properties')
    button = page.locator("#colorChange")
    expect(button).to_have_css('color', 'rgb(220, 53, 69)', timeout=10000)
    button.click()
