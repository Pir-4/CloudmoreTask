import pytest
from http import HTTPStatus
from modules.rest_functions.user_rest import UserRest


def test_positive_create():
    """"""
    user_body = {"username": "Testuser", "firstName": "firstName",
                 "lastName": "lastName", "email": "tmp@email.com", "password": "Password123!",
                 "phone": "156456", "userStatus": 0
                 }
    assert UserRest.create(user_body) == HTTPStatus.OK, "The POST returned unexpected status code"
    status, user = UserRest.get(user_body["username"])
    assert status == HTTPStatus.OK, "The GET returned unexpected status code"
    user_id = user.pop("id")
    assert isinstance(user_id, int) and user_id, "User id isn't int or equal 0"
    assert user == user_body, "The expected body doesn't equal actual"


def test_positive_delete():
    """"""
    user_body = {"username": "Testuser", "firstName": "firstName",
                 "lastName": "lastName", "email": "tmp@email.com", "password": "Password123!",
                 "phone": "156456", "userStatus": 0
                 }
    assert UserRest.create(user_body) == HTTPStatus.OK, "The POST returned unexpected status code"
    status, _ = UserRest.get(user_body["username"])
    assert status == HTTPStatus.OK, "The GET returned unexpected status code"
    assert UserRest.delete(user_body["username"]), "Un success user deleting"
    status, _ = UserRest.get(user_body["username"], expectedError=True)
    assert status == HTTPStatus.NOT_FOUND, "The DELETE returned unexpected status code"


def test_positive_modify():
    """"""
    user_body_1 = {"username": "Testuser", "firstName": "firstName",
                 "lastName": "lastName", "email": "tmp@email.com", "password": "Password123!",
                 "phone": "156456", "userStatus": 0
                 }

    user_body_2 = {"username": "Testuser", "firstName": "firstName2",
                   "lastName": "lastName", "email": "tmp@email.com", "password": "Password123!",
                   "phone": "156456", "userStatus": 0
                   }
    assert UserRest.create(user_body_1) == HTTPStatus.OK, "The POST returned unexpected status code"
    _, user_1 = UserRest.get(user_body_1["username"])
    assert UserRest.modify(user_body_1["username"], user_body_2) == HTTPStatus.OK, \
           "The PUT returned unexpected status code"
    status, user_2 = UserRest.get(user_body_1["username"])
    assert status == HTTPStatus.OK, "The GET returned unexpected status code"
    user_id = user_2.pop("id")
    assert user_id == user_1["id"], "Users objects has different id values"
    assert user_2 != user_body_1, "User after a modification has the same body that it was created"

