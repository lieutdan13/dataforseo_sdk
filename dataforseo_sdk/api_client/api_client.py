import os

from .rest_client import RestClient

DEFAULT_DATA_DIR = os.path.realpath(
    os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "_data")
)


class APIClient:
    def __init__(self, credentials, api_version="v3", data_dir=None):
        self.credentials = credentials
        self.api_version = api_version
        self.data_dir = data_dir or DEFAULT_DATA_DIR

        self._client = None

    @property
    def client(self):
        if not self._client:
            self._client = RestClient(
                self.credentials.username,
                self.credentials.password,
                requests_log_dir=self.data_dir,
            )
        return self._client

    c = client

    def get(self, endpoint):
        return self.client.get(f"/{self.api_version}/{endpoint}")

    def post(self, endpoint, data):
        return self.client.post(f"/{self.api_version}/{endpoint}", data)
