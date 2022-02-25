import os
from unittest import TestCase
from unittest.mock import MagicMock, patch

from dataforseo_sdk.keywords.keyword_service import KeywordService

RANKED_KEYWORDS_RESPONSE_FILE = os.path.realpath(os.path.join(os.path.realpath(__file__), "..", "data", "api.dataforseo.com.v3-dataforseo_labs-ranked_keywords-live.20220225T163613.078371.json"))

class TestKeywordService(TestCase):

    def read_test_data_file(self, file_name):
        with open(file_name, "r", encoding="utf-8") as fh:
            return fh.read()

    @patch("dataforseo_sdk.keywords.keyword_service.APIClient")
    def test_ranked_keywords(self, mock_rest_client_class):
        ranked_keywords_test_data = self.read_test_data_file(RANKED_KEYWORDS_RESPONSE_FILE)
        mock_rest_client = MagicMock()
        mock_rest_client.post.return_value = ranked_keywords_test_data
        mock_rest_client_class.return_value = mock_rest_client

        target_domain = "afishingaddiction.com"
        keyword_service = KeywordService()

        ranked_keywords = keyword_service.ranked_keywords(target_domain=target_domain)

        assert ranked_keywords == ranked_keywords_test_data