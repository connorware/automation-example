from pages.login_page import LoginPage
from playwright.sync_api import expect
import time

def test_login(page, base_url):
    lp = LoginPage(page, base_url)
    lp.open()
    
    lp.login("tomsmith", "SuperSecretPassword!")
    time.sleep(10)
    expect(page).to_have_url(f"{base_url}/secure")
    
    