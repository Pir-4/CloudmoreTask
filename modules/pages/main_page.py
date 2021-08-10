from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from modules.pages.page import Page
from modules.tests_constants import UIConstants as UIC


class MainPage(Page):
    """Provide methods and properties of main page"""

    LOGO_ID = "hs-link-module_14891423382401005"
    DECLINE_BUTTON = (By.ID, "hs-eu-decline-button")
    CLOSE_POPUP_BUTTON = (By.CLASS_NAME, "leadinModal-close")
    MENU_ITEM_XPATH = '//*[@id="hs_menu_wrapper_module_146731076570911"]/ul/li[{0}]/a'
    SEARCH_BUTTON = (By.XPATH, '//*[@id="hs_cos_wrapper_module_15306484973591482"]')
    SEARCH_INPUT = (By.XPATH, '//*[@id="hs_cos_wrapper_module_1530555777115370"]/div/form/input')

    def __init__(self, driver):
        """ Init class

        :param driver: wev driver
        :type driver: selenium.webdriver
        """
        Page.__init__(self, driver, UIC.BASE_UI_URL)

    def close_pop_up_windows(self):
        """ Close pop-up windows which raise
            when main page load the first time

        :returns: None
        """
        self.button_click(self.DECLINE_BUTTON)
        self.button_click(self.CLOSE_POPUP_BUTTON)

    def get_menu_items(self):
        """ Get top of menu items

        :returns: list of webelements
        :rtype: list
        """
        items = []
        for number in range(1, 7):
            xpath = self.MENU_ITEM_XPATH.format(number)
            items.append(self.get_element((By.XPATH, xpath)))
        return items

    def move_menu_item(self, name):
        """ Find and click to menu item and move their page

        :param name: menu item name
        :type name: str
        :returns: new page
        :rtype: MainPage
        """
        from modules.pages.contact_us_page import ContactUsPage
        menu_pages = {UIC.MENU_PLATFORM: PlatformPage,
                      UIC.MENU_SOLUTIONS: SolutionsPage,
                      UIC.MENU_ABOUT_US: AboutUsPage,
                      UIC.MENU_CONTACT_US: ContactUsPage,
                      UIC.MENU_BLOG: BlogPage,
                      UIC.MENU_CASE_STUDIES: CaseStudiesPage}

        menu_item = [item for item in self.get_menu_items() if item.text == name]
        text = menu_item[0].text
        menu_item[0].click()
        return menu_pages[text.upper()](self.driver)

    def search(self, keyword):
        """ Find and click to menu item and move their page

        :param keyword: search keyword
        :type keyword: str
        :returns: page of search result
        :rtype: SearchPage
        """
        from modules.pages.search_page import SearchPage
        self.button_click(self.SEARCH_BUTTON)
        search_item = self.get_element(self.SEARCH_INPUT)
        search_item.send_keys(keyword, Keys.RETURN)
        return SearchPage(self.driver)


class PlatformPage(MainPage):
    LOGO_ID = 'hs-link-module_146731076570910'


class SolutionsPage(MainPage):
    LOGO_ID = 'hs-link-module_14891423382401005'


class AboutUsPage(MainPage):
    LOGO_ID = 'hs-link-module_14891423382401005'


class BlogPage(MainPage):
    LOGO_ID = 'hs-link-module_146731076570910'


class CaseStudiesPage(MainPage):
    LOGO_ID = 'hs-link-module_146731076570910'
