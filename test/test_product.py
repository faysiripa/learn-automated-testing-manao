import pytest
from playwright.sync_api import expect
from keywords.product_keyword import ProductKeyword
from data.product_data import ProductData
from page.product_page import ProductLocator

# TC_Product_001 - 002
@pytest.mark.parametrize("products", [
    ProductData.TC_Product_001_test_data,   # TC_Product_001 : Add a product to cart
    ProductData.TC_Product_002_test_data    # TC_Product_002 : Add multiple products to cart
])
def test_add_products_to_cart(page, products):
    product_action = ProductKeyword(page)
    product_locator = ProductLocator(page)

    product_action.goto_product_page()
    product_action.add_single_or_multiple_products_to_cart(products)

    count = product_action.get_cart_badge_count()
    assert count == len(products), f"Expected {len(products)} items in cart, but got {count}"

    for product in products:
        remove_button = product_locator.get_remove_from_cart_button(product)
        expect(remove_button).to_be_visible()

# TC_Product_003 : Remove products from cart until 0
def test_remove_products_from_cart(page):
    product_action = ProductKeyword(page)
    product_data = ProductData()
    product_locator = ProductLocator(page)

    # Step 1: ไปหน้า product
    product_action.goto_product_page()

    # Step 2: ใส่สินค้าก่อน (จาก TC001 + TC002)
    products_in_cart = product_data.TC_Product_001_test_data + product_data.TC_Product_002_test_data
    product_action.add_single_or_multiple_products_to_cart(products_in_cart)

    # Verify ว่ามีสินค้า 6 ชิ้นใน cart
    count = product_action.get_cart_badge_count()
    assert count == len(products_in_cart), f"Expected {len(products_in_cart)} items in cart, but got {count}"

    # Step 3: ลบสินค้าตาม TC003 จน cart เหลือ 1
    product_action.remove_single_or_multiple_products_from_cart(product_data.TC_Product_003_test_data)

    # Verify ว่า cart badge เหลือ 1
    assert product_action.get_cart_badge_count() == 1, "Cart should contain only 1 item (the red T-Shirt)"

    # ลบตัวสุดท้าย
    product_action.remove_single_or_multiple_products_from_cart(product_data.TC_Product_001_test_data)

    # Verify ว่า cart badge เหลือ 0
    assert product_action.get_cart_badge_count() == 0, "Cart should be empty"

    # Step 4: ปุ่ม Remove กลับเป็น Add to Cart
    for product in products_in_cart:
        add_button = product_locator.get_add_to_cart_button(product)
        expect(add_button).to_be_visible()

# TC_Product_004 : Sorting by Name (A to Z)
def test_sort_products_A_to_Z(page):
    product_action = ProductKeyword(page)
    product_data = ProductData()

    product_action.goto_product_page()
    product_action.select_sorting("az")  # Name (A to Z)

    product_names = product_action.get_all_product_names()
    assert product_names == product_data.TC_Sort_A_to_Z_test_data, f"Expected {product_data.TC_Sort_A_to_Z_test_data}, but got {product_names}"

# TC_Product_005 : Sorting by Name (Z to A)
def test_sort_products_Z_to_A(page):
    product_action = ProductKeyword(page)
    product_data = ProductData()

    product_action.goto_product_page()
    product_action.select_sorting("za")  # Name (Z to A)

    product_names = product_action.get_all_product_names()
    assert product_names == product_data.TC_Sort_Z_to_A_test_data, f"Expected {product_data.TC_Sort_Z_to_A_test_data}, but got {product_names}"