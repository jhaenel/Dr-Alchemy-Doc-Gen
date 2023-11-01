import os
import shutil


def copy_file(src, dest_dir):
    if not os.path.isfile(src):
        raise ValueError("Source is not a valid file")
    dest_path = os.path.join(dest_dir, os.path.basename(src))
    shutil.copy2(src, dest_path)
    return dest_path
