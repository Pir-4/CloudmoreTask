from selenium.webdriver.common.by import By
from modules.pages.main_page import MainPage


class ContactUsPage(MainPage):
    """Provide methods and properties of contact us page"""

    LOGO_ID = 'hs-link-module_146731076570910'
    CONTACT_BODY_XPATH = '//*[@id="hsForm_f9e04aef-80b3-457c-9073-d0d77cb7da75_2328"]'
    CONTACT_BODY_FOOTER_XPATH = '//*[@id="hsForm_432229bb-e668-47cc-856e-84fc921ce284_7339"]'

    def contact_body(self):
        """ Get contact body on middle of page

        :returns: contact body
        :rtype: selenium.webelement
        """
        return self.get_element((By.XPATH, self.CONTACT_BODY_XPATH))

    def contact_body_footer(self):
        """ Get contact body on footer of page

        :returns: contact body
        :rtype: selenium.webelement
        """
        return self.get_element((By.XPATH, self.CONTACT_BODY_FOOTER_XPATH))
