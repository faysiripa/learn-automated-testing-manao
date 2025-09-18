from playwright.sync_api import Page, Locator

class ProductLocator:
    def __init__(self, page: Page):
        self.page = page
        self.locator_add_to_cart_button = page.locator("div:nth-child(6) > .pricebar > .btn_primary")
        self.locator_cart_badge = page.locator(".shopping_cart_badge")

    def get_add_to_cart_button(self, product_name: str) -> Locator:
        return (
            self.page.locator("div.inventory_item")
            .filter(has_text=product_name)
            .locator("button.btn_inventory", has_text="ADD TO CART")
    )

    def get_remove_from_cart_button(self, product_name: str) -> Locator:
        return (
            self.page.locator("div.inventory_item")
            .filter(has_text=product_name)
            .locator("button.btn_inventory", has_text="REMOVE")
    )


 
