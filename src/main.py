import os
import shutil
from config import STATIC_DIR, PUBLIC_DIR


def main():
    if os.path.exists(PUBLIC_DIR):
        shutil.rmtree(PUBLIC_DIR)
        os.mkdir(PUBLIC_DIR)

    copy_contents(STATIC_DIR, PUBLIC_DIR)


def copy_contents(source_dir, target_dir):
    if not os.path.exists(target_dir):
        os.mkdir(target_dir)

    entries = os.listdir(source_dir)
    for entry in entries:
        copy_source = os.path.join(source_dir, entry)
        if os.path.isfile(copy_source):
            shutil.copy(copy_source, target_dir)
            print(f'copied "{copy_source}" to {os.path.join(target_dir, entry)}')
        else:
            copy_target = os.path.join(target_dir, entry)
            copy_contents(copy_source, copy_target)


main()
