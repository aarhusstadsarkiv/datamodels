# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------

from typing import Any, Dict, Optional

from pydantic import BaseModel, Field, root_validator

# -----------------------------------------------------------------------------
# Model
# -----------------------------------------------------------------------------


class Identification(BaseModel):
    """File identification datamodel."""

    puid: Optional[str] = Field(...)
    signature: Optional[str] = Field(...)
    warning: Optional[str]

    @root_validator
    def check_puid_sig(cls, fields: Dict[Any, Any]) -> Dict[Any, Any]:
        """Validate that a PUID cannot have an empty signature
        or vice versa."""

        puid = fields["puid"]
        signature = fields["signature"]

        if puid is not None and signature is None:
            raise ValueError(f"Signature missing for PUID {puid}.")

        if signature is not None and puid is None:
            raise ValueError(f"PUID missing for signature {signature}.")

        return fields
