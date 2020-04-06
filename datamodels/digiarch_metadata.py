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


class DigiarchMetadata(BaseModel):
    """Digiarch metadata data model."""

    last_run: Optional[datetime]
    processed_directory: Path
    file_count: int
    total_size: str
