import random
import sys
import string
from copy import copy, deepcopy

from modules import tests_constants as TC


def get_bodies(number=5, excluded_params=None):
    """"""
    bodies = []
    for _ in range(number):
        bodies.append(create_body(excluded_params))
    return bodies


def get_bodies_modify(number=5, excluded_params=None):
    """"""
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
    """"""
    bodies = [create_body()]#body with id
    param_list = copy(TC.PARAM_LIST)
    param_list.remove("id")
    for param_name in param_list:
        bodies.append(create_body(excluded_params=["id", param_name]))
    for _ in range(5):
        bodies.append(create_body(excluded_params=["id"], is_bad_format=True))
    return bodies


def get_negative_put_bodies():
    """"""
    body = create_body(excluded_params=["id"])
    modify_body = deepcopy(body)
    modify_body.update({"id": random.randint(0, sys.maxsize)})
    bodies = [(body, modify_body)]

    param_list = copy(TC.PARAM_LIST)
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
    """"""
    excluded_params = excluded_params or []
    excluded_params = excluded_params if isinstance(excluded_params, list) else [excluded_params]
    gen_funcs = {"int": lambda: random.randint(0, sys.maxsize),
                 "str": lambda: gen_string(),
                 "telNumber": lambda: gen_string(prefix="+", allowed=["digits"], size=11),
                 "name": lambda: gen_string(allowed=["letters"]),
                 "email": lambda: gen_string(allowed=["letters", "digits"], size=11, postfix="@mail.com")}
    body = {}
    for body_param in TC.PARAM_LIST:
        if body_param in excluded_params:
            continue
        param_format = TC.PARAM_TYPES[body_param]
        if is_bad_format:
            param_format = random.choice([item for item in TC.PARAM_TYPES.values() if item != param_format])
        body[body_param] = gen_funcs[param_format]()
    return body


def gen_string(prefix="", allowed=None, size=None, postfix=""):
    """"""
    symbols_dict = {"letters": string.ascii_letters, "digits": string.digits,
                    "punctuation": string.punctuation}
    allowed = allowed or ["letters", "digits", "punctuation"]
    symbols = []
    for allow_key in allowed:
        symbols += symbols_dict[allow_key]
    size = size or random.randint(1, 50)
    result = prefix + "".join(random.choice(symbols) for _ in range(size)) + postfix
    return result
