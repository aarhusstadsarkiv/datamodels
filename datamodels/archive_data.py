# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------

import json
from pathlib import Path
from typing import List, Optional

from pydantic import BaseModel

from datamodels.archive_file import ArchiveFile
from datamodels.archive_metadata import ArchiveMetadata

# -----------------------------------------------------------------------------
# Model
# -----------------------------------------------------------------------------


class ArchiveData(BaseModel):
    """Archive data model"""

    metadata: ArchiveMetadata
    files: List[ArchiveFile]

    def work_dir(self) -> Path:
        """Create and/or obtain the work directory.

        Returns
        -------
        Path
            Work directory path.
        """
        work_dir: Path = self.metadata.processed_directory / "_out"

        if not work_dir.is_dir():
            work_dir.mkdir()

        return work_dir

    def data_dir(self) -> Path:
        """Create and/or obtain the data directory.

        Returns
        -------
        Path
            Data directory path.
        """
        data_dir: Path = self.work_dir() / ".data"

        if not data_dir.is_dir():
            data_dir.mkdir()

        return data_dir

    def dump(self, to_file: Optional[Path] = None) -> None:
        """Dump an ArchiveData model in JSON format to a file.

        Parameters
        ----------
        to_file : Optional[Path]
            File to dump data to. If None, defaults to
            data_dir / archive_data.json
        """
        to_file = to_file or self.data_dir() / "archive_data.json"
        json.dump(self.json(), to_file.open())
