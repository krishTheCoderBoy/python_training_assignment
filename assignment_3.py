import re

phone_numbers = [
    "(123) 456-7890",
    "123-456-7890",
    "(987) 654-3210",
    "9876543210"
]

for number in phone_numbers:
    if re.match(r"^\(\d{3}\) \d{3}-\d{4}$", number):
        print(number)
