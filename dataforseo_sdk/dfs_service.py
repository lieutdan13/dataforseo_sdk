from .api_client.api_client_mixin import APIClientMixin


class DFSService(APIClientMixin):
    def __init__(self, *args, **kwargs) -> None:
        self.init_api_client(*args, **kwargs)
