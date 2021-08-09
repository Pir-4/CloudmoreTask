from selenium.webdriver.common.by import By


class Page:
    """"""
    def __init__(self, driver, url):
        """"""
        self._driver = driver
        self._url = url

    @property
    def driver(self):
        return self._driver

    def load(self):
        self._driver.maximize_window()
        self._driver.get(self._url)

    def _get_item(self, locator):
        """"""
        return self._driver.find_element(*locator)

    def _get_items(self, locator):
        """"""
        return self._driver.find_elements(*locator)

    def button_click(self, locator):
        self._get_item(locator).click()

    def logo(self):
        return self._get_item((By.ID, self.LOGO_ID))
