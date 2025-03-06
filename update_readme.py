import os
import subprocess
from datetime import datetime

# 除外するファイルやディレクトリ
EXCLUDE_FILES = {"update_readme.py", ".git", ".github", "README.md"}

# README.mdの内容を生成
content = """
# 自動生成されたREADME

このリポジトリには以下のファイルが含まれています（作成日順、降順）：

"""

# ファイル一覧を取得し、最終コミット日時とともにリストに格納
files_with_dates = []
for file in os.listdir("."):
    if file not in EXCLUDE_FILES:
        try:
            # Gitコマンドで最終コミット日時を取得
            result = subprocess.run(
                ["git", "log", "-1", "--format=%ct", file],
                capture_output=True,
                text=True,
                check=True
            )
            # タイムスタンプを取得し変換
            commit_timestamp = int(result.stdout.strip())
            files_with_dates.append((file, commit_timestamp))
        except subprocess.CalledProcessError:
            print(f"Failed to get commit date for {file}")

# 最終コミット日時でソート（降順）
files_with_dates.sort(key=lambda x: x[1], reverse=True)

# ソートされたリストでREADMEの内容を生成
for file, commit_timestamp in files_with_dates:
    formatted_time = datetime.fromtimestamp(commit_timestamp).strftime("%Y-%m-%d %H:%M:%S")
    content += f"- [{file}](./{file}) （最終更新日: {formatted_time}）\n"

# README.mdを書き換え
with open("README.md", "w") as readme_file:
    readme_file.write(content)
