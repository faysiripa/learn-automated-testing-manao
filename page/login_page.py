from playwright.sync_api import Page

class LoginLocator:
    def __init__(self, page: Page):
        self.page = page
        self.locator_username_input = self.page.locator("#user-name")
        self.locator_password_input = self.page.locator("#password")
        self.locator_login_button = self.page.locator("#login-button")
        self.locator_error_message = self.page.locator('[data-test="error"]')