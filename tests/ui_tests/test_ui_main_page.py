import pytest
from selenium import webdriver
from modules.pages.main_page import MainPage
from modules.tests_constants import UIConstants as UIC
from modules.utils.file_utils import save_screenshot


@pytest.fixture()
def browser_chrome_pc():
    """ Init Chrome web driver for PC """
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.fixture()
def browser_chrome_mobile_nexus_5():
    """ Init Chrome web driver for Nexus 5 """
    options = webdriver.ChromeOptions()
    options.add_experimental_option(*UIC.CHROME_OPTIONS_NEXUS_5)
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.fixture()
def start_page_pc(browser_chrome_pc):
    """ Load start page for PC """
    page = MainPage(browser_chrome_pc)
    page.load()
    page.close_pop_up_windows()
    return page


@pytest.fixture()
def start_page_mobile_nexus_5(browser_chrome_mobile_nexus_5):
    """ Load start page for Nexus """
    page = MainPage(browser_chrome_mobile_nexus_5)
    page.load()
    page.close_pop_up_windows()
    return page


@pytest.fixture()
def start_page_param(request):
    """ Get start page by web driver type"""
    if request.param == "pc":
        return request.getfixturevalue("start_page_pc")
    elif request.param == "nexus5":
        return request.getfixturevalue("start_page_mobile_nexus_5")
    else:
        raise ValueError('Unknown type: {}'.format(request.param))


def test_verify_top_menu(start_page_pc):
    """Verify items of top menu"""
    assert start_page_pc.logo(), "Not found logo on the start page"
    menu_items = start_page_pc.get_menu_items()
    text_menu_items = [item.text for item in menu_items]
    for menu_name in UIC.MENU_PAGE_NAMES:
        assert menu_name in text_menu_items, "Not found menu {} on the start page".format(menu_name)


def test_verify_contact_on_pages(start_page_pc):
    """Verify redirect to other pages and contact bodies on 'contact us' page"""
    current_page = start_page_pc
    assert current_page.logo(), "Not found logo on the start page"
    for page_name in UIC.MENU_PAGE_NAMES:
        current_page = current_page.move_menu_item(page_name)
        assert current_page.logo(), "Not found logo on the {} page".format(page_name)

    contact_us_page = current_page.move_menu_item(UIC.MENU_CONTACT_US)
    assert contact_us_page.contact_body(), "Contact body doesn't exist on Contact us page"
    assert contact_us_page.contact_body_footer(), "Contact body doesn't exist on Contact us page footer"


@pytest.mark.parametrize('start_page_param', ["pc", "nexus5"], indirect=True)
@pytest.mark.parametrize('keyword', UIC.SEARCH_WORDS)
def test_verity_search(start_page_param, keyword):
    """ Verify search result pages"""
    search_page = start_page_param.search(keyword)
    for count, page in enumerate(search_page.pages()):
        if count == 2:
            break
    save_screenshot(page, keyword)
