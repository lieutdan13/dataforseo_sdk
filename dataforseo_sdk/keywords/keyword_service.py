from dataforseo_sdk.api_client.api_client import APIClient
from dataforseo_sdk.api_client.api_credentials_factory import APICredentialsFactory
from dataforseo_sdk.config import Config
from dataforseo_sdk.locations.location_service import LocationService


class KeywordService:
    API_ENDPOINT = "dataforseo_labs/ranked_keywords/live"

    def __init__(self):
        self.creds = APICredentialsFactory.credentials_from_environment()
        self.client = APIClient(credentials=self.creds)
        locale = LocationService().locales[Config().locale]
        self.location_code, self.language_code, _ = locale

    def ranked_keywords(self, target_domain):
        post_data = [
            {
                "target": target_domain,
                "location_code": self.location_code,
                "language_code": self.language_code,
            }
        ]

        keywords = self.client.post(self.API_ENDPOINT, post_data)
        return keywords
