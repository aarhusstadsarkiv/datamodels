# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------

from pathlib import Path
from typing import Any, Dict, Optional

from pydantic import BaseModel, root_validator, validator

from datamodels._internals import size_fmt
from datamodels.identification import Identification

# -----------------------------------------------------------------------------
# Model
# -----------------------------------------------------------------------------


class ArchiveFile(BaseModel):
    """ArchiveFile data model."""

    path: Path
    checksum: Optional[str]
    identification: Optional[Identification]

    # Validators
    @root_validator
    def set_extra_info(cls, fields: Dict[Any, Any]) -> Dict[Any, Any]:
        """Set extra information derived from file path."""
        file_path: Optional[Path] = fields.get("path")
        if file_path:
            fields.update(
                {
                    "name_": file_path.name,
                    "ext_": file_path.suffix.lower(),
                    "size_": size_fmt(file_path.stat().st_size),
                }
            )
        return fields

    @validator("path")
    def path_must_be_file(cls, path: Path) -> Path:
        """Resolves the file path and validates that it points
        to an existing file."""
        if not path.resolve().is_file():
            raise ValueError("File does not exist")
        return path.resolve()

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

    def name(self) -> str:
        """Get the file name.

        Returns
        -------
        str
            File name.
        """
        return self.path.name

    def ext(self) -> str:
        """Get the file extension.

        Returns
        -------
        str
            File extension.
        """
        return self.path.suffix.lower()

    def size(self) -> str:
        """Get the file size in human readable string format.

        Returns
        -------
        str
            File size in human readable format.
        """
        return size_fmt(self.path.stat().st_size)
