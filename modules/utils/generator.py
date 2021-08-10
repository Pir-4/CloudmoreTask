import random
import sys
import string
from copy import copy, deepcopy

from modules.tests_constants import RestConstants as RC

positive_body = {"id": 0,
                 "username": "TestUser",
                 "firstName": "TestFirstName",
                 "lastName": "TestLastName",
                 "email": "email@email.com",
                 "password": "Password",
                 "phone": "78526",
                 "userStatus": 0
                 }


def get_bodies(number=5, excluded_params=None):
    """ Generate bodies for create cases

    :param number: number of bodies
    :type number: int
    :param excluded_params: parameter names witch excluded from generated body
    :type excluded_params: list
    :returns: valid bodies
    :rtype: list
    """
    bodies = [positive_body]
    for _ in range(number):
        bodies.append(create_body(excluded_params))
    return bodies


def get_bodies_modify(number=5, excluded_params=None):
    """ Generate bodies for modify cases

    :param number: number of bodies
    :type number: int
    :param excluded_params: parameter names witch excluded from generated body
    :type excluded_params: list
    :returns: valid bodies
    :rtype: list
    """
    bodies = []
    for _ in range(number):
        first_body = create_body(excluded_params)
        second_body = first_body
        while second_body == first_body:
            second_body = create_body(excluded_params)
            second_body["username"] = first_body["username"]
        bodies.append((first_body, second_body))
    return bodies


def get_negative_post_bodies():
    """ Generate non valid bodies for create cases

    :returns: non valid bodies
    :rtype: list
    """
    bodies = [create_body()]#body with id
    param_list = copy(RC.PARAM_LIST)
    param_list.remove("id")
    for param_name in param_list:
        bodies.append(create_body(excluded_params=["id", param_name]))
    for _ in range(5):
        bodies.append(create_body(excluded_params=["id"], is_bad_format=True))
    return bodies


def get_negative_put_bodies():
    """ Generate non valid bodies for modify cases

    :returns: non valid bodies
    :rtype: list
    """
    body = create_body(excluded_params=["id"])
    modify_body = deepcopy(body)
    modify_body.update({"id": random.randint(0, sys.maxsize)})
    bodies = [(body, modify_body)]

    param_list = copy(RC.PARAM_LIST)
    param_list.remove("id")
    for param_name in param_list:
        body = create_body(excluded_params=["id"])
        modify_body = create_body(excluded_params=["id", param_name])
        bodies.append((body, modify_body))
    for _ in range(5):
        body = create_body(excluded_params=["id"])
        modify_body = create_body(excluded_params=["id"], is_bad_format=True)
        bodies.append((body, modify_body))
    return bodies


def create_body(excluded_params=None, is_bad_format=False):
    """ Create body

    :param excluded_params: parameter names witch excluded from generated body
    :type excluded_params: list
    :param is_bad_format: generate body with non format parameters
    :type is_bad_format: bool
    :returns: body
    :rtype: dict
    """
    excluded_params = excluded_params or []
    excluded_params = excluded_params if isinstance(excluded_params, list) else [excluded_params]
    gen_funcs = {"int": lambda: random.randint(0, sys.maxsize),
                 "str": lambda: gen_string(),
                 "telNumber": lambda: gen_string(prefix="+", allowed=["digits"], size=11),
                 "name": lambda: gen_string(allowed=["letters"]),
                 "email": lambda: gen_string(allowed=["letters", "digits"], size=11, postfix="@mail.com")}
    body = {}
    for body_param in RC.PARAM_LIST:
        if body_param in excluded_params:
            continue
        param_format = RC.PARAM_TYPES[body_param]
        if is_bad_format:
            param_format = random.choice([item for item in RC.PARAM_TYPES.values() if item != param_format])
        body[body_param] = gen_funcs[param_format]()
    return body


def gen_string(prefix="", allowed=None, size=None, postfix=""):
    """ Generate string

    :param prefix: prefix of generated string
    :type prefix: str
    :param allowed: list of allowed symbols: letters, digits, punctuation
    :type allowed: list
    :param size: length of string
    :type size: int
    :param postfix: postfix of generated string
    :type postfix: str
    :returns:
    :rtype: str
    """
    symbols_dict = {"letters": string.ascii_letters, "digits": string.digits,
                    "punctuation": string.punctuation}
    allowed = allowed or ["letters", "digits", "punctuation"]
    symbols = []
    for allow_key in allowed:
        symbols += symbols_dict[allow_key]
    size = size or random.randint(1, 50)
    result = prefix + "".join(random.choice(symbols) for _ in range(size)) + postfix
    return result
