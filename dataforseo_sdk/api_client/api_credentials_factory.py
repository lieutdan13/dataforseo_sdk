from typing import Optional

from dataforseo_sdk.config import Config
from .api_credentials import APICredentials


class APICredentialsFactory:
    """A factory to produce credentials from various different inputs"""

    @staticmethod
    def credentials_from_all_credentials(
        credentials: Optional[APICredentials] = None,
        username: Optional[str] = None,
        password: Optional[str] = None,
    ) -> APICredentials:
        """Returns an APICredentials object from an object, username/password
        combination, or defaults from the config object.

        Args:
            credentials (APICredentials, optional): An object with a username and password attribute. Defaults to None.
            username (str, optional): A valid Data for SEO API username. Defaults to None.
            password (str, optional): A valid Data for SEO API password. Defaults to None.

        Returns:
            APICredentials: An APICredentials object
        """
        if not credentials:
            if username and password:
                return APICredentialsFactory.credentials_from_username_and_password(
                    username, password
                )
            return APICredentialsFactory.credentials_from_config()
        return credentials

    @staticmethod
    def credentials_from_username_and_password(
        username: str, password: str
    ) -> APICredentials:
        """Returns an APICredentials object from a username and password

        Args:
            username (str): A valid Data for SEO API username
            password (str): A valid Data for SEO API password

        Returns:
            APICredentials: An APICredentials object
        """
        return APICredentials(username=username, password=password)

    @staticmethod
    def credentials_from_config() -> APICredentials:
        """Creates and returns an APICredentials object from the credentials
        from the Config object. The Config object, by default, gets the
        credentials from the DFS_API_USERNAME and DFS_API_PASSWORD environment
        variables.

        Returns:
            APICredentials:  An APICredentials object
        """
        username = Config.config["api_username"]
        password = Config.config["api_password"]
        return APICredentials(username=username, password=password)
