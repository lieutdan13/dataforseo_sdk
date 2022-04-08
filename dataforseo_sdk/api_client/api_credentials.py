class APICredentials:
    """A class to create an object that represents the Data for SEO API credentials"""

    def __init__(self, username: str, password: str) -> None:
        """APICredentials object constructor

        Args:
            username (str): A valid Data for SEO API username
            password (str): A valid Data for SEO API password
        """
        self.username = username
        self.password = password
