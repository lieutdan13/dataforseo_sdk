import json
import os
import re

from dataforseo_sdk.config import Config
from dataforseo_sdk.api_client.api_client import APIClient
from dataforseo_sdk.api_client.api_credentials_factory import APICredentialsFactory


class LocationService:
    API_ENDPOINT = "dataforseo_labs/locations_and_languages"
    FILE_PATTERN = (
        r"api\.dataforseo\.com\.v3-dataforseo_labs-locations_and_languages.*\.json"
    )

    def __init__(self, data_dir=None):
        self.data_dir = data_dir or Config().data_dir
        self.creds = APICredentialsFactory.credentials_from_environment()
        self.client = APIClient(credentials=self.creds, data_dir=self.data_dir)
        self._locations_and_languages = None
        self._locales = None

    def _maybe_load_from_file(self):
        for _, _, files in os.walk(self.data_dir):
            for file in files:
                if re.match(self.FILE_PATTERN, file):
                    file_path = os.path.join(self.data_dir, file)
                    with open(file_path, "r") as fh:
                        contents = fh.read()
                        response = json.loads(contents)
                        self._load_from_response(response=response)
                        if self._locations_and_languages:
                            return

    def _load_from_response(self, response):
        if response["tasks"]:
            self._locations_and_languages = {}
            for location in response["tasks"][0]["result"]:
                self._locations_and_languages[location["location_code"]] = location

    @property
    def locations_and_languages(self):
        if self._locations_and_languages is None:
            self._maybe_load_from_file()
        if self._locations_and_languages is None:
            results = self.client.get(self.API_ENDPOINT)
            self._load_from_response(results)
        return self._locations_and_languages

    @property
    def locales(self):
        if self._locales is None:
            self._locales = {}
            for location_code, location in self.locations_and_languages.items():
                for language in location["available_languages"]:
                    locale = f"{language['language_code']}_{location['country_iso_code']}".lower()
                    self._locales[locale] = (
                        location_code,
                        language["language_code"],
                        location["country_iso_code"],
                    )
        return self._locales
