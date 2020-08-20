# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------

from pathlib import Path

from pydantic import ValidationError

import pytest
from acamodels import ArchiveFile, Identification
from acamodels._internals import size_fmt

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
    def test_required_fields(self, test_file, required_fields_regex):
        # Empty
        with pytest.raises(
            ValidationError, match=required_fields_regex(ArchiveFile),
        ):
            ArchiveFile()  # type: ignore

        # With required fields
        file = ArchiveFile(path=test_file)
        assert file.path == test_file
        assert file.checksum is None
        assert file.identification is None

    def test_optional_fields(self, test_file):
        file_identification = Identification(
            puid="fmt/test", signature="Test signature"
        )
        file = ArchiveFile(
            path=test_file, checksum="abc", identification=file_identification,
        )
        assert file.checksum == "abc"
        assert file.identification == file_identification


class TestValidators:
    def test_path_validation(self):
        with pytest.raises(ValidationError, match="File does not exist"):
            ArchiveFile(path="not a file")


class TestMethods:
    text = "This is a test file."

    @pytest.fixture
    def archive_file(self, test_file):
        return ArchiveFile(path=test_file)

    def test_read_text(self, archive_file):
        assert archive_file.read_text() == self.text

    def test_read_bytes(self, archive_file):
        assert archive_file.read_bytes() == self.text.encode()

    def test_name(self, archive_file):
        assert archive_file.name() == archive_file.path.name

    def test_ext(self, archive_file):
        assert archive_file.ext() == archive_file.path.suffix.lower()

    def test_size(self, archive_file):
        assert archive_file.size() == size_fmt(
            archive_file.path.stat().st_size
        )
