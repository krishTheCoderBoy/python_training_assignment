import glob
import re

files = glob.glob("*")

for file in files:
    # Allow both "data.csv" and "data_*.csv"
    if re.match(r"^data(_.*)?\.csv$", file):
        print(f"CSV Match: {file}")
