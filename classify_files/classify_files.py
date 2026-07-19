import os
import shutil

CLASSIFY_DIR_PATH = R"F:\Tmp"
DST_BASE_DIR_PATH = R"F:\Tmp"
EXTNAME_DIRNAME = {
    ".txt": "txt"
}

def check_path(path: str) -> bool:
    return os.path.exists(path)


def is_dir(path: str) -> bool:
    return os.path.isdir(path)


def list_dir(path: str):
    if not check_path(path):
        print(f"Path: {path} not exists")
        return [""]

    if not is_dir(path):
        print(f"Path: {path} is not directory")
        return [""]

    return os.listdir(path)


def classify_files(file: str):
    idx = file.rfind(".")
    if idx == -1:
        return
    ext_name = file[idx:]
    # print(f"ext_name: {ext_name}")
    dir = EXTNAME_DIRNAME.get(ext_name, "")
    # print(f"dir: {dir}")
    if dir == "":
        return
    dir_path = os.path.join(DST_BASE_DIR_PATH, dir)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    file_path = os.path.join(CLASSIFY_DIR_PATH, file)
    print(f"move {file_path} to {dir_path}")
    _ = shutil.move(file_path, dir_path)


if __name__ == "__main__":
    files:list[str] = list_dir(CLASSIFY_DIR_PATH)
    for file in files:
        classify_files(file)