from selenium.webdriver.common.by import By
from modules.pages.main_page import MainPage
from selenium.webdriver.common.action_chains import ActionChains

class SearchPage(MainPage):
    # NEXT_PAGE_BUTTON = (By.XPATH, '//*[@id="hs_cos_wrapper_module_1530612174918208"]')
    NEXT_PAGE_BUTTON = (By.CLASS_NAME, 'hs-search-results__next-page')
    # NEXT_PAGE_BUTTON = (By.CLASS_NAME, 'hs-search-results__pagination')
    NEXT_PAGE_BUTTON_2 = (By.CLASS_NAME, 'hs-search-results__listing')

    def scroll_down(self):
        count = 0
        while True:
            element = self._get_item(self.NEXT_PAGE_BUTTON_2)
            js = "arguments[{0}].scrollIntoView();".format(count)
            self._driver.execute_script(js, element)
            count +=1

    def pages(self):
        # self.scroll_down()
        while True:
            #t = self._driver.isDisplayes(*self.NEXT_PAGE_BUTTON)
            next_button = self._get_item(self.NEXT_PAGE_BUTTON_2)
            actions = ActionChains(self._driver)
            actions.move_to_element(next_button).perform()
            self._driver.execute_script("arguments[0].scrollIntoView();", next_button)

