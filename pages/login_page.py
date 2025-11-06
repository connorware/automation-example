from playwright.sync_api import Page

# Login page POM
class LoginPage:
    # Initialise and create instance attributes
    def __init__(self, page: Page, base_url):
        self.page = page
        self.base_url = base_url
        self.username = page.get_by_role("textbox", name="Username")
        self.password = page.get_by_role("textbox", name="Password")
        self.login_button = page.get_by_role("button", name=" Login")

    def open(self):
        self.page.goto(f"{self.base_url}/login")

    def login(self, user, pwd):
        self.username.fill(user)
        self.password.fill(pwd)
        self.login_button.click()

 
        

