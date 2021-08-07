import pytest
from http import HTTPStatus
from modules.rest_functions.user_rest import UserRest
from modules.utils import generator

#TODO create teardown


@pytest.mark.parametrize('input_body', generator.get_negative_post_bodies())
def test_negative_create(input_body):
    """"""
    assert UserRest.create(input_body) == HTTPStatus.BAD_REQUEST, \
        "The POST returned unexpected status code with body {}".format(input_body)


def test_negative_get():
    """"""
    non_exist_user = generator.create_body()
    status, _ = UserRest.get(non_exist_user["username"])
    assert status == HTTPStatus.NOT_FOUND, "Was get ono exist user"


def test_negative_delete():
    """"""
    status = HTTPStatus.OK
    non_exist_user = {}
    while status != HTTPStatus.NOT_FOUND:
        non_exist_user = generator.create_body()
        status, _ = UserRest.get(non_exist_user["username"])
    assert UserRest.delete(non_exist_user["username"]), "Delete non exist user"


def test_negative_modify_non_exist_user():
    """"""
    status = HTTPStatus.OK
    non_exist_user = {}
    while status != HTTPStatus.NOT_FOUND:
        non_exist_user = generator.create_body(excluded_params=["id"])
        status, _ = UserRest.get(non_exist_user["username"])
    assert UserRest.modify(non_exist_user["username"], non_exist_user), "Modify non exist user"


@pytest.mark.parametrize('input_body, modify_body', generator.get_negative_put_bodies())
def test_negative_modify(input_body, modify_body):
    """"""
    assert UserRest.create(input_body) == HTTPStatus.OK, "The POST returned unexpected status code"
    _, input_user = UserRest.get(input_body["username"])
    assert UserRest.modify(input_body["username"], modify_body) == HTTPStatus.BAD_REQUEST, \
           "The PUT returned unexpected status code with body {}".format(modify_body)
