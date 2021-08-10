class RestConstants:
    """ Constants for Rest API tests """

    BASE_REST_URL = "https://petstore.swagger.io/v2"
    REST_OBJ_USER = "user"
    USER_CREATE_LIST = "createWithList"
    PARAM_TYPES = {"id": "int", "username": "name", "firstName": "name",
                   "lastName": "name", "email": "email", "password": "name",
                   "phone": "telNumber", "userStatus": "str"}
    PARAM_LIST = ["id", "username", "firstName", "lastName", "email", "password",
                  "phone", "userStatus"]


class UIConstants:
    """ Constants for UI tests """

    BASE_UI_URL = "https://web.cloudmore.com/"
    MENU_PLATFORM = "PLATFORM"
    MENU_SOLUTIONS = "SOLUTIONS"
    MENU_ABOUT_US = "ABOUT US"
    MENU_CONTACT_US = "CONTACT US"
    MENU_BLOG = "BLOG"
    MENU_CASE_STUDIES = "CASE STUDIES"
    MENU_PAGE_NAMES = [MENU_PLATFORM, MENU_SOLUTIONS, MENU_ABOUT_US, MENU_CONTACT_US, MENU_BLOG, MENU_CASE_STUDIES]

    SCREENSHOT_FOLDER = "logs/screenshots"
    SEARCH_WORDS = ["Högset", "o"]

    CHROME_OPTIONS_NEXUS_5 = ("mobileEmulation", {"deviceName": "Nexus 5"})
