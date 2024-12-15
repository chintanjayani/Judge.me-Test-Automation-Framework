from .base_page import BasePage

class ReviewsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.search_input = self.page.locator("input#search-input")
        self.search_button = self.page.locator("//label[@class='material-icons input_glass_icon']")
        self.search_suggestion = ".dropdown-content.dropdown-content--expand div"
        self.review_sort_dropdown = page.locator("(//select[@class='sort-dropdown'])[2]")

    def navigate(self):
        super().navigate("/reviews")

    def search_for_reviews(self, query):
        self.search_input.type(query)
        self.search_input.press("Enter")
#           other way of search without using Enter press
#         self.search_button.click()
#         search_suggestion = self.page.locator(self.search_suggestion, has_text=query).first
#         search_suggestion.click()

    def sort_reviews(self, sort_option):
        self.review_sort_dropdown.select_option(value=sort_option)

