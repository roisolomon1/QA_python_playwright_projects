from playwright.sync_api import Page

class ProductPage:
    def __init__(self, page: Page):
        self.page = page
        self.add_to_cart_button = page.get_by_role("link", name="Add to cart")
        self.product_name = page.locator("h2.name")

    def click_add_to_cart(self):
        # Set up a listener for the dialog before clicking
        self.page.once("dialog", lambda dialog: dialog.accept())
        self.add_to_cart_button.click()
