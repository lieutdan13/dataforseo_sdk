"""Console script for dataforseo_sdk."""
import argparse
import sys


class CLI:
    def main():
        """Console script for dataforseo_sdk."""
        parser = argparse.ArgumentParser()
        parser.add_argument("_", nargs="*")
        args = parser.parse_args()

        print("Arguments: " + str(args._))
        print(
            "Replace this message by putting your code into " "dataforseo_sdk.cli.main"
        )
        return 0


if __name__ == "__main__":
    sys.exit(CLI().main())  # pragma: no cover
