from dataforseo_sdk.api_client.api_client import APIClient
from dataforseo_sdk.api_client.api_credentials_factory import APICredentialsFactory


class CompetitorService:
    API_ENDPOINT = "dataforseo_labs/competitors_domain/live"

    def __init__(self):
        self.creds = APICredentialsFactory.credentials_from_environment()
        self.client = APIClient(credentials=self.creds)

    def domain_competitors(self, target_domains):
        post_data = {
            i: {"target": domain, "location_code": 2840, "language_code": "en"}
            for i, domain in enumerate(target_domains)
        }
        competitors = self.client.post(self.API_ENDPOINT, post_data)
        return competitors
