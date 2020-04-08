# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------

import pytest
from datamodels._internals import size_fmt

# -----------------------------------------------------------------------------
# Tests
# -----------------------------------------------------------------------------


class TestInternalFunctions:
    def test_size_fmt(self):
        assert size_fmt(2 ** 0) == "1.0 B"
        assert size_fmt(2 ** 10) == "1.0 KiB"
        assert size_fmt(2 ** 20) == "1.0 MiB"
        assert size_fmt(2 ** 30) == "1.0 GiB"
        assert size_fmt(2 ** 40) == "1.0 TiB"
