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
    def test_required_fields(self, test_file):
        file = File(path=test_file)
        assert file.path == test_file
        assert file.name == test_file.name
        assert file.ext == test_file.suffix.lower()
        assert file.size == size_fmt(test_file.stat().st_size)
        assert file.checksum is None
        assert file.identification is None

    def test_optional_fields(self, test_file):
        file_identification = Identification(
            puid="fmt/test", signature="Test signature"
        )
        file = File(
            path=test_file, checksum="abc", identification=file_identification,
        )
        assert file.checksum == "abc"
        assert file.identification == file_identification

