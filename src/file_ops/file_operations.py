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


def find_files_in_directory(directory: str) -> List[str]:
    if not os.path.isdir(directory):
        raise ValueError("Provided path is not a valid directory")

    return [
        os.path.join(directory, f)
        for f in os.listdir(directory)
        if os.path.isfile(os.path.join(directory, f))
    ]

def find_all_files_recursively(directory: str) -> List[str]:
    if not os.path.isdir(directory):
        raise ValueError("Provided path is not a valid directory")

    return [
        os.path.join(dirpath, f)
        for dirpath, _, filenames in os.walk(directory)
        for f in filenames
    ]

def replace_file(src:str, new_content:str) -> None:
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
