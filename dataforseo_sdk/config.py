import os
from typing import Any

from ultra_config import GlobalConfig as Config

ENV_VAR_PREFIX = "DFS"


class DefaultConfig:
    data_dir = os.path.realpath(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), "_data")
    )
    locale = "en_us"
    api_domain = "api.dataforseo.com"


REQUIRED_CONFIGS = []


Config.load(
    default_settings=DefaultConfig,
    env_var_prefix=ENV_VAR_PREFIX,
    required=REQUIRED_CONFIGS,
)
