class HelpPage():
    def __init__(self, page):
        self.page = page

    def search_help(self,item):
        self.page.get_by_role("textbox", name="What can we help you with?").click()
        self.page.get_by_role("textbox", name="What can we help you with?").fill(item)
        self.page.get_by_role("textbox", name="What can we help you with?").press("Enter")
