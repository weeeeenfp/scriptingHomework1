import os
import shutil

# 要整理的資料夾
source = r"C:\Users\wendy\OneDrive\桌面\scriptHomework\Downloads"  # ← 修改這裡

# 定義分類規則 (dict)
file_types = {
    "Exe": [".exe"],
    "Zip": [".zip"],
    "Images": [".png", ".jpg"],
    "PDF": [".pdf"],
    "Others": []  # 其餘副檔名
}

# 建立副檔名 → 資料夾對應表
ext_map = {}
for folder, exts in file_types.items():
    for ext in exts:
        ext_map[ext.lower()] = folder

# 走訪來源資料夾中的檔案
for file in os.listdir(source):
    filepath = os.path.join(source, file)
    if os.path.isfile(filepath):  # 確保是檔案
        ext = os.path.splitext(file)[1].lower()  # 取副檔名 (含.)

        # 判斷分類
        folder = ext_map.get(ext, "Others")
        target = os.path.join(source, folder)

        # 若資料夾不存在就建立
        os.makedirs(target, exist_ok=True)

        # 移動檔案
        shutil.move(filepath, os.path.join(target, file))

print("✅ 檔案已依 dict 規則分類完成！")
