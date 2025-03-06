import os
from datetime import datetime

# 除外するファイルやディレクトリ
EXCLUDE_FILES = {"update_readme.py", ".git", ".github", "README.md"}

# README.mdの内容を生成
content = """
# 自動生成されたREADME

このリポジトリには以下のファイルが含まれています（作成日順、降順）：

"""

# ファイル一覧を取得し、作成日とともにリストに格納
files_with_dates = []
for file in os.listdir("."):
    if file not in EXCLUDE_FILES:
        created_time = os.path.getctime(file)
        files_with_dates.append((file, created_time))

# 作成日でソート（降順）
files_with_dates.sort(key=lambda x: x[1], reverse=True)

# ソートされたリストでREADMEの内容を生成
for file, created_time in files_with_dates:
    # 日時をフォーマット
    formatted_time = datetime.fromtimestamp(created_time).strftime("%Y-%m-%d %H:%M:%S")
    # ファイルをリンク形式で追加
    content += f"- [{file}](./{file}) （作成日: {formatted_time}）\n"

# README.mdを書き換え
with open("README.md", "w") as readme_file:
    readme_file.write(content)
