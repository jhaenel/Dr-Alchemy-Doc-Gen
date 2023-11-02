import os
import shutil


def copy_file(src, dest_dir):
    if not os.path.isfile(src):
        raise ValueError("Source is not a valid file")
    if not os.path.isdir(dest_dir):
        raise ValueError("Destination is not a valid directory")

    dest_path = os.path.join(dest_dir, os.path.basename(src))
    shutil.copy2(src, dest_path)
    return dest_path


def find_files_in_directory(directory: str):
    if not os.path.isdir(directory):
        raise ValueError("Provided path is not a valid directory")

    return [
        os.path.join(directory, f)
        for f in os.listdir(directory)
        if os.path.isfile(os.path.join(directory, f))
    ]
