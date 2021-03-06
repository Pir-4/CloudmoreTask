import requests
from modules.tests_constants import RestConstants as RC


class BaseRestApi:
    """ Provide base Rest methods """

    _requestsCalls = {"GET": requests.get,
                      "POST": requests.post,
                      "PUT": requests.put,
                      "DEL": requests.delete}

    def __init__(self, base_url=RC.BASE_REST_URL):
        """ Init class

        :param base_url: url of an information system
        :type base_url: str
        :returns: None
        """
        self._baseUrl = base_url
        self._header = {}

    def request(self, req_type, rest_obj, obj_id, params=None):
        """ Send request

        :param req_type: request type: Get, Post, Delete, Put
        :type req_type: str
        :param rest_obj: name or rest object
        :type rest_obj: str
        :param obj_id: id of rest object or command
        :type obj_id: str
        :param params: request body
        :type params: dict
        :returns: main parts of response: status_code, reason, text, success
        :rtype: dict
        """
        request_url = self._get_url(self._baseUrl, rest_obj, obj_id)
        params = params or {}

        response = self._requestsCalls[req_type.upper()](request_url, json=params, headers=self._header)
        result = {"status_code": response.status_code,
                  "reason": response.reason,
                  "text": response.text,
                  "success": response.ok}
        return result

    def update_header(self, header):
        """ Update headers

        :param header: additional header parameters
        :type header: dict
        :returns: None
        """
        self._header.update(header)

    def _get_url(self, *args):
        """ Get full request url

        :param args: parts of url for joining
        :type: list
        :returns: full request url
        :rtype: str
        """
        if self._baseUrl not in args:
            args.insert(0, self._baseUrl)
        return "/".join(args)
