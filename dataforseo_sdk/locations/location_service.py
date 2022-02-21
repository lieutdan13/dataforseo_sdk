from dataforseo_sdk.api_client.api_client import APIClient
from dataforseo_sdk.api_client.api_credentials_factory import APICredentialsFactory


class LocationService:
    API_ENDPOINT = "dataforseo_labs/locations_and_languages"

    def __init__(self):
        self.creds = APICredentialsFactory.credentials_from_environment()
        self.client = APIClient(credentials=self.creds)


    def locations_and_languages(self):
        results = self.client.get(self.API_ENDPOINT)
        locations = {}
        for location in results["tasks"][0]["result"]:
            locations[location["location_code"]] = location
        return locations

    def locales(self):
        locations = self.locations_and_languages()

        locales = {}
        for location_code, location in locations.items():
            for language in location["available_languages"]:
                locale = f"{language['language_code']}_{location['country_iso_code']}".lower()
                locales[locale] = (
                    location_code,
                    language['language_code'],
                    location['country_iso_code'],
                )
        return locales