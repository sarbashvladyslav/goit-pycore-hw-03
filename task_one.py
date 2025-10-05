from datetime import datetime
import re

"""    # 1 Варіант
def get_days_from_today(date: str) -> int:
    current_date = datetime.today().date()
    # будь-яке від'ємне число перетвориться в позитивне, так як "-" це спецсимвол (можно покращити)
    pattern = r"\d+"
    split_time = re.findall(pattern, date)

    if len(split_time) != 3:
        return "Error: Incorrect date format. Please use YYYY-MM-DD."
    
    # В нас завжди буде 3 елементи str які потрібно перетворити в int(прибирає зайві нулі)
    for i in range(0, 3):
        split_time[i] = int(split_time[i])

    try:
        date = datetime(year=split_time[0], month=split_time[1], day=split_time[2]).date()
    except ValueError:
        return "Error: Invalid date. Please check the day or month"
    
    # При застосуванні выднімання дат утворюється об'єкт timedelta до якого можна звернутися за кількістю днів через атрибут days
    temporary_difference = (current_date - date).days
    
    return temporary_difference
"""

    # 2 Варіант
def get_days_from_today(date: str) -> int:
    current_date = datetime.today().date()

    try:
        time = datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError:
        return "Error: Incorrect date format. Please use YYYY-MM-DD."

    try:
        date = datetime(year=time.year, month=time.month, day=time.day).date()
    except ValueError:
        return "Error: Invalid date. Please check the day or month"
    
    # При застосуванні выднімання дат утворюється об'єкт timedelta до якого можна звернутися за кількістю днів через атрибут days
    temporary_difference = (current_date - date).days

    return temporary_difference

enter_date = input("Enter date in format YYYY-MM-DD: ")

print(get_days_from_today(enter_date))