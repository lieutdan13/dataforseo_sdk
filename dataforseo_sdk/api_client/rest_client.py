import datetime
import os
import re

from base64 import b64encode
from http.client import HTTPSConnection
from json import dumps, loads

from slugify import slugify

ALLOWED_SLUG_CHARS = re.compile(r"[^-_a-zA-Z0-9]+")


class RestClient:
    """This Client was taken from the Data for SEO Python Simple Rest Client.
    https://cdn.dataforseo.com/v3/examples/python/python_Client.zip?2022221"""

    domain = "api.dataforseo.com"

    def __init__(self, username, password, requests_log_dir=None):
        self.username = username
        self.password = password
        self.requests_log_dir = requests_log_dir

    def _generate_file_path_for_request(self, endpoint):
        now = datetime.datetime.now()
        date_str = now.strftime("%Y%m%dT%H%M%S.%f")
        file_name = f"{self.domain}.{slugify(endpoint, regex_pattern=ALLOWED_SLUG_CHARS)}.{date_str}.json"
        return os.path.join(self.requests_log_dir, file_name)

    def _maybe_create_response_file(self, endpoint, response_json):
        if self.requests_log_dir:
            file_path = self._generate_file_path_for_request(endpoint=endpoint)
            with open(file_path, "w+", encoding="utf-8") as fh:
                fh.write(response_json)

    def request(self, path, method, data=None):
        connection = HTTPSConnection(self.domain)
        try:
            base64_bytes = b64encode(
                ("%s:%s" % (self.username, self.password)).encode("ascii")
            ).decode("ascii")
            headers = {
                "Authorization": "Basic %s" % base64_bytes,
                "Content-Encoding": "gzip",
            }
            connection.request(method, path, headers=headers, body=data)
            response = connection.getresponse()
            response_json = response.read().decode()
            self._maybe_create_response_file(path, response_json)
            response_object = loads(response_json)
            return response_object
        finally:
            connection.close()

    def get(self, path):
        return self.request(path, "GET")

    def post(self, path, data):
        if isinstance(data, str):
            data_str = data
        else:
            data_str = dumps(data)
        return self.request(path, "POST", data_str)
