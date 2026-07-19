import os
import shutil

INPUT_ZIP_FILE = R"F:\Tmp\test.zip"
OUTPUT_BASE_DIR = R"F:\Tmp"

def is_zipfile(path: str) -> bool:
    if not os.path.isfile(path):
        return False

    ext_name = path.split(".")[-1]
    if not ext_name.endswith("zip"):
        return False

    return True


def decompress(path: str) -> None:
    if not is_zipfile(path):
        return
    folder_name = path.split(".")[:-1]
    out_dir = os.path.join(OUTPUT_BASE_DIR, *folder_name)
    # print(f"out_dir: {out_dir}")
    shutil.unpack_archive(path, out_dir, format="zip")
    print(f"Decompress zip file: {path} to extract directory: {out_dir}")

if __name__ == "__main__":
    decompress(INPUT_ZIP_FILE)