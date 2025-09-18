# valid login
class ValidLoginData:
    def __init__(self, username, password, expected_url, expected_title):
        self.username = username
        self.password = password
        self.expected_url = expected_url 
        self.expected_title = expected_title

# invalid login
class InvalidLoginData:
    def __init__(self, username, password, expected_error):
        self.username = username
        self.password = password
        self.expected_error = expected_error

# valid login data test : TC_Login_001_data_test 
standard_user = ValidLoginData( 
    username="standard_user",
    password="secret_sauce",
    expected_url="https://www.saucedemo.com/v1/inventory.html",
    expected_title="Swag Labs"
)

# TC_Login_002_data_test
problem_user = ValidLoginData( 
    username="problem_user",
    password="secret_sauce",
    expected_url="https://www.saucedemo.com/v1/inventory.html",
    expected_title="Swag Labs"
)

# TC_Login_003_data_test
performance_glitch_user = ValidLoginData(
    username="performance_glitch_user",
    password="secret_sauce",
    expected_url="https://www.saucedemo.com/v1/inventory.html",
    expected_title="Swag Labs"
)

# invalid login data test : TC_Login_004_data_test
invalid_username = InvalidLoginData("invalid", "secret_sauce",
                             "Epic sadface: Username and password do not match any user in this service")

# TC_Login_005_data_test
invalid_password = InvalidLoginData("standard_user", "invalid",
                             "Epic sadface: Username and password do not match any user in this service")
# TC_Login_006_data_test
invalid_both = InvalidLoginData("invalid", "invalid",
                         "Epic sadface: Username and password do not match any user in this service")
# TC_Login_007_data_test
empty_username = InvalidLoginData("", "secret_sauce",
                           "Epic sadface: Username is required")
# TC_Login_008_data_test
empty_password = InvalidLoginData("standard_user", "",
                           "Epic sadface: Password is required")
# TC_Login_009_data_test
empty_both = InvalidLoginData("", "",
                       "Epic sadface: Username is required")
# TC_Login_010_data_test
locked_user = InvalidLoginData("locked_out_user", "secret_sauce",
                        "Epic sadface: Sorry, this user has been locked out.")

# valid login data list
valid_login_data = [standard_user, problem_user, performance_glitch_user]

# invalid login data list
invalid_login_data = [
    invalid_username,
    invalid_password,
    invalid_both,
    empty_username,
    empty_password,
    empty_both,
    locked_user
]