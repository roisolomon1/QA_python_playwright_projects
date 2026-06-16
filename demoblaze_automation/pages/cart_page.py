from playwright.sync_api import Page

class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.cart_items = page.locator("#tbodyid tr")
        self.place_order_button = page.get_by_role("button", name="Place Order")
        self.name_field = page.locator("#name")
        self.country_field = page.locator("#country")
        self.city_field = page.locator("#city")
        self.card_field = page.locator("#card")
        self.month_field = page.locator("#month")
        self.year_field = page.locator("#year")
        self.purchase_button = page.get_by_role("button", name="Purchase")
        self.success_message = page.locator(".sweet-alert h2")
        self.ok_button = page.get_by_role("button", name="OK")

    def get_item_names(self):
        # Wait for the table to have at least one row
        self.page.wait_for_selector("#tbodyid tr", state="visible")
        # Return a list of text from the second column (product name)
        return self.page.locator("#tbodyid tr td:nth-child(2)").all_inner_texts()
