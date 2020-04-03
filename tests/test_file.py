# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------

from pathlib import Path

from pydantic import ValidationError

import pytest
from datamodels import File, Identification
from datamodels._internals import OverwriteWarning, size_fmt

# -----------------------------------------------------------------------------
# Fixtures
# -----------------------------------------------------------------------------


@pytest.fixture
def test_file(temp_dir):
    test_file: Path = temp_dir / "test.txt"
    test_file.write_text("This is a test file.")
    return test_file


# -----------------------------------------------------------------------------
# Tests
# -----------------------------------------------------------------------------


class TestInit:
    def test_required_fields(self):
        pass

    def test_optional_fields(self):
        pass

    def test_validators(self):
        pass
