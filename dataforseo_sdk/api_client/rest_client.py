import datetime
import os
from pathlib import Path
import re

from base64 import b64encode
from http.client import HTTPSConnection
from json import dumps, loads
from typing import Any, Optional

from slugify import slugify

from dataforseo_sdk.config import Config

ALLOWED_SLUG_CHARS = re.compile(r"[^-_a-zA-Z0-9]+")


class RestClient:
    """This Client was taken from the Data for SEO Python Simple Rest Client.
    https://cdn.dataforseo.com/v3/examples/python/python_Client.zip?2022221"""

    def __init__(
        self, username: str, password: str, requests_log_dir: Optional[Path] = None
    ) -> None:
        """RestClient constructor

        Args:
            username (str): A valid Data for SEO API username
            password (str): A valid Data for SEO API password
            requests_log_dir (Path, optional): the directory to which all responses as json files are written. Defaults to None.
        """
        self.username = username
        self.password = password
        self.requests_log_dir = requests_log_dir
        self._domain = None

    @property
    def domain(self) -> str:
        """The domain name to use for Data for SEO API calls. Defaults to retrieve from the Config object which gets
        the value from the DFS_API_DOMAIN environment variable.

        Returns:
            str: the DFS API domain name
        """
        if not self._domain:
            self._domain = Config.config["api_domain"]
        return self._domain

    @domain.setter
    def domain(self, value: str) -> None:
        self._domain = value

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

    def request(self, path: str, method: str, data: Any = None) -> Any:
        """Make an API request, save the response as a file, and return the response object.

        Args:
            path (str): The path part of the API URL
            method (str): The HTTP method. e.g. GET, POST
            data (Any, optional): The payload to send with a POST request. Defaults to None.

        Returns:
            Any: A Python object representing the HTTP response
        """
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

    def get(self, path: str) -> Any:
        """Perform a GET request against the Data for SEO API

        Args:
            path (str): The path part of the API URL

        Returns:
            Any: A Python object representing the HTTP response
        """
        return self.request(path, "GET")

    def post(self, path: str, data: Any) -> Any:
        """Perform a POST request against the Data for SEO API

        Args:
            path (str): The path part of the API URL
            data (Any, optional): The payload to send with a POST request. Defaults to None.

        Returns:
            Any: A Python object representing the HTTP response
        """
        if isinstance(data, str):
            data_str = data
        else:
            data_str = dumps(data)
        return self.request(path, "POST", data_str)
