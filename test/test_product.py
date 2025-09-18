import pytest
from playwright.sync_api import expect
from keywords.product_keyword import ProductKeyword
from data.product_data import ProductData

# TC_Product_001
@pytest.mark.asyncio
def test_add_product_to_cart(page):
    product_action = ProductKeyword(page)
    product_data = ProductData()

    product_action.goto_product_page()
    product_action.add_product_to_cart(product_data.single_product)

    expect(page.get_by_role("link", name="1")).to_be_visible()
    expect(page.get_by_role("button", name="REMOVE")).to_be_visible()