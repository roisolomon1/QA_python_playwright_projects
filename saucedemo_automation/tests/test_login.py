import pytest
from playwright.sync_api import expect
from saucedemo_automation.pages.login_page import LoginPage
from saucedemo_automation.globals import URL

def test_successful_login(page):
    page.goto(URL)
    login_page = LoginPage(page)
    login_page.login("standard_user", "secret_sauce")
    
    # Verify login success by checking the URL or a specific element on the inventory page
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    inventory_title = page.locator(".title")
    expect(inventory_title).to_have_text("Products")
