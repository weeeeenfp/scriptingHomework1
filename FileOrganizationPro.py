import os
import shutil

# 找到目前使用者的「下載」資料夾
downloads = os.path.join(os.path.expanduser("~"), "Downloads")

# 定義分類規則
file_types = {
    "Exe": [".exe"],
    "Zip": [".zip"],
    "Images": [".png", ".jpg"],
    "PDF": [".pdf"],
    "Others": []  # 沒有在上面規則的副檔名 → 丟這裡
}

# 建立副檔名 → 資料夾對應表
ext_map = {}
for folder, exts in file_types.items():
    for ext in exts:
        ext_map[ext.lower()] = folder

# 遍歷下載資料夾
for file in os.listdir(downloads):
    filepath = os.path.join(downloads, file)

    if os.path.isfile(filepath):  # 只處理檔案
        ext = os.path.splitext(file)[1].lower()  # 取副檔名 (含.)

        # 找到分類資料夾，若無則丟進 Others
        folder = ext_map.get(ext, "Others")
        target = os.path.join(downloads, folder)

        # 如果資料夾不存在，就建立
        os.makedirs(target, exist_ok=True)

        # 目標路徑
        dest = os.path.join(target, file)


        # 移動檔案
        shutil.move(filepath, dest)

print("Done")
