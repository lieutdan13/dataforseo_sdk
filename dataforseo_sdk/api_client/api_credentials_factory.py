import os

from dataforseo_sdk.config import Config
from .api_credentials import APICredentials


class APICredentialsFactory:
    @staticmethod
    def credentials_from_username_and_password(username, password):
        return APICredentials(username=username, password=password)

    @staticmethod
    def credentials_from_config():
        username = Config.config["api_username"]
        password = Config.config["api_password"]
        return APICredentials(username=username, password=password)
