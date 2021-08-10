from modules.rest_functions.base_rest import BaseRestApi
from modules.tests_constants import RestConstants as RC
import json


class UserRest:
    """ Provide Rest API for User rest object """

    @staticmethod
    def create(users):
        """ Create user or users

        :param users: list of users bodies
        :type users: list
        :returns: status code
        :type: int
        """
        base_rest = BaseRestApi()
        users = users if isinstance(users, list) else [users]
        result = base_rest.request("POST", RC.REST_OBJ_USER, RC.USER_CREATE_LIST, params=users)
        return result["status_code"]

    @staticmethod
    def get(user_name, expected_error=False):
        """ Get user entry

        :param user_name: user name
        :type user_name: str
        :param expected_error:
        :type expected_error: true if request is unsuccess
        :returns: status code and user body
        :rtype: tuple
        """
        base_rest = BaseRestApi()
        result = base_rest.request("GET", RC.REST_OBJ_USER, user_name)
        if expected_error:
            return result["status_code"], result
        return result["status_code"], json.loads(result["text"])

    @staticmethod
    def modify(user_name, body):
        """ Modify user entry via Put

        :param user_name: user name
        :type user_name: str
        :param body: new body for modifying
        :type body: dict
        :returns: status code
        :rtype: int
        """
        base_rest = BaseRestApi()
        result = base_rest.request("PUT", RC.REST_OBJ_USER, user_name, body)
        return result["status_code"]

    @staticmethod
    def delete(user_name):
        """ Delete user entry

        :param user_name: user name
        :type user_name: str
        :returns: status code
        :rtype: int
        """
        base_rest = BaseRestApi()
        result = base_rest.request("DEL", RC.REST_OBJ_USER, user_name)
        return result["status_code"]
