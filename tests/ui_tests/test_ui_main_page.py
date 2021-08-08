import pytest
from selenium import webdriver
from modules.pages.main_page import MainPage


@pytest.fixture()
def browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_verify_top_menu(browser):
    start_page = MainPage(browser)
    start_page.load()
    start_page.close_pop_up_windows()
    assert start_page.logo()
    menu_items = start_page.get_menu_items()
    text_menu_items = [item.text for item in menu_items]
    for menu_name in ["PLATFORM", "SOLUTIONS", "ABOUT US", "CONTACT US", "BLOG", "CASE STUDIES"]:
        assert menu_name in text_menu_items, "Not found menu {} on the start page".format(menu_name)


def test_verify_contact_on_pages(browser):
    current_page = MainPage(browser)
    current_page.load()
    current_page.close_pop_up_windows()
    assert current_page.logo(), "Not found logo on the start page"
    for page_name in ["PLATFORM", "SOLUTIONS", "ABOUT US", "CONTACT US", "BLOG", "CASE STUDIES"]:
        current_page = current_page.move_menu_item(page_name)
        assert current_page.logo(), "Not found logo on the {} page".format(page_name)

    contact_us_page = current_page.move_menu_item("CONTACT US")


