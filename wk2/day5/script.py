from pathlib import Path 

file_path = Path("developer.txt")

if file_path.exists():
    print("files exists")