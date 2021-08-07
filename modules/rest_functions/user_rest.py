from modules.rest_functions.base_rest import BaseRestApi
from modules import tests_constants as TC


class UserRest:
    """"""

    @staticmethod
    def create(users):
        """"""
        base_rest = BaseRestApi()
        base_rest.update_header({"W-Token": "Ilovemyboss"})
        users = users if isinstance(users, list) else [users]
        result = base_rest.request("POST", TC.REST_OBJ_USER, TC.USER_CREATELIST, params=users)
        return result["status_code"]

    @staticmethod
    def get(user_name):
        """"""
        base_rest = BaseRestApi()
        result = base_rest.request("GET", TC.REST_OBJ_USER, user_name)
        return result["status_code"], result["text"]

    @staticmethod
    def modify( user_name, body):
        """"""
        base_rest = BaseRestApi()
        result = base_rest.request("PUT", TC.REST_OBJ_USER, user_name, body)
        return result["status_code"]

    @staticmethod
    def delete(user_name):
        """"""
        base_rest = BaseRestApi()
        result = base_rest.request("DEL", TC.REST_OBJ_USER, user_name)
        return result["status_code"]
