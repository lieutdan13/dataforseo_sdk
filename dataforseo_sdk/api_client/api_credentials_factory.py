import os

from .api_credentials import APICredentials


class APICredentialsFactory:
    @staticmethod
    def credentials_from_environment():
        username = os.environ["DFS_API_USERNAME"]
        password = os.environ["DFS_API_PASSWORD"]
        return APICredentials(username=username, password=password)

    @staticmethod
    def credentials_from_username_and_password(username, password):
        return APICredentials(username=username, password=password)
