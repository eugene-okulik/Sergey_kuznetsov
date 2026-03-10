from playwright.sync_api import Page


def test_login(page: Page):
    page.goto('https://the-internet.herokuapp.com/')
    page.get_by_role('link', name='Form Authentication').click()
    page.get_by_role('textbox', name='username').fill('login')
    page.get_by_role('textbox', name='password').fill('password')
    page.get_by_role('button', name="submit")


def test_form(page: Page):
    page.goto('https://demoqa.com/automation-practice-form')
    page.get_by_placeholder('First Name').fill("Sergey")
    page.get_by_placeholder('Last Name').fill("Kuznetsov")
    page.get_by_placeholder('name@example.com').fill("Serkuz@mail.com")
    page.locator('//*[@id="gender-radio-1"]').click()
    page.get_by_placeholder('Mobile Number').fill("88005553535")
    page.locator('//*[@id="dateOfBirthInput"]').fill("2026-03-10")
    subject_field = page.locator('//*[@id="subjectsInput"]')
    subject_field.fill("Physics")
    subject_field.press("Enter")
    page.locator('//*[@id="hobbies-checkbox-1"]').click()
    page.get_by_placeholder('Current Address').fill("Minsk city")
    page.locator('//*[@id="state"]').click()
    page.get_by_text('Haryana').click()
    page.locator('//*[@id="city"]').click()
    page.get_by_text('Panipat').click()
    page.locator('//*[@id="submit"]').click()
