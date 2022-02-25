from dataforseo_sdk.api_client.api_client import APIClient
from dataforseo_sdk.api_client.api_credentials_factory import APICredentialsFactory


class LocationService:
    API_ENDPOINT = "dataforseo_labs/locations_and_languages"

    def __init__(self):
        self.creds = APICredentialsFactory.credentials_from_environment()
        self.client = APIClient(credentials=self.creds)
        self._locations_and_languages = None
        self._locales = None

    @property
    def locations_and_languages(self):
        if self._locations_and_languages is None:
            results = self.client.get(self.API_ENDPOINT)
            self._locations_and_languages = {}
            for location in results["tasks"][0]["result"]:
                self._locations_and_languages[location["location_code"]] = location
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
