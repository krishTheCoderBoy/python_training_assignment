import glob
import re

txt_files = glob.glob("*.txt")

for file in txt_files:
    with open(file, "r") as f:
        content = f.read()
        if re.search(r"Python", content, re.IGNORECASE):
            print(f"Found 'Python' in: {file}")
        else:
            print(f"No 'Python' found in: {file}")
