from dataforseo_sdk.api_client.api_client import APIClient
from dataforseo_sdk.api_client.api_credentials_factory import APICredentialsFactory
from dataforseo_sdk.config import Config


class DFSService:
    def __init__(self, *args, **kwargs) -> None:
        self._client = kwargs.get("client")
        self._data_dir = kwargs.get("data_dir")
        self._credentials = kwargs.get("credentials")
        self._username = kwargs.get("username")
        self._password = kwargs.get("password")

    @property
    def credentials(self):
        if not self._credentials:
            self._credentials = APICredentialsFactory.credentials_from_all_credentials(
                username=self._username, password=self._password
            )
        return self._credentials

    @property
    def client(self):
        if not self._client:
            self._client = APIClient(
                credentials=self.credentials, data_dir=self.data_dir
            )
        return self._client

    @property
    def data_dir(self):
        if not self._data_dir:
            self._data_dir = Config.config["data_dir"]
        return self._data_dir
