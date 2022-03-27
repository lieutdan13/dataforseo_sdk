from dataforseo_sdk.api_client.api_client import APIClient
from dataforseo_sdk.api_client.api_credentials_factory import APICredentialsFactory
from dataforseo_sdk.config import Config


class APIClientMixin:
    def init_api_client(self, **kwargs):
        self._data_dir = kwargs.get("data_dir")
        self._credentials = kwargs.get("credentials")
        self._username = kwargs.get("username")
        self._password = kwargs.get("password")

    @property
    def credentials(self):
        if not getattr(self, "_credentials", None):
            if getattr(self, "_username", None) and getattr(self, "_password", None):
                self._credentials = (
                    APICredentialsFactory.credentials_from_username_and_password(
                        username=self._username, password=self._password
                    )
                )
            else:
                self._credentials = APICredentialsFactory.credentials_from_config()
        return self._credentials

    @property
    def client(self):
        if not getattr(self, "_client", None):
            self._client = APIClient(credentials=self.credentials)
        return self._client

    @property
    def data_dir(self):
        if not self._data_dir:
            self._data_dir = Config.config["data_dir"]
        return self._data_dir
