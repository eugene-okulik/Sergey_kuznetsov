import re
from playwright.sync_api import expect
from test_UI_Kuznetsov_Sergey_pw.Page_Object_Model_PW.pages.base_page import BasePage


class CotegPage(BasePage):
    page_url = '/shop/furn-9999-office-design-software-7?category=9'

    card_tab = '//*[@class="col-lg-6 mt-md-4"]'
    add_to_cart_button = '//*[@id="add_to_cart"]'
    alert = '//*[@role="alert"]'
    view_cart_button = '//*[@class="w-100 btn btn-primary"]'
    added_item = '//*[@id="cart_products"]'
    remove_button = '//*[@title="Remove from cart"]'
    empty_cart = '.js_cart_lines.alert-info'
    search_field = '//*[@data-search-type="products"]'
    search_button = '//*[@class="btn oe_search_button btn btn-light"]'
    new_page = '//*[@class="container oe_website_sale pt-2"]'
    three_element = '(//*[@class="oe_product"])[3]'

    def add_item_to_cart(self):
        self.page.locator(self.card_tab)
        self.page.locator(self.add_to_cart_button).click()

    def click_the_view_cart_button(self):
        self.page.locator(self.alert)
        self.page.locator(self.view_cart_button).click()

    def check_added_item(self):
        expect(self.page.locator(self.added_item))

    def click_remove_button(self):
        self.page.locator(self.remove_button).click()

    def check_empty_cart(self, text):
        expect(self.page.locator(self.empty_cart)).to_have_text(text)

    def enter_text_to_search_field(self, text):
        self.page.locator(self.search_field).fill(text)

    def click_search_button(self):
        self.page.locator(self.search_button).click()

    def select_third_element(self):
        self.page.locator(self.three_element).click()

    def check_text_for_url(self, text):
        expect(self.page).to_have_url(re.compile(f".*{text}.*"))
