from playwright.sync_api import Page, Locator, expect


class BasePage:
    base_url = 'http://testshop.qa-practice.com'
    page_url = None

    def __init__(self, page: Page):
        self.page = page

    def open_page(self):
        if self.page_url:
            self.page.goto(f'{self.base_url}{self.page_url}')
        else:
            raise NotImplementedError("Page can not be opened")

    def find_wait(self, locator: str) -> Locator:
        return self.page.locator(locator)

    def click(self, locator: str):
        self.find_wait(locator).click()

    def hover(self, locator: str):
        self.find_wait(locator).hover()

    def current_urls(self, page_url: str):
        expect(self.page).to_have_url(f"{self.base_url}{page_url}")
