from playwright.sync_api import Page 

class BasePage():
    # Add base page for repeated functions across all pages
    def __init__(self, page: Page, base_url):
        self.page = page
        self.base_url = base_url

    # function to open all pages easier
    def open_url(self, path = "/"):
        self.page.goto(f"{self.base_url}{path}")
        