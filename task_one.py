from datetime import datetime
import re

def get_days_from_today(date: str) -> int:
    current_date = datetime.today().date()
    # будь-яке відьемне число перетвориться в позитивне, так як "-" спецсимвол (можно покращити)
    pattern = r"\d+"
    split_time = re.findall(pattern, date)

    if len(split_time) != 3:
        return "Error: Incorrect date format. Please use YYYY-MM-DD."
    
    # В нас завжди буде 3 елементи str які потрібно перетворити в int(прибирає зайві нулі)
    for i in range(0, 3):
        split_time[i] = int(split_time[i])

    if split_time[1] < 1 or split_time[1] > 12:
        return "Error: Month must be between 1 and 12."
    if split_time[2] < 1 or split_time[2] > 31:
        return "Error: Day must be between 1 and 31."

    # Отримуемо дату у потрібному форматі YYYY-MM-DD об'єкта datetime
    date = datetime(year=split_time[0], month=split_time[1], day=split_time[2]).date()

    # При застосуванні выднімання дат утворюється об'єкт timedelta до якого можна звернутися за кількістю днів через атрибут days
    temporary_difference = (current_date - date).days
    
    return temporary_difference

enter_date = input("Enter date in format YYYY-MM-DD: ")

print(get_days_from_today(enter_date))