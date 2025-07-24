import os
import shutil


def copy_static_contents(source_dir, target_dir):
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    for filename in os.listdir(source_dir):
        from_path = os.path.join(source_dir, filename)
        to_path = os.path.join(target_dir, filename)
        if os.path.isfile(from_path):
            shutil.copy(from_path, to_path)
            print(f'copied "{from_path}" to {to_path}')
        else:
            copy_static_contents(from_path, to_path)
