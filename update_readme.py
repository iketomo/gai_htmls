import os

# README.mdの内容を生成
content = """
# 自動生成されたREADME

このリポジトリには以下のファイルが含まれています：

"""

# ディレクトリ内のファイル一覧を取得
files = os.listdir(".")
for file in files:
    content += f"- {file}\n"

# README.mdを書き換え
with open("README.md", "w") as readme_file:
    readme_file.write(content)
