import os

# 除外するファイルやディレクトリ
EXCLUDE_FILES = {"update_readme.py", ".git", ".github", "README.md"}

content = """
# 自動生成されたREADME

このリポジトリには以下のファイルが含まれています（ファイル名順）:

"""

# ファイル一覧を取得（除外ファイルをのぞく）
file_list = [f for f in os.listdir('.') if f not in EXCLUDE_FILES]

# ファイル名順にソート
file_list.sort(reverse=True)

# READMEの内容を生成（作成日の記載は不要）
for file in file_list:
    content += f"- [{file}](./{file})\n"

# README.mdを書き換え
with open("README.md", "w") as readme_file:
    readme_file.write(content)
