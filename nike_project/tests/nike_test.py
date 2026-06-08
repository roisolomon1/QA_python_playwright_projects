from playwright.sync_api import expect
from nike_project.globals import URL
from nike_project.pages.golf_page import GolfPage
from nike_project.pages.help_page import HelpPage
from nike_project.pages.home_page import HomePage
from nike_project.pages.page_after_search import page_after_search_item


# all around the project there are

    # ⚡ Interesting test
    # =====================

    # statements to show the more interesting tests , each show a different concept at least a bit different

class Test_General():

    # ⚡ Interesting test
    # =====================

    # def test_shop_button_engineered_to_win(self,setup_playwright):
    #     page = setup_playwright
    #     page.goto(URL)
    #     home_page = HomePage(page)
    #     home_page.shop_engineered_click()
    #
    #     expect(page).to_have_url("https://www.nike.com/il/w/golf-23q9w")
    #
    #     golf_page = GolfPage(page)
    #
    #     category_name = "Accessories & Equipment"
    #     golf_page.click_category_and_gender(category_name)
    #     key_words_category = category_name.replace("&"," ").split()
    #     url_lower = page.url.lower()
    #     print("h")
    #     for word in key_words_category:
    #         assert word.lower() in url_lower
    #
    #     gender = "Men"
    #     golf_page.choose_gender_golf(gender)
    #     url_lower = page.url.lower()
    #     assert gender.lower() in url_lower

    # ⚡ Interesting test
    # =====================

    def test_click_on_item_size(self,setup_playwright):
        page = setup_playwright
        page.goto(URL)
        home_page = HomePage(page)
        element1,element2 = home_page.search_item("shirt")
        expect(element1).to_contain_text("shirt",ignore_case=True)
        expect(element2).to_contain_text("shirt",ignore_case=True)

        page_after_search = page_after_search_item(page)
        size = "M"
        page_after_search.click_on_item_and_pick_size(size)

        # the page is creating a new element after select and not changing attribute of the old one
        new_element_for_size = page.locator('[data-testid="pdp-grid-selector-item-selected"]').locator(f'[for="grid-selector-input-{size}"]')
        expect(new_element_for_size).to_be_visible()

    # ⚡ Interesting test
    # =====================

    def test_bag_items_count_at_start(self,setup_playwright):
        page = setup_playwright
        page.goto(URL)
        home_page = HomePage(page)
        bag_items_count = home_page.bag_items_count()
        title_value = bag_items_count.get_attribute("title")

        assert title_value == "Bag Items: 0","bag not empty at first open"

    def test_home_button_nike_symbol(self,setup_playwright):
        page = setup_playwright
        page.goto("https://www.nike.com/il/w?q=shoes&vst=shoes")
        page_after_search = page_after_search_item(page)
        page_after_search.home_button()

        expect(page).to_have_url("https://www.nike.com/il/")

    # ⚡ Interesting test
    # =====================

    def test_sort_and_color_after_search(self,setup_playwright):
        page = setup_playwright
        page.goto(URL)
        home_page = HomePage(page)
        element1, element2 = home_page.search_item("shoes")

        expect(element1).to_contain_text("shoe", ignore_case=True)
        expect(element2).to_contain_text("shoe", ignore_case=True)

        page_after_search = page_after_search_item(page)
        sort_category = "Price: High-Low"
        after_select = page_after_search.sort_after_item_search(sort_category)

        expect(after_select).to_contain_text(sort_category)

        color1,color2 = page_after_search.pick_a_color("Red","Pink")

        expect(color1,color2).to_have_attribute("class","filter-item is--color is--selected is--button css-5faxmh")

        selected = page.locator('.filter-item.is--color.is--selected.is--button')

        assert selected.count() == 2, "error more or less than 2 colors are selected"

    def test_jordan_button(self,setup_playwright):
        page = setup_playwright
        page.goto(URL)
        home_page = HomePage(page)
        home_page.jordan_click()

        expect(page).to_have_url("https://www.nike.com/il/jordan")

    # ⚡ Interesting test
    # =====================

    def test_change_gender_after_search(self,setup_playwright):
        page = setup_playwright
        page.goto(URL)
        home_page = HomePage(page)
        element1, element2 = home_page.search_item("shoes")

        expect(element1).to_contain_text("shoe", ignore_case=True)
        expect(element2).to_contain_text("shoe", ignore_case=True)

        page_after_search = page_after_search_item(page)
        page_after_search.choose_gender_after_search("Men")

        expect(page).to_have_url("https://www.nike.com/il/w/mens-nik1?q=shoes")


