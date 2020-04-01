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

    @root_validator
    def check_puid_sig(cls, values: Dict[Any, Any]) -> Dict[Any, Any]:
        """Validate that a PUID cannot have an empty signature
        or vice versa."""

        puid = values["puid"]
        signature = values["signature"]

        if puid is not None and signature is None:
            raise ValueError(f"Signature missing for PUID {puid}.")

        if signature is not None and puid is None:
            raise ValueError(f"PUID missing for signature {signature}.")

        return values
