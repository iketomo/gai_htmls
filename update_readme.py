import os
from datetime import datetime

# 除外するファイルやディレクトリ
EXCLUDE_FILES = {"update_readme.py", ".git", "README.md"}

# README.mdの内容を生成
content = """
# 自動生成されたREADME

このリポジトリには以下のファイルが含まれています：

"""

# ファイル一覧を取得
files = [f for f in os.listdir(".") if f not in EXCLUDE_FILES]

for file in files:
    # ファイルの作成日時を取得
    created_time = datetime.fromtimestamp(os.path.getctime(file)).strftime("%Y-%m-%d %H:%M:%S")

    # ファイルをリンク形式で追加（全てのファイル）
    content += f"- [{file}](./{file}) （作成日: {created_time}）\n"

# README.mdを書き換え
with open("README.md", "w") as readme_file:
    readme_file.write(content)