class Test_Nike_Right_Buttons():

    # ⚡ Interesting test
    # =====================

    def test_search_for_item(self,setup_playwright):
        page = setup_playwright
        page.goto(URL)
        home_page = HomePage(page)
        element1,element2 = home_page.search_item("shoes")

        expect(element1).to_contain_text("shoe",ignore_case=True)
        expect(element2).to_contain_text("shoe",ignore_case=True)

    def test_favourites_button(self,setup_playwright):
        page = setup_playwright
        page.goto(URL)
        home_page = HomePage(page)
        home_page.favourites_button()

        expect(page).to_have_url("https://www.nike.com/il/favorites")

    def test_bag_items_click(self,setup_playwright):
        page = setup_playwright
        page.goto(URL)
        home_page = HomePage(page)
        home_page.bag_items()

        expect(page).to_have_url("https://www.nike.com/il/cart")

class Test_Upper_Menu():

    def test_find_a_store(self,setup_playwright):
        page = setup_playwright
        page.goto(URL)
        home_page = HomePage(page)
        home_page.find_a_store()

        expect(page).to_have_url("https://www.nike.com/il/retail")

    def test_help(self,setup_playwright):
        page = setup_playwright
        page.goto(URL)
        home_page = HomePage(page)
        home_page.help_button()

        expect(page).to_have_url("https://www.nike.com/il/help")

    def test_join_us(self,setup_playwright):
        page = setup_playwright
        page.goto(URL)
        home_page = HomePage(page)
        home_page.join_us()

        expect(page).to_have_url("https://www.nike.com/il/membership")

    def test_sign_in_click(self,setup_playwright):
        page = setup_playwright
        page.goto(URL)
        home_page = HomePage(page)
        email_input = home_page.sign_in()

        expect(email_input).to_be_visible()

class Test_Menu_Buttons():

    # ⚡ Interesting test
    # =====================

    # for new, and kids category's

    def test_new_and_kids_buttons(self,setup_playwright):
        page = setup_playwright
        page.goto(URL)
        home_page = HomePage(page)
        category = "New"
        home_page.all_buttons_click(category)

        assert category.lower() in page.url.lower()


    def test_men_button_click(self,setup_playwright):
        page = setup_playwright
        page.goto(URL)
        home_page = HomePage(page)
        home_page.men_button_click()

        expect(page).to_have_url("https://www.nike.com/il/men")

    def test_women_button_click(self,setup_playwright):
        page = setup_playwright
        page.goto(URL)
        home_page = HomePage(page)
        home_page.women_button_click()

        expect(page).to_have_url("https://www.nike.com/il/women")

    def test_sport_button_click(self, setup_playwright):
        page = setup_playwright
        page.goto(URL)
        home_page = HomePage(page)
        home_page.sport_button_click()

        expect(page).to_have_url("https://www.nike.com/il/lockerroom")


class Test_Help():

    def test_help_search(self,setup_playwright):
        page = setup_playwright
        page.goto(URL)
        home_page = HomePage(page)
        home_page.help_button()
        help_page = HelpPage(page)
        help_page.search_help("shoes")
        expect(page).to_have_url("https://www.nike.com/il/help/search/shoes")



