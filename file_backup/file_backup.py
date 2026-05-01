import datetime
import schedule
import shutil
import os
import time

SOURCE_DIR = R"F:\Tmp"
DEST_DIR = R"F:\Bakup"


def copy_folder_to_dest(source, dest):
    today = datetime.date.today()
    dest_dir = os.path.join(dest, str(today))

    try:
        shutil.copytree(source, dest_dir)
        print(f"Copy {source} to {dest_dir} success!")
    except FileExistsError:
        print(f"Error: {dest_dir} already exist!")


# 每天执行
schedule.every().day.at("08:55").do(lambda: copy_folder_to_dest(SOURCE_DIR, DEST_DIR))

while True:
    schedule.run_pending()
    time.sleep(60)
