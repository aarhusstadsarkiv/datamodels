# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------

from datetime import datetime
from pathlib import Path
from typing import List, Optional

from pydantic import BaseModel, validator

# -----------------------------------------------------------------------------
# Model
# -----------------------------------------------------------------------------


class ArchiveMetadata(BaseModel):
    """Metadata data model."""

    last_run: datetime = datetime.min
    processed_directory: Path
    file_count: int
    total_size: str
    empty_subdirectories: Optional[List[Path]]
    several_files: Optional[List[Path]]
    identification_warnings: Optional[int]
    duplicates: Optional[int]

    @validator("last_run", pre=True, always=True)
    def set_last_run(cls, last_run: datetime) -> datetime:
        if last_run == datetime.min:
            last_run = datetime.now()
        return last_run

    @validator("processed_directory")
    def path_must_be_dir(cls, processed_directory: Path) -> Path:
        if not processed_directory.resolve().is_dir():
            raise ValueError("Directory does not exist")
        return processed_directory.resolve()
