"""
Fixtures for test data
"""

import json
import os
from pathlib import Path


class Fixture:
    """
    Fixture class for test data
    """

    def __init__(self):
        self.fixtures_directory = Path(__file__).parent
        self._json_files = [
            f.name
            for f in self.fixtures_directory.iterdir()
            if f.is_file() and f.suffix == ".json"
        ]

    def get_fixture_names(self):
        """Returns a list of fixture names without the .json extension"""
        return [os.path.splitext(f)[0] for f in self._json_files]

    def load_fixture(self, name):
        """Load and return the data from the specified JSON fixture"""
        filename = f"{name}.json"
        filepath = os.path.join(self.fixtures_directory, filename)

        if not os.path.exists(filepath):
            raise FileNotFoundError(
                f"Fixture `{filename}` not found in {self.fixtures_directory}"
            )
        else:
            with open(filepath, "r", encoding="utf-8") as f:
                return json.load(f)

    def load_all_fixtures(self):
        """Load and return a dict of all fixtures"""
        fixtures = {
        }
        for name in self.get_fixture_names():
            fixtures[name] = self.load_fixture(name)
        return fixtures
