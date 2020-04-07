# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------

from datetime import datetime
from pathlib import Path

from pydantic import ValidationError

import pytest
from datamodels import ArchiveMetadata
from datamodels._internals import size_fmt
from freezegun import freeze_time

# -----------------------------------------------------------------------------
# Tests
# -----------------------------------------------------------------------------


class TestInit:
    last_run = datetime.now()
    file_count = 0
    size = size_fmt(0)
    empty_subdirectories = [Path("empty/sub"), Path("one/more")]
    several_files = [Path("more/than/one/file"), Path("same/problem")]
    identification_warnings = 500
    duplicates = 32

    def test_required_fields(self, temp_dir):
        metadata = ArchiveMetadata(
            processed_directory=temp_dir,
            file_count=self.file_count,
            total_size=self.size,
        )
        assert metadata.last_run is not None
        assert metadata.processed_directory == temp_dir
        assert metadata.file_count == self.file_count
        assert metadata.total_size == self.size
        assert metadata.empty_subdirectories is None
        assert metadata.several_files is None
        assert metadata.identification_warnings is None
        assert metadata.duplicates is None

    def test_optional_fields(self, temp_dir):
        metadata = ArchiveMetadata(
            last_run=self.last_run,
            processed_directory=temp_dir,
            file_count=self.file_count,
            total_size=self.size,
            empty_subdirectories=self.empty_subdirectories,
            several_files=self.several_files,
            identification_warnings=self.identification_warnings,
            duplicates=self.duplicates,
        )
        assert metadata.last_run == self.last_run
        assert metadata.empty_subdirectories == self.empty_subdirectories
        assert metadata.several_files == self.several_files
        assert metadata.identification_warnings == self.identification_warnings
        assert metadata.duplicates == self.duplicates


class TestValidators:
    file_count = 0
    size = size_fmt(0)

    # Time is frozen, so datetime.now() will
    # return datetime(2020, 3, 23)
    @freeze_time("2020-03-23")
    def test_set_last_run(self, temp_dir):
        # Test with no last_run parameter
        metadata = ArchiveMetadata(
            processed_directory=temp_dir,
            file_count=self.file_count,
            total_size=self.size,
        )
        assert metadata.last_run == datetime(2020, 3, 23)

        # With last run set
        metadata = ArchiveMetadata(
            last_run="2010-02-16 00:00",
            processed_directory=temp_dir,
            file_count=self.file_count,
            total_size=self.size,
        )
        assert metadata.last_run == datetime(2010, 2, 16)

    def test_path_must_be_dir(self):
        with pytest.raises(ValidationError):
            ArchiveMetadata(
                processed_directory="not/a/dir",
                file_count=self.file_count,
                total_size=self.size,
            )
