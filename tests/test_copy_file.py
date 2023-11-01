import os

from src.file_ops.copy_file import copy_file


def test_copy_file_valid(tmp_path):
    src_file = tmp_path / "source.txt"
    src_file.write_text("Hello, World!")

    dest_dir = tmp_path / "dest"
    dest_dir.mkdir()

    copied_path = copy_file(src_file, dest_dir)
    copied_file = tmp_path / "dest" / "source.txt"

    assert os.path.exists(copied_file)
    assert copied_path == copied_file
    assert copied_file.read_text() == "Hello, World!"
