import pytest
from demoblaze_automation.pages.home_page import HomePage
from demoblaze_automation.globals import BASE_URL
from playwright.sync_api import expect

@pytest.fixture(autouse=True)
def go_home(page):
    page.goto(BASE_URL)

def test_home_button(page):
    home_page = HomePage(page)
    expect(home_page.home_button).to_be_visible()
    home_page.click_home()
    expect(page).to_have_url(f"{BASE_URL}index.html")

def test_contact_button(page):
    home_page = HomePage(page)
    expect(home_page.contact_button).to_be_visible()
    home_page.click_contact()
    expect(page.locator("#exampleModal")).to_be_visible()
    page.locator("#exampleModal").get_by_text("Close", exact=True).click()
    expect(page.locator("#exampleModal")).not_to_be_visible()

def test_about_us_button(page):
    home_page = HomePage(page)
    expect(home_page.about_us_button).to_be_visible()
    home_page.click_about_us()
    expect(page.locator("#videoModal")).to_be_visible()
    page.locator("#videoModal").get_by_text("Close", exact=True).click()
    expect(page.locator("#videoModal")).not_to_be_visible()

def test_cart_button(page):
    home_page = HomePage(page)
    expect(home_page.cart_button).to_be_visible()
    home_page.click_cart()
    expect(page).to_have_url(f"{BASE_URL}cart.html")

def test_login_button(page):
    home_page = HomePage(page)
    expect(home_page.login_button).to_be_visible()
    home_page.click_login()
    expect(page.locator("#logInModal")).to_be_visible()
    page.locator("#logInModal").get_by_text("Close", exact=True).click()
    expect(page.locator("#logInModal")).not_to_be_visible()


def test_signup_button(page):
    home_page = HomePage(page)
    expect(home_page.signup_button).to_be_visible()
    home_page.click_signup()
    expect(page.locator("#signInModal")).to_be_visible()
    page.locator("#signInModal").get_by_text("Close", exact=True).click()
    expect(page.locator("#signInModal")).not_to_be_visible()
