import os

SEARCH_PATH = R"E:\Projects\Rust"
SEARCH_STR = R"Hello"

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

def pattern_match(pattern: str, file: str) -> bool:
    if pattern in file:
        return True
    else:
        return False

if __name__ == "__main__":
    files = list_dir(SEARCH_PATH)
    for file in files:
        if pattern_match(SEARCH_STR, file):
            print(f"Find file: {file}")