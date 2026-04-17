def test_search_item(cart_page):
    cart_page.open_page()
    cart_page.button_search()
    cart_page.input_search("Conference chair")
    cart_page.first_element_select()
    cart_page.should_have_header("Conference Chair")


def test_check_logo(cart_page):
    cart_page.open_page()
    cart_page.head_logo_click()
    cart_page.current_urls("/")


def test_check_desks(cart_page):
    cart_page.open_page()
    cart_page.menu_dropdown_hover()
    cart_page.button_desks_click()
    cart_page.current_urls("/shop/category/desks-1")


def test_add_to_card_item_from_list(item_page):
    item_page.open_page()
    item_page.sort_by_title_list_select()
    item_page.active_list_sorting_check()
    item_page.cart_button_for_item_desk_click()
    item_page.add_product_to_cart()
    item_page.should_item_in_cart()


def test_add_to_card_ended_item(item_page):
    item_page.open_page()
    item_page.customizable_desk_card_select()
    item_page.select_legs_for_desk()
    item_page.select_color_for_desk()
    item_page.check_error_text('This combination does not exist.')


def test_add_to_cart_some_items(item_page):
    item_page.open_page()
    item_page.customizable_desk_card_select()
    item_page.select_legs_for_desk()
    item_page.button_add_cart_check()


def test_check_cart_via_popup(category_page):
    category_page.open_page()
    category_page.add_item_to_cart()
    category_page.click_the_view_cart_button()
    category_page.check_added_item()


def test_remove_from_cart(category_page):
    category_page.open_page()
    category_page.add_item_to_cart()
    category_page.click_the_view_cart_button()
    category_page.check_added_item()
    category_page.click_remove_button()
    category_page.check_empty_cart('Your cart is empty!')


def test_change_item_via_search(category_page):
    category_page.open_page()
    category_page.enter_text_to_search_field("Office")
    category_page.click_search_button()
    category_page.select_third_element()
    category_page.check_text_for_url('office-chair')
