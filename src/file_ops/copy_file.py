import os
import shutil


    dest_path = os.path.join(dest_dir, os.path.basename(src))
    shutil.copy2(src, dest_path)
    return dest_path
