from unittest import TestCase
from unittest.mock import MagicMock, patch

from dataforseo_sdk.dfs_service import DFSService
from dataforseo_sdk.api_client.api_credentials import APICredentials


class TestDFSService(TestCase):
    def test_instantiate__with_credentials(self):
        credentials = MagicMock(spec=APICredentials)

        dfs_service = DFSService(credentials=credentials)

        assert dfs_service.credentials == credentials

    def test_instantiate__with_username_and_password(self):
        username = "username"
        password = "password"

        dfs_service = DFSService(username=username, password=password)

        assert dfs_service.credentials.username == username
        assert dfs_service.credentials.password == password

    def test_instantiate__with_client(self):
        client = MagicMock()

        dfs_service = DFSService(client=client)

        assert dfs_service.client == client
