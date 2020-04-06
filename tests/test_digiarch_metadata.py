# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------

from datetime import datetime
from pathlib import Path
from unittest.mock import patch

from pydantic import ValidationError
import pytest

from datamodels import DigiarchMetadata
from datamodels._internals import size_fmt

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
        metadata = DigiarchMetadata(
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
        metadata = DigiarchMetadata(
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

    def test_set_last_run(self, temp_dir):
        _time = datetime.now()
        with patch("datetime.datetime.now", return_value=_time):
            metadata = DigiarchMetadata(
                processed_directory=temp_dir,
                file_count=self.file_count,
                total_size=self.size,
            )
        assert metadata.last_run == _time

    def test_path_must_be_dir(self):
        # TODO: Mock with FreezeGun
        # https://github.com/spulec/freezegun
        with pytest.raises(ValidationError):
            DigiarchMetadata(
                processed_directory="not/a/dir",
                file_count=self.file_count,
                total_size=self.size,
            )
