import pytest
from http import HTTPStatus
from modules.rest_functions.user_rest import UserRest
from modules.utils import generator


@pytest.mark.parametrize('input_body', generator.get_bodies(excluded_params=["id"]))
def test_positive_create(input_body):
    """"""
    assert UserRest.create(input_body) == HTTPStatus.OK, "The POST returned unexpected status code"
    status, user = UserRest.get(input_body["username"])
    assert status == HTTPStatus.OK, "The GET returned unexpected status code"
    user_id = user.pop("id")
    assert isinstance(user_id, int) and user_id, "User id isn't int or equal 0"
    assert not user.get("password") and user.get("password") == input_body["password"], "GET return user password"
    assert user == input_body, "The expected body doesn't equal actual"


@pytest.mark.parametrize('input_body', generator.get_bodies(excluded_params=["id"]))
def test_positive_delete(input_body):
    """"""
    assert UserRest.create(input_body) == HTTPStatus.OK, "The POST returned unexpected status code"
    status, _ = UserRest.get(input_body["username"])
    assert status == HTTPStatus.OK, "The GET returned unexpected status code"
    assert UserRest.delete(input_body["username"]), "Un success user deleting"
    status, _ = UserRest.get(input_body["username"], expectedError=True)
    assert status == HTTPStatus.NOT_FOUND, "The DELETE returned unexpected status code"


@pytest.mark.parametrize('input_body, modify_body', generator.get_bodies_modify(excluded_params=["id"]))
def test_positive_modify(input_body, modify_body):
    """"""
    assert UserRest.create(input_body) == HTTPStatus.OK, "The POST returned unexpected status code"
    _, input_user = UserRest.get(input_body["username"])
    assert UserRest.modify(input_body["username"], modify_body) == HTTPStatus.OK, \
           "The PUT returned unexpected status code"
    status, modify_user = UserRest.get(input_body["username"])
    assert status == HTTPStatus.OK, "The GET returned unexpected status code"
    modify_user_id = modify_user.pop("id")
    assert modify_user == modify_body, "User doesn't have modified body"
    assert modify_user_id == input_user["id"], "Users objects has different id values"
    assert modify_user != input_body, "User after a modification has the same body that it was created"

