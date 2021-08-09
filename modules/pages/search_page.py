from selenium.webdriver.common.by import By
from modules.pages.main_page import MainPage
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException


class SearchPage(MainPage):
    NEXT_PAGE_BUTTON = (By.CLASS_NAME, 'hs-search-results__next-page')
    SCROLL_STEP = 50

    def pages(self, wait_count=5000):
        page = self
        new_height = self.driver.execute_script("return document.body.scrollHeight") / 2
        for _ in range(wait_count):
            try:
                if page:
                    yield page
                next_button = self._get_item(self.NEXT_PAGE_BUTTON)
                next_button.click()
                page = SearchPage(self.driver)
            except NoSuchElementException:
                break
            except ElementClickInterceptedException:
                new_height += self.SCROLL_STEP
                script = "window.scrollTo(0, {0});".format(new_height)
                self.driver.execute_script(script)
                page = None
        return page
