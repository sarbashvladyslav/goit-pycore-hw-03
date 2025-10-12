from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

users = [
    {"name": "John Doe", "birthday": "1985.10.12"},
    {"name": "Charlie Davis", "birthday": "1995.10.15"},
    {"name": "David Brown", "birthday": "1993.1.16"},
    {"name": "Jane Smith", "birthday": "1990.10.18"},
    {"name": "Eve Wilson", "birthday": "1988.10.20"},
    {"name": "Alice Johnson", "birthday": "1975.9.20"},
    {"name": "Bob Brown", "birthday": "2000.11.15"},
    {"name": "Grace Lee", "birthday": "1992.12.14"},
    {"name": "Hank Miller", "birthday": "1983.11.16"},
]

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    new_list = []

    for user in users:
        parsed_birthday_date = datetime.strptime(user['birthday'], "%Y.%m.%d").date()
        birthday_this_year = datetime(month=parsed_birthday_date.month, day=parsed_birthday_date.day, year=today.year).date()
        current_month = birthday_this_year.month == today.month
        birthday_within_a_week = 0 <= (birthday_this_year - today).days <= 7
        birthday_on_saturday = birthday_this_year.isoweekday() == 6
        birthday_on_sunday = birthday_this_year.isoweekday() == 7

        # 4. Перевірте, чи вже минув день народження в цьому році (if birthday_this_year < today). Якщо так, розгляньте дату на наступний рік.
        # Як позуміти цю умову? Якщо нам потрібно додавати в список ДН в наступному році, то можна прибрати continue і додати в список кодом нижче (33-34 рядок)
        if birthday_this_year < today:
            continue
            # relativedelta - для коректного переходу на наступний рік (високосний рік і т.д.)
            # congratulation_date = datetime.strftime(birthday_this_year + relativedelta(years=+1), "%Y-%m-%d")
            # new_list.append({"name": user["name"], "congratulation_date": congratulation_date})
        elif birthday_within_a_week and current_month:
            if birthday_on_saturday:
                congratulation_date = datetime.strftime(birthday_this_year + timedelta(days=2), "%Y-%m-%d") 
                new_list.append({"name": user["name"], "congratulation_date": congratulation_date})
            elif birthday_on_sunday:
                congratulation_date = datetime.strftime(birthday_this_year + timedelta(days=1), "%Y-%m-%d")
                new_list.append({"name": user["name"], "congratulation_date": congratulation_date})
            else:
                congratulation_date = datetime.strftime(birthday_this_year, "%Y-%m-%d")
                new_list.append({"name": user["name"], "congratulation_date": congratulation_date})

    return new_list

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
