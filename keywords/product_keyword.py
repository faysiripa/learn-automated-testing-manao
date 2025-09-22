from playwright.sync_api import Page, expect
from page.product_page import ProductLocator

class ProductKeyword:
    product_url = "https://www.saucedemo.com/v1/inventory.html"

    def __init__(self, page:Page):
        self.page = page
        self.product_page = ProductLocator(page)

    def goto_product_page(self, url=product_url):
        self.page.goto(url)

    def add_single_or_multiple_products_to_cart(self, products: list[str]):
        for product in products:
            self.product_page.get_add_to_cart_button(product).click()

    def get_cart_badge_count(self) -> int:
        badge = self.product_page.locator_cart_badge_count
        if badge.is_visible():
            return int(badge.inner_text())
        return 0
    
    def remove_single_or_multiple_products_from_cart(self, products: str):
        for product in products:
            self.product_page.get_remove_from_cart_button(product).click()

    def select_sorting(self, sort_type: str):
        self.product_page.locator_sort_dropdown.select_option(sort_type)

    def get_all_product_names(self) -> list[str]:
        expect(self.product_page.locator_product_title.first).to_be_visible()
        return self.product_page.locator_product_title.all_inner_texts()
    
    def goto_product_detail_by_name(self, product_name: str):
        self.product_page.get_product_link(product_name).click()

    def goto_product_detail_by_image(self, product_name: str):
        self.product_page.get_product_image(product_name).click()

    def add_product_from_detail(self):
        self.product_page.get_detail_add_to_cart_button().click()

    def remove_product_from_detail(self):
        self.product_page.get_detail_remove_button().click()

    def goto_cart_page(self):
        self.product_page.locator_cart_badge_link.click()

    def click_back_to_products(self):
        self.product_page.locator_back_button.click()
        
    
