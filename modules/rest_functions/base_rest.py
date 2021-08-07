import requests
from modules import tests_constants as TC


class BaseRestApi:
    """"""
    _requestsCalls = {"GET": requests.get,
                      "POST": requests.post,
                      "PUT": requests.put,
                      "DEL": requests.delete}

    def __init__(self, baseUrl=TC.BASE_URL):
        """"""
        self._baseUrl = baseUrl
        self._header = {}

    def request(self, req_type, rest_obj, obj_id, params=None):
        """"""
        request_url = self._get_url(self._baseUrl, rest_obj, obj_id)
        params = params or {}

        response = self._requestsCalls[req_type.upper()](request_url, json=params, headers=self._header)
        result = {"status_code": response.status_code,
                  "reason": response.reason,
                  "text": response.text,
                  "success": response.ok}
        return result

    def update_header(self, header):
        """"""
        self._header.update(header)

    def _get_url(self, *args):
        """"""
        if self._baseUrl not in args:
            args.insert(0, self._baseUrl)
        return "/".join(args)
