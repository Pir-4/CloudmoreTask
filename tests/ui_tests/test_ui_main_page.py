import pytest
from selenium import webdriver
from modules.pages.main_page import MainPage
from modules.tests_constants import UIConstants as UIC


@pytest.fixture()
def browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.fixture()
def start_page(browser):
    page = MainPage(browser)
    page.load()
    page.close_pop_up_windows()
    return page


# def test_verify_top_menu(start_page):
#     assert start_page.logo(), "Not found logo on the start page"
#     menu_items = start_page.get_menu_items()
#     text_menu_items = [item.text for item in menu_items]
#     for menu_name in UIC.MENU_PAGE_NAMES:
#         assert menu_name in text_menu_items, "Not found menu {} on the start page".format(menu_name)
#
#
# def test_verify_contact_on_pages(start_page):
#     current_page = start_page
#     assert current_page.logo(), "Not found logo on the start page"
#     for page_name in UIC.MENU_PAGE_NAMES:
#         current_page = current_page.move_menu_item(page_name)
#         assert current_page.logo(), "Not found logo on the {} page".format(page_name)
#
#     contact_us_page = current_page.move_menu_item(UIC.MENU_CONTACT_US)
#     assert contact_us_page.contact_body(), "Contact body doesn't exist on Contact us page"
#     assert contact_us_page.contact_body_footer(), "Contact body doesn't exist on Contact us page footer"


def test_verity_search(start_page, keyword="Högset"):
    search_page = start_page.search(keyword)
    search_page.pages()