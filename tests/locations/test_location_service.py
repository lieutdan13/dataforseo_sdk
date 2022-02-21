from unittest import TestCase
from unittest.mock import MagicMock, patch

from dataforseo_sdk.locations.location_service import LocationService

STATUS_CODE_OK = 20000
LOCATION_CODE__AUSTRALIA = 2036
LOCATION_CODE__AUSTRIA = 2040
LOCATION_CODE__CANADA = 2124
LOCATION_CODE__UNITED_STATES = 2840

MOCK_VALID_RESPONSE_LOCATION_AND_LANGUAGES = {
    "version": "0.1.20220216",
    "status_code": STATUS_CODE_OK,
    "status_message": "Ok.",
    "time": "0.2478 sec.",
    "cost": 0,
    "tasks_count": 1,
    "tasks_error": 0,
    "tasks": [
        {
            "id": "02211752-3334-0196-0000-d7d2ec33f81d",
            "status_code": STATUS_CODE_OK,
            "status_message": "Ok.",
            "time": "0 sec.",
            "cost": 0,
            "result_count": 91,
            "path": [
                "v3",
                "dataforseo_labs",
                "locations_and_languages"
            ],
            "data": {
                "api": "dataforseo_labs",
                "function": "locations_and_languages"
            },
            "result": [
                {
                    "location_code": LOCATION_CODE__AUSTRALIA,
                    "location_name": "Australia",
                    "location_code_parent": None,
                    "country_iso_code": "AU",
                    "location_type": "Country",
                    "available_languages": [
                        {
                            "available_sources": [
                                "google",
                                "bing"
                            ],
                            "language_name": "English",
                            "language_code": "en",
                            "keywords": 196283373,
                            "serps": 14975687
                        }
                    ]
                },
                {
                    "location_code": LOCATION_CODE__AUSTRIA,
                    "location_name": "Austria",
                    "location_code_parent": None,
                    "country_iso_code": "AT",
                    "location_type": "Country",
                    "available_languages": [
                        {
                            "available_sources": [
                                "google",
                                "bing"
                            ],
                            "language_name": "German",
                            "language_code": "de",
                            "keywords": 43697801,
                            "serps": 2852838
                        }
                    ]
                },
                {
                    "location_code": LOCATION_CODE__CANADA,
                    "location_name": "Canada",
                    "location_code_parent": None,
                    "country_iso_code": "CA",
                    "location_type": "Country",
                    "available_languages": [
                        {
                            "available_sources": [
                                "google",
                                "bing"
                            ],
                            "language_name": "English",
                            "language_code": "en",
                            "keywords": 221233655,
                            "serps": 15535562
                        },
                        {
                            "available_sources": [
                                "google",
                                "bing"
                            ],
                            "language_name": "French",
                            "language_code": "fr",
                            "keywords": 115305083,
                            "serps": 8069200
                        }
                    ]
                },
                {
                    "location_code": LOCATION_CODE__UNITED_STATES,
                    "location_name": "United States",
                    "location_code_parent": None,
                    "country_iso_code": "US",
                    "location_type": "Country",
                    "available_languages": [
                        {
                            "available_sources": [
                                "google",
                                "bing"
                            ],
                            "language_name": "English",
                            "language_code": "en",
                            "keywords": 854895220,
                            "serps": 189902351
                        },
                        {
                            "available_sources": [
                                "google"
                            ],
                            "language_name": "Spanish",
                            "language_code": "es",
                            "keywords": 100715022,
                            "serps": 5640792
                        }
                    ]
                }
            ]
        }
    ]
}

class TestLocationService(TestCase):
    @patch("dataforseo_sdk.api_client.api_client.RestClient")
    def test_locations_and_languages(self, mock_rest_client_class):
        mock_rest_client = MagicMock()
        mock_rest_client.get.return_value = MOCK_VALID_RESPONSE_LOCATION_AND_LANGUAGES
        mock_rest_client_class.return_value = mock_rest_client

        location_service = LocationService()

        locations = location_service.locations_and_languages()

        assert locations[LOCATION_CODE__AUSTRALIA] == MOCK_VALID_RESPONSE_LOCATION_AND_LANGUAGES["tasks"][0]["result"][0]
        assert locations[LOCATION_CODE__AUSTRIA] == MOCK_VALID_RESPONSE_LOCATION_AND_LANGUAGES["tasks"][0]["result"][1]
        assert locations[LOCATION_CODE__CANADA] == MOCK_VALID_RESPONSE_LOCATION_AND_LANGUAGES["tasks"][0]["result"][2]
        assert locations[LOCATION_CODE__UNITED_STATES] == MOCK_VALID_RESPONSE_LOCATION_AND_LANGUAGES["tasks"][0]["result"][3]

    @patch("dataforseo_sdk.api_client.api_client.RestClient")
    def test_locales(self, mock_rest_client_class):
        mock_rest_client = MagicMock()
        mock_rest_client.get.return_value = MOCK_VALID_RESPONSE_LOCATION_AND_LANGUAGES
        mock_rest_client_class.return_value = mock_rest_client

        location_service = LocationService()

        locales = location_service.locales()

        assert locales == {
            "en_au": (LOCATION_CODE__AUSTRALIA, "en", "AU"),
            "de_at": (LOCATION_CODE__AUSTRIA, "de", "AT"),
            "en_ca": (LOCATION_CODE__CANADA, "en", "CA"),
            "fr_ca": (LOCATION_CODE__CANADA, "fr", "CA"),
            "en_us": (LOCATION_CODE__UNITED_STATES, "en", "US"),
            "es_us": (LOCATION_CODE__UNITED_STATES, "es", "US"),
        }