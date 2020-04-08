# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------

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

    def dump_model(self, to_file: Optional[Path] = None) -> Path:
        """Dump an ArchiveData model in JSON format to a file.
        The output JSON file is formatted with indent=4 and
        ensure_ascii=False.

        Parameters
        ----------
        to_file : Optional[Path]
            File to dump data to. If None, defaults to
            data_dir / archive_data.json
        Returns
        -------
        Path
            Path to the output file
        """
        to_file = (
            to_file or self.metadata.processed_directory / "archive_data.json"
        )
        to_file.write_text(self.json(indent=4, ensure_ascii=False))
        return to_file
