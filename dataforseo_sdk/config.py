import os


class Config:
    def __init__(self):
        self.data_dir = os.environ.get("DFS_DATA_DIR") or os.path.realpath(
            os.path.join(os.path.dirname(os.path.realpath(__file__)), "_data")
        )
