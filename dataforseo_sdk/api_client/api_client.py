from pathlib import Path
from typing import Optional, Union

from dataforseo_sdk.config import Config
from .rest_client import RestClient


class APIClient:
    """APIClient is a wrapper for the original RestClient
    class provided by Data for SEO.
    """

    def __init__(
        self,
        credentials: object,
        api_version: str = "v3",
        data_dir: Optional[Path] = Config.config["data_dir"],
    ) -> None:
        """Constructor for APIClient

        Args:
            credentials (object): a credentials object with username/password attributes
            api_version (str, optional): the version of the Data for SEO API. Options are "v2" or "v3". Defaults to "v3".
            data_dir (_type_, optional): the directory to which all responses as json files are written to and read from. Defaults to Config.config["data_dir"].
        """
        self.credentials = credentials
        self.api_version = api_version
        self.data_dir = data_dir

        self._client = None

    @property
    def client(self) -> RestClient:
        """A property for the http client.

        Returns:
            RestClient: The class that makes the http requests to the API.
        """
        if not self._client:
            self._client = RestClient(
                self.credentials.username,
                self.credentials.password,
                requests_log_dir=self.data_dir,
            )
        return self._client

    c = client

    def get(self, endpoint: str) -> dict:
        """The method that makes GET HTTP requests.

        Args:
            endpoint (str): The URL without the api version to make the HTTP request against

        Returns:
            dict: A dictionary representing the json response
        """
        return self.client.get(f"/{self.api_version}/{endpoint}")

    def post(self, endpoint: str, data: Union[list, dict, str]) -> dict:
        """The method that makes POST HTTP requests.

        Args:
            endpoint (str): The URL without the api version to make the HTTP request against
            data (Union[list, dict, str]): The object to pass as post data in the request

        Returns:
            dict: A dictionary representing the json response
        """
        return self.client.post(f"/{self.api_version}/{endpoint}", data)
