from pathlib import Path 
from datetime import datetime

folder = Path("data")

folder.mkdir(exist_ok=True)

today = datetime.today()
now = datetime.now()
print(today.day)
print(now)