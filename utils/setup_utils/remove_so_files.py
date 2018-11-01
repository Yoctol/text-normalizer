from pathlib import Path
import os


def remove_so_files():
    so_paths = sorted(
        Path('./strpipe').rglob(
            "*.cpython-36m-x86_64-linux-gnu.so",
        ),
    )
    for path in so_paths:
        os.remove(str(path.resolve()))


if __name__ == '__main__':
    remove_so_files()
