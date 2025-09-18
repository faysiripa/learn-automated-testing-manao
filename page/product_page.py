from playwright.sync_api import Page

class ProductLocator:
    def __init__(self, page: Page):
        self.page = page
        self.locator_add_to_cart_button = page.locator("div:nth-child(6) > .pricebar > .btn_primary")
        self.locator_cart_badge = page.locator(".shopping_cart_badge")

 
