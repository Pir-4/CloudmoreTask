from selenium.webdriver.common.by import By

from modules.pages.page import Page
from modules import tests_constants as TC


class MainPage(Page):
    """"""
    DECLINE_BUTTON = (By.ID, "hs-eu-decline-button")
    CLOSE_POPUP_BUTTON = (By.CLASS_NAME, "leadinModal-close")
    MENU_ITEM_XPATH = '//*[@id="hs_menu_wrapper_module_146731076570911"]/ul/li[{0}]/a'

    def __init__(self, driver):
        Page.__init__(self, driver, TC.BASE_UI_URL)

    def close_pop_up_windows(self):
        self.button_click(self.DECLINE_BUTTON)
        self.button_click(self.CLOSE_POPUP_BUTTON)

    def get_menu_items(self):
        items = []
        for number in range(1, 7):
            xpath = self.MENU_ITEM_XPATH.format(number)
            items.append(self._get_item((By.XPATH, xpath)))
        return items
