from selenium.webdriver.common.by import By

class MainPage:
    """"""
    SEARCH_INPUT = (By.NAME, 'q')

    def __init__(self, driver, url):
        """"""
        self._driver = driver
        self._url = url

    def load(self):
        self._driver.get(self._url)

    def get_top_elements(self):
        """"""
        t = self.search("Platform")
        return t

    def search(self, phrase):
        search_input = self._driver.find_element(*self.SEARCH_INPUT)
        return search_input