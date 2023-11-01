import os

import pytest

from src.file_ops.copy_file import copy_file


def test_copy_file_valid(tmp_path):
    src_file = tmp_path / "source.txt"
    src_file.write_text("Hello, World!")

    dest_dir = tmp_path / "dest"
    dest_dir.mkdir()

    copied_path = copy_file(src_file, dest_dir)
    copied_file = tmp_path / "dest" / "source.txt"

    assert os.path.exists(copied_file)
    assert str(copied_path) == str(copied_file)
    assert copied_file.read_text() == "Hello, World!"


def test_copy_file_invalid_src(tmp_path):
    with pytest.raises(ValueError, match="Source is not a valid file"):
        copy_file(str(tmp_path), tmp_path)


def test_copy_file_src_does_not_exist(tmp_path):
    dest_dir = tmp_path / "dest"
    dest_dir.mkdir()

    with pytest.raises(ValueError, match="Source is not a valid file"):
        copy_file(tmp_path / "nonexistent_file.txt", dest_dir)
