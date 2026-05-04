from test_UI_Kuznetsov_Sergey_pw.Page_Object_Model_PW.pages.base_page import BasePage
from playwright.sync_api import expect


class ItemPage(BasePage):
    page_url = '/shop/category/desks-1'
    sort_by_list = '//*[@title="List"]'
    active_sort_by_list = '//*[@class="btn btn-light o_wsale_apply_list active"]'
    cart_button_for_item = '(//*[@class="btn btn-primary a-submit"])[1]'
    add_to_cart_pop_up = '//*[@class="modal-dialog modal-lg"]'
    proceed_to_checkout_button = '//*[@class="btn btn-primary o_sale_product_configurator_edit"]'
    order_overview_tab = '//*[@class="mb-4"]'
    counter_for_cart = '.my_cart_quantity.badge:first-of-type'
    customizable_desk_card = '//*[@content="Customizable Desk"]'
    cus_desk = '//*[@id="wrapwrap"]'
    legs_for_desk = '//*[@data-value_id="2"]'
    color_for_desk = '//*[@data-value_id="4"]'
    error_text = '//*[@class="css_not_available_msg alert alert-warning"]'
    add_cart_button = '//*[@id="add_to_cart"]'

    def sort_by_title_list_select(self):
        self.page.locator(self.sort_by_list).click()

    def active_list_sorting_check(self):
        self.page.locator(self.active_sort_by_list)

    def cart_button_for_item_desk_click(self):
        self.page.locator(self.cart_button_for_item).click()

    def add_product_to_cart(self):
        self.page.locator(self.add_to_cart_pop_up)
        self.page.locator(self.proceed_to_checkout_button).click()

    def order_overview_tab_view(self):
        return self.page.locator(self.order_overview_tab)

    def cart_counter(self):
        return self.page.locator(self.counter_for_cart).first

    def customizable_desk_card_select(self):
        self.page.locator(self.customizable_desk_card).click()

    def select_legs_for_desk(self):
        self.page.locator(self.legs_for_desk).click()

    def select_color_for_desk(self):
        self.page.locator(self.color_for_desk).click()

    def error_texts(self):
        return self.page.text_content(self.error_text)

    def button_add_cart_check(self):
        expect(self.page.locator(self.add_cart_button)).to_be_visible()

    def should_item_in_cart(self):
        expect(self.order_overview_tab_view()).to_be_attached()
        expect(self.cart_counter()).to_be_attached()

    def check_error_text(self, text):
        expect(self.page.locator(self.error_text)).to_have_text(text)
