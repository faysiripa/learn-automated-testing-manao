from playwright.sync_api import Page

class ProductLocator:
    def __init__(self, page: Page):
        self.page = page
        # self.locator_add_to_cart_button = self.page.get_by_role("button", name="ADD TO CART")
        # self.locator_remove_button = self.page.get_by_role("button", name="REMOVE")
        # self.locator_cart_badge = self.page.locator("#shopping_cart_container").get_by_role("link")
        # self.locator_cart_badge_count = self.page.locator(".shopping_cart_badge")
        # self.locator_product_name = self.page.locator(".inventory_item_name")
        self.locator_cart_badge = self.page.locator(".shopping_cart_badge")

    def add_to_cart_button_for(self, product_name):
        # return self.page.locator(f".inventory_item:has-text('{product_name}') button:has-text('Add to cart')")
        return f"//div[text()='{product_name}']/ancestor::div[@class='inventory_item']//button"
    

    def button_for(self, product_name):
        return f"{self.locator_product_name}:has-text('{product_name}') {self.locator_remove_button}"

 
