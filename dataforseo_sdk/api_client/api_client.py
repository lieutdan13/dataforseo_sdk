from dataforseo_sdk.config import Config
from .rest_client import RestClient


class APIClient:
    def __init__(self, credentials, api_version="v3", data_dir=None):
        self.credentials = credentials
        self.api_version = api_version
        self.data_dir = data_dir or Config().data_dir

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
