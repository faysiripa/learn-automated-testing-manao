from playwright.sync_api import Page
from page.product_page import ProductLocator

class ProductKeyword:
    product_url = "https://www.saucedemo.com/v1/inventory.html"

    def __init__(self, page:Page):
        self.page = page
        self.product_page = ProductLocator(page)

    def goto_product_page(self, url=product_url):
        self.page.goto(url)

    def add_to_cart(self, page: Page, product_name: str):
        button_selector = self.product_page.add_to_cart_button(product_name)
        page.click(button_selector)

# class VerifyProductKeyword:
    


    # def add_product_to_cart(self, product_name):
    #     add_to_cart_button_locator = self.product_page.add_to_cart_button_for(product_name)
    #     add_to_cart_button_locator.click()

    # def add_multiple_products_to_cart(self, product_list):
    #     for product in product_list:
    #         self.add_product_to_cart(product)

    # def get_cart_badge_count(self):
    #     cart_badge_count = self.product_page.locator_cart_badge_count
    #     return int(cart_badge_count.inner_text()) if cart_badge_count.is_visible() else 0
    
# class VerifyProductKeyword:
#     def __init__(self, page):
#         self.page = page
#         self.product_page = ProductLocator(page)

#     def verify_cart_count(self, expected_count):
#         cart_badge_count = self.product_page.locator_cart_badge_count
#         actual_count = int(cart_badge_count.inner_text()) if cart_badge_count.is_visible() else 0
#         assert actual_count == expected_count, f"Expected cart count {expected_count}, but got {actual_count}"

#     def verify_add_button_changed_to_remove(self, product_name):
#         button_for = self.product_page.button_for(product_name)
#         button_text = button_for.inner_text()
#         assert button_text.lower() == "remove", f"Add button for '{product_name}' did not change to Remove"