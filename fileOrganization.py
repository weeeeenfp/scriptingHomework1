import os
import shutil

# 指定要整理的資料夾
source = r"C:\Users\wendy\OneDrive\桌面\scriptHomework\Downloads"   # ← 修改成你要整理的資料夾

# 想要獨立分類的副檔名
categories = ["exe", "zip", "png", "jpg", "pdf"]

# 走訪資料夾中的所有檔案
for file in os.listdir(source):
    filepath = os.path.join(source, file)

    if os.path.isfile(filepath):  # 只處理檔案
        ext = os.path.splitext(file)[1].lower().strip('.')  # 取得副檔名（小寫，去掉.）

        # 決定分類
        if ext in categories:
            folder = ext
        else:
            folder = "others"

        # 目標資料夾
        target = os.path.join(source, folder)
        os.makedirs(target, exist_ok=True)

        # 移動檔案
        shutil.move(filepath, os.path.join(target, file))

print("✅ 檔案已依副檔名分類完成！")
