from .rest_client import RestClient


class APIClient:
    def __init__(self, credentials, api_version="v3"):
        self.credentials = credentials
        self.api_version = api_version

        self._client = None

    @property
    def client(self):
        if not self._client:
            self._client = RestClient(
                self.credentials.username, self.credentials.password
            )
        return self._client

    c = client

    def get(self, endpoint):
        return self.client.get(f"{self.api_version}/{endpoint}")