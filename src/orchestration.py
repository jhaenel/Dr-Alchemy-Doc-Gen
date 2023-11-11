from src.AI.generate_comments import generate_comments
from src.file_ops.file_operations import (
    copy_all_files,
    find_all_files_recursively,
    read_file,
    replace_file,
    create_machine_readable_copies,
)


def orchestrate():
    copy_all_files("src", "doc_gen")
    for file in find_all_files_recursively("doc_gen"):
        replace_file(src=file, new_content=generate_comments(read_file(file)))
    create_machine_readable_copies("doc_gen","doc_gen_machine_readable")

if __name__ == "__main__":
    orchestrate()
