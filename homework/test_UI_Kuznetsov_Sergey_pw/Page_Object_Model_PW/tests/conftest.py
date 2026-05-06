import pytest
from test_UI_Kuznetsov_Sergey_pw.Page_Object_Model_PW.pages.cart_page import CartPage
from test_UI_Kuznetsov_Sergey_pw.Page_Object_Model_PW.pages.item_page import ItemPage
from test_UI_Kuznetsov_Sergey_pw.Page_Object_Model_PW.pages.category_page import CotegPage


@pytest.fixture()
def cart_page(page):
    return CartPage(page)


@pytest.fixture()
def item_page(page):
    return ItemPage(page)


@pytest.fixture()
def category_page(page):
    return CotegPage(page)
