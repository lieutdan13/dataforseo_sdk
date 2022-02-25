from http.client import HTTPResponse
import os
import sys
from unittest import TestCase
from unittest.mock import MagicMock, Mock, patch

from dataforseo_sdk.api_client.rest_client import RestClient


class TestRestClient(TestCase):
    def setUp(self) -> None:
        self.data_dir = os.path.join(
            os.path.dirname(os.path.realpath(__file__)), "data"
        )
        self.response_file = None
        return super().setUp()

    def tearDown(self) -> None:
        # if self.response_file is not None and os.path.isfile(self.response_file):
        #     os.remove(self.response_file)
        return super().tearDown()

    def setup_mocking(self, mock_https_connection_class, response_json):
        self.mock_http_response = Mock(spec=HTTPResponse)
        self.mock_http_response.read.return_value = response_json
        self.mock_https_connection = MagicMock()
        self.mock_https_connection.getresponse.return_value = self.mock_http_response
        mock_https_connection_class.return_value = self.mock_https_connection

    @patch("dataforseo_sdk.api_client.rest_client.HTTPSConnection")
    def test_request(self, mock_https_connection_class):
        response_json = b'{"test": "message"}'
        expected_response = {"test": "message"}
        self.setup_mocking(mock_https_connection_class, response_json)
        endpoint = "/v3/my_endpoint"

        rest_client = RestClient("username", "password")
        response = rest_client.request(endpoint, "GET")

        assert response == expected_response

    @patch("dataforseo_sdk.api_client.rest_client.datetime")
    @patch("dataforseo_sdk.api_client.rest_client.HTTPSConnection")
    def test_request__creates_file(self, mock_https_connection_class, mock_datetime):
        response_json = b'{"test": "message"}'
        date_str = "20220225T084125.123456"
        expected_domain_name = "api.example.com"
        self.setup_mocking(mock_https_connection_class, response_json)
        mock_now = MagicMock()
        mock_now.strftime.return_value = date_str
        mock_datetime.datetime.now.return_value = mock_now
        endpoint = "/v3/my_endpoint"
        slug_endpoint = "v3-my_endpoint"
        self.response_file = os.path.join(
            self.data_dir, f"{expected_domain_name}.{slug_endpoint}.{date_str}.json"
        )

        rest_client = RestClient("username", "password", requests_log_dir=self.data_dir)
        rest_client.domain = expected_domain_name
        rest_client.request(endpoint, "GET")

        assert os.path.isfile(self.response_file)
        with open(self.response_file, "r") as f:
            assert f.read() == response_json.decode()
