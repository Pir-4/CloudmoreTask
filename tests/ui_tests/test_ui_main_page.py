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
    assert "PLATFORM" in text_menu_items
    assert "SOLUTIONS" in text_menu_items
    assert "ABOUT US" in text_menu_items
    assert "CONTACT US" in text_menu_items
    assert "BLOG" in text_menu_items
    assert "CASE STUDIES" in text_menu_items


