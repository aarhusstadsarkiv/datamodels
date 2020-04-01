# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------

from typing import Optional
from pydantic import BaseModel

# -----------------------------------------------------------------------------
# Model
# -----------------------------------------------------------------------------


class Identification(BaseModel):
    """File identification datamodel."""

    puid: Optional[str] = Field(...)
    signature: Optional[str] = Field(...)
    warning: Optional[str]
