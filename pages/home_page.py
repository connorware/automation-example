from .base_page import BasePage
from playwright.sync_api import Page

# Homepage POM
class HomePage(BasePage):
    heading_text = "Welcome to the-internet"

    def __init__(self, page: Page, base_url):
        super().__init__(page, base_url)

    def open(self):
        self.open_url()