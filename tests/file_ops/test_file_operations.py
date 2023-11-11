import os

import pytest

from src.file_ops.file_operations import (
    copy_file,
    find_all_files_recursively,
    copy_all_files,
    read_file,
    replace_file,
    write_file_content_for_machine,
    create_machine_readable_copies,
)


def test_read_file_valid(tmp_path):
    p = tmp_path / "testfile.txt"
    p.write_text("content")

    assert read_file(p) == "content"


def test_read_file_invalid(tmp_path):
    with pytest.raises(ValueError, match="Provided path is not a valid file"):
        read_file(tmp_path / "nonexistent_file.txt")


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

    files = find_all_files_recursively(d)
    assert len(files) == 1
    assert os.path.basename(files[0]) == "testfile.txt"


def test_find_files_in_directory_multiple(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p1 = d / "testfile1.txt"
    p1.write_text("content")
    p2 = d / "testfile2.txt"
    p2.write_text("content")

    files = find_all_files_recursively(d)
    assert len(files) == 2
    assert os.path.basename(files[0]) in ["testfile1.txt", "testfile2.txt"]
    assert os.path.basename(files[1]) in ["testfile1.txt", "testfile2.txt"]


def test_find_files_in_directory_recursively(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    sub_d = d / "subsub"
    sub_d.mkdir()
    p = sub_d / "testfile.txt"
    p.write_text("content")

    files = find_all_files_recursively(d)
    assert len(files) == 1
    assert os.path.basename(files[0]) == "testfile.txt"


def test_find_files_in_directory_with_no_files(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()

    files = find_all_files_recursively(d)
    assert len(files) == 0


def test_directory_does_not_exist(tmp_path):
    with pytest.raises(ValueError, match="Provided path is not a valid directory"):
        find_all_files_recursively(tmp_path / "nonexistent_dir")


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


def test_replace_file(tmp_path):
    p = tmp_path / "testfile.txt"
    p.write_text("content")

    replace_file(p, "new content")

    assert p.read_text() == "new content"


def test_replace_file_dne(tmp_path):
    with pytest.raises(ValueError, match="Source is not a valid file"):
        replace_file(tmp_path / "nonexistent_file.txt", "new content")


def test_replace_file_permission_denied(tmp_path):
    p = tmp_path / "testfile.txt"
    p.write_text("content")
    p.chmod(0o000)

    with pytest.raises(PermissionError):
        replace_file(p, "new content")


def test_write_file_content_for_machines(tmp_path):
    dest_file_path = tmp_path / "dest.txt"
    src_file_path = tmp_path / "src.txt"
    src_file_path.write_text("Hello\nWorld")

    with open(dest_file_path, "w") as dest_file:
        write_file_content_for_machine(dest_file, src_file_path)

    assert dest_file_path.read_text() == "File: {}\n1: Hello\n2: World".format(
        src_file_path
    )

def test_write_file_content_for_machines_with_empty_file(tmp_path):
    dest_file_path = tmp_path / "dest.txt"
    src_file_path = tmp_path / "src.txt"
    src_file_path.write_text("")

    with open(dest_file_path, "w") as dest_file:
        write_file_content_for_machine(dest_file, src_file_path)

    assert dest_file_path.read_text() == "File: {}\n".format(src_file_path)

def test_create_machine_readable_copies(tmp_path):
    src_dir = tmp_path / "src"
    src_dir.mkdir()
    (src_dir / "file1.txt").write_text("Hello\nWorld")
    (src_dir / "file2.txt").write_text("Foo\nBar")

    dest_dir = tmp_path / "dest"
    dest_dir.mkdir()

    create_machine_readable_copies(src_dir, dest_dir)

    actual_content = (dest_dir / "machine_readable.txt").read_text()

    expected_content_file1 = "File: {}\n1: Hello\n2: World".format(
        src_dir / "file1.txt"
    )
    expected_content_file2 = "File: {}\n1: Foo\n2: Bar".format(src_dir / "file2.txt")

    assert expected_content_file1 in actual_content
    assert expected_content_file2 in actual_content
