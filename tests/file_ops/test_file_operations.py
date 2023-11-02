import os

import pytest

from src.file_ops.file_operations import (
    copy_file,
    find_files_in_directory,
    copy_all_files,
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


def test_find_files_in_directory_multiple(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p1 = d / "testfile1.txt"
    p1.write_text("content")
    p2 = d / "testfile2.txt"
    p2.write_text("content")

    files = find_files_in_directory(d)
    assert len(files) == 2
    assert os.path.basename(files[0]) == "testfile1.txt"
    assert os.path.basename(files[1]) == "testfile2.txt"


def test_find_files_in_directory_with_no_files(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()

    files = find_files_in_directory(d)
    assert len(files) == 0


def test_directory_does_not_exist(tmp_path):
    with pytest.raises(ValueError, match="Provided path is not a valid directory"):
        find_files_in_directory(tmp_path / "nonexistent_dir")


def test_copy_all_files_single(tmp_path):
    src_dir = tmp_path / "src"
    src_dir.mkdir()
    dest_dir = tmp_path / "dest"
    dest_dir.mkdir()
    p = src_dir / "testfile.txt"
    p.write_text("content")

    copy_all_files(src_dir, dest_dir)
    assert os.path.isfile(dest_dir / "testfile.txt")


def test_copy_all_files_multiple(tmp_path):
    src_dir = tmp_path / "src"
    src_dir.mkdir()
    dest_dir = tmp_path / "dest"
    dest_dir.mkdir()
    p1 = src_dir / "testfile1.txt"
    p1.write_text("content")
    p2 = src_dir / "testfile2.txt"
    p2.write_text("content")

    copy_all_files(src_dir, dest_dir)
    assert os.path.isfile(dest_dir / "testfile1.txt")
    assert os.path.isfile(dest_dir / "testfile2.txt")


def test_copy_all_files_empty_directory(tmp_path):
    src_dir = tmp_path / "src"
    src_dir.mkdir()
    dest_dir = tmp_path / "dest"
    dest_dir.mkdir()

    copy_all_files(src_dir, dest_dir)
    # make dest_dir from path to
    assert not list(dest_dir.iterdir())


def test_copy_all_files_recursively(tmp_path):
    src_dir = tmp_path / "src"
    src_dir.mkdir()
    sub_dir = src_dir / "sub"
    sub_dir.mkdir()
    sub_sub_dir = sub_dir / "subsub"
    sub_sub_dir.mkdir()

    (src_dir / "file1.txt").write_text("Content of file 1")
    (sub_dir / "file2.txt").write_text("Content of file 2")
    (sub_sub_dir / "file3.txt").write_text("Content of file 3")

    dest_dir = tmp_path / "dest"
    dest_dir.mkdir()

    copy_all_files(src_dir, dest_dir)

    assert os.path.isfile(dest_dir / "file1.txt")
    assert os.path.isfile(dest_dir / "sub" / "file2.txt")
    assert os.path.isfile(dest_dir / "sub" / "subsub" / "file3.txt")
