# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------

from pydantic import ValidationError

import pytest
from acamodels import Identification

# -----------------------------------------------------------------------------
# Tests
# -----------------------------------------------------------------------------


class TestInit:
    puid = "fmt/test"
    signature = "Test signature"
    warning = "This is a test"

    def test_required_fields(self):
        id_ = Identification(puid=None, signature=None)
        assert id_.puid is None
        assert id_.signature is None
        assert id_.warning is None

    def test_optional_fields(self):
        id_ = Identification(
            puid=self.puid, signature=self.signature, warning=self.warning
        )
        assert id_.puid == self.puid
        assert id_.signature == self.signature
        assert id_.warning == self.warning

    def test_validators(self):
        sig_missing = "Signature missing for PUID"
        puid_missing = "PUID missing for signature"

        with pytest.raises(ValidationError, match=sig_missing):
            Identification(puid=self.puid, signature=None)

        with pytest.raises(ValidationError, match=puid_missing):
            Identification(puid=None, signature=self.signature)
