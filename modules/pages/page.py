from selenium.webdriver.common.by import By


class Page:
    """"""
    #LOGO_ID = None
    #LOGO_SEARCH =

    def __init__(self, driver, url):
        """"""
        self._driver = driver
        self._url = url

    def load(self):
        self._driver.maximize_window()
        self._driver.get(self._url)

    def _get_item(self, locator):
        """"""
        return self._driver.find_element(*locator)

    def button_click(self, locator):
        self._get_item(locator).click()

    def logo(self):
        return self._get_item((By.ID, self.LOGO_ID))
