import os

import pytest

from src.file_ops.file_operations import (
    copy_file,
    find_files_in_directory,
)


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


def test_copy_file_invalid_dest(tmp_path):
    src_file = tmp_path / "source.txt"
    src_file.write_text("Hello, World!")

    with pytest.raises(ValueError, match="Destination is not a valid directory"):
        copy_file(src_file, tmp_path / "nonexistent_dir")


def test_find_files_in_directory_single(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "testfile.txt"
    p.write_text("content")

    files = find_files_in_directory(d)
    assert len(files) == 1
    assert os.path.basename(files[0]) == "testfile.txt"


def test_find_files_in_directory_with_no_files(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()

    files = find_files_in_directory(d)
    assert len(files) == 0
