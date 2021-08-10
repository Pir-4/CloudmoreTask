from selenium.webdriver.common.by import By


class Page:
    """Provide base methods and properties of page"""

    def __init__(self, driver, url):
        """ Init class

        :param driver: wev driver
        :type driver: selenium.webdriver
        :param url: url of page
        :type url: str
        """
        self._driver = driver
        self._url = url

    @property
    def driver(self):
        """ Driver getter

        :returns: web driver
        :rtype: selenium.webdriver
        """
        return self._driver

    def load(self):
        """ Load page by url

        :returns: None
        """
        self.driver.maximize_window()
        self.driver.get(self._url)

    def get_element(self, locator):
        """ Get element

        :param locator: search condition
        :type locator: tuple(selenium.webdriver.common.by, str)
        :returns: web element
        :rtype: selenium.webelement
        """
        return self.driver.find_element(*locator)

    def button_click(self, locator):
        """ Find button and click it

        :param locator: search condition
        :type locator: tuple(selenium.webdriver.common.by, str)
        :returns: None
        """
        self.get_element(locator).click()

    def logo(self):
        """ Get logo

        :returns: web element
        :rtype: selenium.webelement
        """
        return self.get_element((By.ID, self.LOGO_ID))
