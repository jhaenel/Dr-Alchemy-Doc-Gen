from src.AI.generate_comments import generate_comments
from src.file_ops.file_operations import (
    copy_all_files,
    find_all_files_recursively,
    read_file,
    replace_file,
    create_machine_readable_copies,
)

def orchestrate(src:str, dest:str)->None:
    copy_all_files(src, dest)
    for file in find_all_files_recursively(dest):
        replace_file(src=file, new_content=generate_comments(read_file(file)))
    create_machine_readable_copies(dest, "doc_gen_machine_readable")


if __name__ == "__main__":
    orchestrate()
