from selenium.webdriver.common.by import By
from modules.pages.main_page import MainPage
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException


class SearchPage(MainPage):
    NEXT_PAGE_BUTTON = (By.CLASS_NAME, 'hs-search-results__next-page')

    def pages(self):
        page = self
        while True:
            try:
                if page:
                    yield page
                next_button = self._get_item(self.NEXT_PAGE_BUTTON)
                next_button.click()
                page = SearchPage(self.driver)
            except NoSuchElementException:
                break
            except ElementClickInterceptedException:
                new_height = self.driver.execute_script("return document.body.scrollHeight")/2
                script = "window.scrollTo(0, {0});".format(new_height+5)
                self.driver.execute_script(script)
                page = None
        return page
