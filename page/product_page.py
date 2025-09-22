from playwright.sync_api import Page, Locator

class ProductLocator:
    def __init__(self, page: Page):
        self.page = page
        self.locator_cart_badge_count = page.locator(".shopping_cart_badge")
        self.locator_sort_dropdown = page.locator(".product_sort_container")
        self.locator_product_title = page.locator(".inventory_item_name")
        self.locator_cart_badge_link = page.locator(".shopping_cart_link")

    def get_add_to_cart_button(self, product_name: str) -> Locator:
        return (
            self.page.locator("div.inventory_item")
            .filter(has_text=product_name)
            .locator("button", has_text="ADD TO CART")     
    )

    def get_remove_from_cart_button(self, product_name: str) -> Locator:
        return (
            self.page.locator("div.inventory_item")
            .filter(has_text=product_name)
            .locator("button", has_text="REMOVE")
    )

    def get_product_link(self, product_name: str) -> Locator:
        return self.page.locator(".inventory_item_name", has_text=product_name)

    def get_product_image(self, product_name: str) -> Locator:
        return (
            self.page.locator("div.inventory_item")
            .filter(has_text=product_name)
            .locator("img.inventory_item_img")
        )

    def get_detail_add_to_cart_button(self) -> Locator:
        return self.page.locator("button.btn_primary.btn_inventory")

    def get_detail_remove_button(self) -> Locator:
        return self.page.locator("button.btn_secondary.btn_inventory")