from dataforseo_sdk.dfs_service import DFSService
from dataforseo_sdk.locations.location_mixin import LocationMixin


class KeywordService(DFSService, LocationMixin):
    API_ENDPOINT = "dataforseo_labs/ranked_keywords/live"

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
