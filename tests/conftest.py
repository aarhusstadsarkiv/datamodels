"""Shared testing fixtures.

"""

# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------
from pathlib import Path

import pytest

# -----------------------------------------------------------------------------
# Fixtures
# -----------------------------------------------------------------------------


@pytest.fixture
def temp_dir(tmpdir_factory):
    temp_dir: str = tmpdir_factory.mktemp("temp_dir")
    return Path(temp_dir)


@pytest.fixture
def required_fields_regex():
    def _regex(datamodel):
        required_fields = [
            field
            for field, field_data in datamodel.__fields__.items()
            if field_data.required
        ]
        return (
            r"(?s)"
            + r"(\s)+field required.*".join(required_fields)
            + r"(\s)+field required"
        )

    return _regex
