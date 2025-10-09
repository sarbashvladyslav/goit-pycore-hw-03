import re

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

corrected_numbers = []

def normalize_phone(phone_number: str) -> str:
    pattern = r"\+?\d+"
    updated_number = re.findall(pattern, phone_number)
    new_string = ""

    for i in updated_number:
        new_string += i
    if new_string[0] == "0":
        new_string = "+38" + new_string
    elif new_string[0] != "+":
        new_string = "+" + new_string

    return new_string

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)