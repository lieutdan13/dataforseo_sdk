from dataforseo_sdk.api_client.api_client import APIClient
from dataforseo_sdk.api_client.api_credentials_factory import APICredentialsFactory
from dataforseo_sdk.config import Config


class APIClientMixin:
    def __init__(self, *args, **kwargs):
        self._set_data_dir(kwargs.get("data_dir"))
        self._set_credentials(
            credentials=kwargs.get("credentials"),
            username=kwargs.get("username"),
            password=kwargs.get("password"),
        )
        self.client = APIClient(credentials=self.credentials)

    def _set_credentials(self, credentials=None, username=None, password=None):
        if credentials:
            self.credentials = credentials
        elif username and password:
            self.credentials = (
                APICredentialsFactory.credentials_from_username_and_password(
                    username=username, password=password
                )
            )
        else:
            self.credentials = APICredentialsFactory.credentials_from_config()

    def _set_data_dir(self, data_dir=None):
        self.data_dir = data_dir or Config.config["data_dir"]
