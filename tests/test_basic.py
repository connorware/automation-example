from pages.login_page import LoginPage
from pages.home_page import HomePage
from playwright.sync_api import expect
import time

def test_login(page, base_url):
    lp = LoginPage(page, base_url)
    lp.open()
    lp.login("tomsmith", "SuperSecretPassword!")
    # assertions to confirm test login successful
    expect(page).to_have_url(f"{base_url}/secure")

def test_wrong_login(page, base_url):
    # Test incorrect password scenario
    lp = LoginPage(page, base_url)
    lp.open()
    lp.login("tomsmith","abcdef")
    # Check invalid text - inside elemet with id "flash"
    expect(page.locator("#flash")).to_contain_text("Your password is invalid!")

def test_open_home(page, base_url):
    home = HomePage(page, base_url)
    # open page using open method - this uses polymorphism, inheritance, 
    home.open()
    expect(page.get_by_role("heading", name="Welcome to the-internet")).to_be_visible()
    
    
    