# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------

from pathlib import Path
from typing import Any, Dict, Optional

from pydantic import BaseModel, root_validator, validator

from datamodels._internals import size_fmt, warn_overwrite
from datamodels.identification import Identification

# -----------------------------------------------------------------------------
# Model
# -----------------------------------------------------------------------------


class ArchiveFile(BaseModel):
    """ArchiveFile data model."""

    path: Path
    name: str = ""
    ext: str = ""
    size: str = ""
    checksum: Optional[str]
    identification: Optional[Identification]

    # Validators
    @root_validator
        return fields

    @validator("path")
    def path_must_be_file(cls, path: Path) -> Path:
        """Resolves the file path and validates that it points
        to an existing file."""
        if not path.resolve().is_file():
            raise ValueError("File does not exist")
        return path.resolve()

    # Init
    def __init__(self, **data: Any):
        super().__init__(**data)
        self.name = self.path.name
        self.ext = self.path.suffix.lower()
        self.size = size_fmt(self.path.stat().st_size)

    # Methods
    def read_text(self) -> str:
        """Expose read_text() functionality from pathlib.
        Encoding is set to UTF-8.

        Returns
        -------
        str
            File text data.
        """
        return self.path.read_text(encoding="utf-8")

    def read_bytes(self) -> bytes:
        """Expose read_bytes() functionality from pathlib.

        Returns
        -------
        bytes
            File byte data.
        """
        return self.path.read_bytes()
