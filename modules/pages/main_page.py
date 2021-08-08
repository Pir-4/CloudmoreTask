from selenium.webdriver.common.by import By

from modules.pages.page import Page
from modules.tests_constants import UIConstants as UIC


class MainPage(Page):
    """"""
    LOGO_ID = "hs-link-module_14891423382401005"
    DECLINE_BUTTON = (By.ID, "hs-eu-decline-button")
    CLOSE_POPUP_BUTTON = (By.CLASS_NAME, "leadinModal-close")
    MENU_ITEM_XPATH = '//*[@id="hs_menu_wrapper_module_146731076570911"]/ul/li[{0}]/a'

    def __init__(self, driver):
        Page.__init__(self, driver, UIC.BASE_UI_URL)

    def close_pop_up_windows(self):
        self.button_click(self.DECLINE_BUTTON)
        self.button_click(self.CLOSE_POPUP_BUTTON)

    def get_menu_items(self):
        items = []
        for number in range(1, 7):
            xpath = self.MENU_ITEM_XPATH.format(number)
            items.append(self._get_item((By.XPATH, xpath)))
        return items

    def move_menu_item(self, name):
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
        return menu_pages[text.upper()](self._driver)


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
