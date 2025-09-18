import pytest
from actions.product_keyword import ProductKeyword, VerifyProductKeyword
from data.product_data import ProductData
from page.product_page import ProductLocator

# TC_Product_001
@pytest.mark.parametrize("data", single_product_data)
def test_add_single_product(page, data):
    product_action = ProductKeyword(page)
    verify = VerifyProductKeyword(page)

    product_action.goto_product_page()
    product_action.add_product_to_cart(data.product_name)

    verify.verify_cart_count(data.expected_cart_count)
    verify.verify_add_button_changed_to_remove(data.product_name)

# TC_Product_002
@pytest.mark.parametrize("data", multiple_product_data)
def test_add_multiple_products(page, data):
    product_action = ProductKeyword(page)
    verify = VerifyProductKeyword(page)

    product_action.goto_product_page()
    product_action.add_multiple_products_to_cart(data.product_name_list)

    verify.verify_cart_count(data.expected_cart_count)
    for product in data.product_name_list:
        verify.verify_add_button_changed_to_remove(product)