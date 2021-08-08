from selenium.webdriver.common.by import By


class Page:
    """"""
    LOGO_SEARCH = (By.ID, "hs-link-module_14891423382401005")

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
        return self._get_item(self.LOGO_SEARCH)