from playwright.sync_api import Page

class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.home_button = page.get_by_role("link", name="Home")
        self.contact_button = page.get_by_role("link", name="Contact")
        self.about_us_button = page.get_by_role("link", name="About us")
        self.cart_button = page.get_by_role("link", name="Cart", exact=True)
        self.login_button = page.get_by_role("link", name="Log in")
        self.signup_button = page.get_by_role("link", name="Sign up")
        self.laptops_category = page.get_by_role("link", name="Laptops")
        self.first_product_link = page.locator(".card-title a").first
        self.contact_email_field = page.locator("#recipient-email")
        self.contact_name_field = page.locator("#recipient-name")
        self.contact_message_field = page.locator("#message-text")
        self.send_message_button = page.get_by_role("button", name="Send message")

    def click_home(self):
        self.home_button.click()

    def click_contact(self):
        self.contact_button.click()

    def click_about_us(self):
        self.about_us_button.click()

    def click_cart(self):
        self.cart_button.click()

    def click_login(self):
        self.login_button.click()

    def click_signup(self):
        self.signup_button.click()
