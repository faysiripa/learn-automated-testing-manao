from playwright.sync_api import Page
from page.product_page import ProductLocator

class ProductKeyword:
    product_url = "https://www.saucedemo.com/v1/inventory.html"

    def __init__(self, page:Page):
        self.page = page
        self.product_page = ProductLocator(page)

    def goto_product_page(self, url=product_url):
        self.page.goto(url)

    def add_product_to_cart(self, product_name: str):
        self.product_page.get_add_to_cart_button(product_name).click()

    def add_single_or_multiple_products_to_cart(self, products: list[str]):
        for product in products:
            self.add_product_to_cart(product)

    def get_cart_badge_count(self) -> int:
        badge = self.product_page.locator_cart_badge
        if badge.is_visible():
            return int(badge.inner_text())
        return 0
    
    def remove_product_from_cart(self, product_name: str):
        self.product_page.get_remove_from_cart_button(product_name).click()
