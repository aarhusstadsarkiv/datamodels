# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------

from pathlib import Path
from acamodels.aca_base import ACABase

# -----------------------------------------------------------------------------
# Tests
# -----------------------------------------------------------------------------


class NewModel(ACABase):
    name: str
    age: int = 32


class EncodeModel(ACABase):
    path: Path


class TestInit:
    def test_required_fields(self):
        assert ACABase()


class TestValidators:
    def test_validation(self):
        assert True


class TestMethods:
    def test_dump(self, temp_dir):
        new_model = NewModel(name="Test med æ")
        test_file = temp_dir / "test_file.json"
        new_model.dump(test_file)
        assert test_file.read_text(encoding="utf-8") == new_model.json(
            indent=2, ensure_ascii=False
        )

    def test_encode(self):
        new_model = EncodeModel(path=Path("test"))
        encoded_model = new_model.encode()
        assert isinstance(encoded_model["path"], str)
