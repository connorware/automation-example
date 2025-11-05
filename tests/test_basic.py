from pages.login_page import LoginPage
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
    
    
    