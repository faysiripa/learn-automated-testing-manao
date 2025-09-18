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
        self.product_page.locator_add_to_cart_button.click()

    def get_cart_badge_count(self) -> int:
        badge = self.page.locator_cart_badge
        if badge.is_visible():
            return int(badge.inner_text())
        return 0