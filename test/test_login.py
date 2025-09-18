import pytest
from data.login_data import valid_login_data, invalid_login_data
from keywords.login_keyword import LoginKeyword, VerifyKeyword

# TC_Login_001 - 003
@pytest.mark.parametrize("data", valid_login_data)
def test_valid_login(page, data):
    login_action = LoginKeyword(page)
    verify = VerifyKeyword(page)

    login_action.goto_login_page()
    login_action.login(data.username, data.password)

    verify.verify_url(data.expected_url)
    verify.verify_title(data.expected_title)

# TC_Login_004 - 010
@pytest.mark.parametrize("data", invalid_login_data)
def test_invalid_login(page, data):
    login_action = LoginKeyword(page)
    verify = VerifyKeyword(page)

    login_action.goto_login_page()
    login_action.login(data.username, data.password)

    verify.verify_error_message(data.expected_error)