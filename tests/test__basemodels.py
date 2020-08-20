# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------

from acamodels._basemodels import EntityModel

# -----------------------------------------------------------------------------
# Tests
# -----------------------------------------------------------------------------


class TestInit:
    def test_required_fields(self):
        assert EntityModel()

    def test_optional_fields(self):
        pass

    def test_validators(self):
        pass
