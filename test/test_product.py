import pytest
from playwright.sync_api import expect
from keywords.product_keyword import ProductKeyword
from data.product_data import ProductData
from page.product_page import ProductLocator

# TC_Product_001 - 002
import pytest

@pytest.mark.parametrize("products", [
    ProductData.TC_Product_001_test_data,  
    ProductData.TC_Product_002_test_data
])
def test_add_products_to_cart(page, products):
    product_action = ProductKeyword(page)
    product_locator = ProductLocator(page)

    product_action.goto_product_page()
    product_action.add_single_or_multiple_products_to_cart(products)

    count = product_action.get_cart_badge_count()
    assert count == len(products), f"Expected {len(products)} items in cart, but got {count}"

    for product in products:
        remove_button = product_locator.get_remove_from_cart_button(product_name=product)
        expect(remove_button).to_be_visible()