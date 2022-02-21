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