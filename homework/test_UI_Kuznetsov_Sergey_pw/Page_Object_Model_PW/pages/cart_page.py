from test_UI_Kuznetsov_Sergey_pw.Page_Object_Model_PW.pages.base_page import BasePage
from playwright.sync_api import expect


class CartPage(BasePage):
    page_url = '/shop/cart'
    search_button = '//*[@data-bs-target="#o_search_modal"]'
    input_search_field = ('//*[@class="search-query form-control oe_search_box border-0 bg-light'
                          ' border border-end-0 p-3"]')
    first_element = '//*[@class="d-flex align-items-center flex-wrap o_search_result_item"]'
    head_page = 'h1'
    header_logo = '//*[@class="navbar-brand logo me-4"]'
    dropdown_menu = ".nav-link.dropdown-toggle"
    desks_button = 'Desks'

    def button_search(self):
        self.page.locator(self.search_button).click()

    def input_search(self, text):
        field = self.page.locator(self.input_search_field)
        field.fill(text)

    def first_element_select(self):
        self.page.locator(self.first_element).click()

    def header_page(self):
        return self.page.text_content(self.head_page)

    def head_logo_click(self):
        self.page.locator(self.header_logo).click()

    def menu_dropdown_hover(self):
        self.page.locator(self.dropdown_menu).first.hover()

    def button_desks_click(self):
        self.page.locator("nav").first.get_by_text(self.desks_button).click()

    def should_have_header(self, expected_title):
        expect(self.page.locator(self.head_page)).to_have_text(expected_title)
