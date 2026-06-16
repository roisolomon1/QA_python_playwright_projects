import pytest
from demoblaze_automation.pages.home_page import HomePage
from demoblaze_automation.pages.product_page import ProductPage
from demoblaze_automation.pages.cart_page import CartPage
from demoblaze_automation.globals import BASE_URL
from playwright.sync_api import expect

def test_add_laptop_to_cart(page):
    home_page = HomePage(page)
    product_page = ProductPage(page)
    cart_page = CartPage(page)

    page.goto(BASE_URL)

    # Click Laptops category
    home_page.laptops_category.click()
    # Wait for the first laptop to be visible after category filter
    page.wait_for_timeout(2000) # Simple wait for category to load

    # Click on the first laptop item
    expected_product_name = home_page.first_product_link.inner_text()
    home_page.first_product_link.click()

    # Verify we are on the product page and it's the correct product
    expect(product_page.product_name).to_have_text(expected_product_name)

    # Click Add to Cart and handle alert
    product_page.click_add_to_cart()

    # Go to Cart
    home_page.click_cart()

    # Check if item is in the cart
    cart_item_names = cart_page.get_item_names()
    assert expected_product_name in cart_item_names, f"Expected {expected_product_name} to be in cart, but found {cart_item_names}"

    # Click Place Order
    cart_page.place_order_button.click()
    page.wait_for_selector("#orderModal", state="visible")

    # Fill in fake checkout details
    cart_page.name_field.fill("Fake User")
    cart_page.country_field.fill("Fake Country")
    cart_page.city_field.fill("Fake City")
    cart_page.card_field.fill("1234567890123456")
    cart_page.month_field.fill("12")
    cart_page.year_field.fill("2026")

    # Click Purchase
    cart_page.purchase_button.click()

    # Verify success message
    expect(cart_page.success_message).to_have_text("Thank you for your purchase!")
    
    # Click OK to finish
    cart_page.ok_button.click()
    expect(page).to_have_url(f"{BASE_URL}index.html")
