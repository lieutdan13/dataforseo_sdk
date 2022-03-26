from dataforseo_sdk.api_client.api_client_mixin import APIClientMixin
from dataforseo_sdk.locations.location_mixin import LocationMixin


class CompetitorService(APIClientMixin, LocationMixin):
    API_ENDPOINT = "dataforseo_labs/competitors_domain/live"

    def domain_competitors(self, target_domain):
        post_data = [
            {
                "target": target_domain,
                "location_code": self.location_code,
                "language_code": self.language_code,
            }
        ]

        competitors = self.client.post(self.API_ENDPOINT, post_data)
        return competitors
