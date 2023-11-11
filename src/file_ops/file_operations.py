import os
import shutil
from typing import List


def read_file(path: str) -> str:
    if not os.path.isfile(path):
        raise ValueError("Provided path is not a valid file")

    with open(path, "r") as f:
        return f.read()


def copy_file(src: str, dest_dir: str) -> str:
    if not os.path.isfile(src):
        raise ValueError("Source is not a valid file")
    if not os.path.isdir(dest_dir):
        raise ValueError("Destination is not a valid directory")

    dest_path = os.path.join(dest_dir, os.path.basename(src))
    shutil.copy2(src, dest_path)
    return dest_path


def is_unicodable(path: str) -> bool:
    try:
        read_file(path)
        return True
    except UnicodeDecodeError:
        return False


def find_all_files_recursively(directory: str) -> List[str]:
    if not os.path.isdir(directory):
        raise ValueError("Provided path is not a valid directory")

    return [
        os.path.join(dirpath, f)
        for dirpath, _, filenames in os.walk(directory)
        for f in filenames
        if is_unicodable(os.path.join(dirpath, f))
    ]


def replace_file(src: str, new_content: str) -> None:
    if not os.path.isfile(src):
        raise ValueError("Source is not a valid file")

    with open(src, "w") as f:
        f.write(new_content)


def copy_all_files(src: str, dest: str) -> None:
    for dirpath, _, filenames in os.walk(src):
        dest_dir = os.path.join(dest, os.path.relpath(dirpath, src))
        os.makedirs(dest_dir, exist_ok=True)
        for file in filenames:
            shutil.copy2(os.path.join(dirpath, file), dest_dir)

def write_file_content_for_machine(dest_file, src_file_path):
    with open(src_file_path, 'r') as src_file:
        dest_file.write(f'File: {src_file_path}\n')
        for line_no, line in enumerate(src_file, start=1):
            dest_file.write(f'{line_no}: {line}')

