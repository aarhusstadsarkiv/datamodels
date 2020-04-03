"""Shared testing fixtures.

"""

# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------
from pathlib import Path

import pytest

# -----------------------------------------------------------------------------
# Fixtures
# -----------------------------------------------------------------------------


@pytest.fixture
def temp_dir(tmpdir_factory):
    temp_dir: str = tmpdir_factory.mktemp("temp_dir")
    return Path(temp_dir)
