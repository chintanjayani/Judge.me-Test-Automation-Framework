import pytest
import datetime
from pages.reviews_page import ReviewsPage

@pytest.mark.ui
def test_reviews_page_loads(page):
    reviews_page = ReviewsPage(page)
    reviews_page.navigate()

    assert "Discover trusted products based on verified reviews and ratings on Judge.me Reviews" in page.title()

@pytest.mark.ui
def test_reviews_page_search_section_title(page):
    reviews_page = ReviewsPage(page)
    reviews_page.navigate()
    page_content = page.text_content("body")

    assert "Discover trusted products" in page_content

@pytest.mark.ui
def test_product_search_box_is_visible(page):
    reviews_page = ReviewsPage(page)
    reviews_page.navigate()
    search_box = page.locator("//input[@placeholder='Search products']")

    assert search_box.is_visible(), "Search box is not visible on the page."

@pytest.mark.ui
def test_product_categories_on_reviews_page(page):
    reviews_page = ReviewsPage(page)
    reviews_page.navigate()

    categories_xpath = "//a[@class='meganav__header-link']"
    reviews_page.wait_for_selector(categories_xpath)
    elements = page.locator(categories_xpath)

    expected_texts = [
    "Apparel & Accessories",
    "Animals & Pet Supplies",
    "Health & Beauty",
    "Home & Garden",
    "Electronics",
    "Furniture"
    ]

    count = elements.count()

    assert count == len(expected_texts), f"Expected {len(expected_texts)} elements, but found {count}"

    for i in range(count):
        element_text = elements.nth(i).inner_text()
        assert element_text == expected_texts[i], f"Element {i + 1} text '{element_text}' does not match expected text '{expected_texts[i]}'"

@pytest.mark.ui
def test_view_all_button_on_reviews_page(page):
    reviews_page = ReviewsPage(page)
    reviews_page.navigate()

    view_all_button = page.locator("//a[@class='btn pf-secondary-button cs__see-all']")
    view_all_button.click()

    assert "Discover trusted products by category | Reviews on Judge.me" in page.title()

@pytest.mark.ui
def test_categories_page_heading_title(page):
    reviews_page = ReviewsPage(page)
    reviews_page.navigate()

    view_all_button = page.locator("//a[@class='btn pf-secondary-button cs__see-all']")
    view_all_button.click()
    page_content = page.text_content("body")

    assert "Browse all categories" in page_content

@pytest.mark.ui
def test_product_search_on_reviews_page(page):
    reviews_page = ReviewsPage(page)
    reviews_page.navigate()

    reviews_page.search_for_reviews("iphone")
    reviews_page.wait_for_selector(".search-results__result-heading")
    heading_element = page.locator(".search-results__result-heading")
    heading_text = heading_element.inner_text()

    expected_text = "results found"

    assert expected_text in heading_text, f"Heading text '{heading_text}' does not contain expected text '{expected_text}'"

@pytest.mark.ui
def test_review_page_copyright_year(page):
    reviews_page = ReviewsPage(page)
    reviews_page.navigate()

    footer_element = page.locator("//p[contains(text(), 'All Rights Reserved')]")

    today = datetime.date.today()
    year = today.year

    expected_text = "© {} | All Rights Reserved | Judge.me Company Limited".format(year)

    assert expected_text in footer_element.inner_text(), f"Footer text '{footer_element.inner_text()}' does not contain expected text '{expected_text}'"

@pytest.mark.ui
def test_currency_change_for_product_search(page):
    reviews_page = ReviewsPage(page)
    reviews_page.navigate()

    header_element = page.locator("(//div[@class='main-header__menu-button'])[1]")

    currency = "BSD"
    header_element.click()
    page.select_option("select.currency-dropdown__select", label=currency)

    reviews_page.search_for_reviews("iphone")

    price_element = page.locator("(//p[@class='product-search-card__price'])[1]")
    price_text = price_element.text_content()

    assert currency in price_text, f"Currency text '{price_text}' does not contain expected text '{currency}'"

@pytest.mark.ui
def test_search_functionality_when_no_product_found(page):
    reviews_page = ReviewsPage(page)
    reviews_page.navigate()

    reviews_page.search_for_reviews("iphlkehfasldkfhs;kfjhsjfhslkdjfkaone")
    reviews_page.wait_for_selector(".search-results__result-heading")
    heading_element = page.locator(".search-results__result-heading")
    heading_text = heading_element.inner_text()

    expected_text = "0 results found for \"iphlkehfasldkfhs;kfjhsjfhslkdjfkaone\""

    assert expected_text in heading_text, f"Heading text '{heading_text}' does not contain expected text '{expected_text}'"

@pytest.mark.ui
def test_sort_reviews(page):
    reviews_page = ReviewsPage(page)
    reviews_page.navigate()

    reviews_page.search_for_reviews("iphone")
    reviews_page.sort_reviews("newest")

    selected_option = page.locator("select.sort-dropdown option:checked").first
    selected_option_text = selected_option.text_content()
    assert "Newest" in selected_option_text, f"Expected 'Newest', but got '{selected_option_text}'"

@pytest.mark.ui
def test_sort_reviews_all_options(page):
    reviews_page = ReviewsPage(page)
    reviews_page.navigate()

    reviews_page.search_for_reviews("iphone")

    select_options = page.locator("(//select[@class='sort-dropdown'])[2]")
    select_options_text = select_options.text_content()

    expected_options = [
        "Default",
        "Most reviews first",
        "Newest",
        "Best Selling",
        "Low price first",
        "High price first"
        ]

    for option in expected_options:
        assert option in select_options_text, f"Expected {option}, but got '{select_options_text}'"

