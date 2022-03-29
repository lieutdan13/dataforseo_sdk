import os

from dataforseo_sdk.config import Config
from .api_credentials import APICredentials


class APICredentialsFactory:
    @staticmethod
    def credentials_from_all_credentials(
        credentials=None, username=None, password=None
    ):
        if not credentials:
            if username and password:
                return APICredentialsFactory.credentials_from_username_and_password(
                    username, password
                )
            return APICredentialsFactory.credentials_from_config()
        return credentials

    @staticmethod
    def credentials_from_username_and_password(username, password):
        return APICredentials(username=username, password=password)

    @staticmethod
    def credentials_from_config():
        username = Config.config["api_username"]
        password = Config.config["api_password"]
        return APICredentials(username=username, password=password)
