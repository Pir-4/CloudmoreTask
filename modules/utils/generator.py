import random
import sys
import string

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
        second_body = create_body(excluded_params)
        second_body["username"] = first_body["username"]
        while second_body == first_body:
            second_body = create_body(excluded_params)
            second_body["username"] = first_body["first_body"]
        bodies.append((first_body, second_body))
    return bodies


def create_body(excluded_params=None):
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
        body[body_param] = gen_funcs[TC.PARAM_TYPES[body_param]]()
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
