import pytest
from src.app import EmptyContentError, write_file
from pathlib import Path

directory = Path("data") / "config.json"
def test_empty_content_error():
    with pytest.raises(EmptyContentError):
        write_file(directory , "Nothing", "")
