# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------
from pathlib import Path
from typing import Any, Dict, Optional

from pydantic import BaseModel, root_validator, validator

from datamodels import Identification
from datamodels._internals import warn_overwrite, size_fmt

# -----------------------------------------------------------------------------
# Model
# -----------------------------------------------------------------------------


class File(BaseModel):
    """File datamodel."""

    path: Path
    name: str = ""
    ext: str = ""
    size: str = ""
    checksum: Optional[str]
    identification: Optional[Identification]

    @root_validator
    def overwrite(cls, values: Dict[Any, Any]) -> Dict[Any, Any]:
        """Warns about fields that will be overwritten during init."""
        for field, value in values.items():
            if field in {"name", "ext", "size"} and value:
                warn_overwrite(
                    f"{field}={value} will be overwritten during init."
                )
                values[field] = ""
        return values

    @validator("path")
    def path_must_be_file(cls, path: Path) -> Path:
        if not path.is_file():
            raise ValueError("File does not exist.")
        return path

    def __init__(self, **data: Any):
        super().__init__(**data)

        self.path = self.path.resolve()
        self.name = self.path.name
        self.ext = self.path.suffix.lower()
        self.size = size_fmt(self.path.stat().st_size)
