# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------

from pathlib import Path

from pydantic import ValidationError

import pytest
from datamodels import ArchiveData, ArchiveFile, ArchiveMetadata
from datamodels._internals import size_fmt

# -----------------------------------------------------------------------------
# Fixtures
# -----------------------------------------------------------------------------


@pytest.fixture
def metadata(temp_dir) -> ArchiveMetadata:
    return ArchiveMetadata(
        processed_directory=temp_dir, file_count=3, total_size=size_fmt(243)
    )


@pytest.fixture
def test_file(temp_dir) -> ArchiveFile:
    file_path: Path = temp_dir / "test_file.txt"
    file_path.write_text("Testing")
    return ArchiveFile(path=file_path)


# -----------------------------------------------------------------------------
# Tests
# -----------------------------------------------------------------------------


class TestInit:
    def test_required_fields(self, metadata, test_file, required_fields_regex):

        # Empty
        with pytest.raises(
            ValidationError, match=required_fields_regex(ArchiveData),
        ):
            ArchiveData()  # type: ignore

        # With fields
        archive_data = ArchiveData(
            metadata=metadata, files=[test_file, test_file]
        )
        assert archive_data.metadata == metadata
        assert archive_data.files == [test_file, test_file]


class TestMethods:
    def test_dump_model(self, metadata, test_file):
        # Dump to self.metadata.processed_directory
        archive_data = ArchiveData(
            metadata=metadata, files=[test_file, test_file]
        )
        out_file = archive_data.dump_model()
        assert out_file == metadata.processed_directory / "archive_data.json"
        parsed_data = ArchiveData.parse_file(out_file)
        assert archive_data == parsed_data
