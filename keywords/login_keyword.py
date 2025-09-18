from page.login_page import LoginLocator

class LoginKeyword:
    login_url = "https://www.saucedemo.com/v1/"

    def __init__(self, page):
        self.page = page
        self.login_page = LoginLocator(page)

    def goto_login_page(self, url=login_url):
        self.page.goto(url)

    def login(self, username, password):
        self.login_page.locator_username_input.fill(username)
        self.login_page.locator_password_input.fill(password)
        self.login_page.locator_login_button.click()

class VerifyKeyword:
    def __init__(self, page):
        self.page = page
        self.login_page = LoginLocator(page)

    def verify_url(self, expected_url):
        assert self.page.url == expected_url, f"Expected URL {expected_url}, but got {self.page.url}"

    def verify_title(self, expected_title):
        assert self.page.title() == expected_title, f"Expected title '{expected_title}', but got '{self.page.title}'"

    def verify_error_message(self, expected_error):
        actual_error = self.login_page.locator_error_message
        assert actual_error.inner_text() == expected_error, f"Expected error message '{expected_error}', but got '{actual_error}'"