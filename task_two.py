import random
    
#Варіант 1    

def get_numbers_ticket(min: int, max: int, quantity: int) -> list[int]:
    if min < 1 or max > 1000 or min > max or quantity > (max - min + 1):
        return []

    winning_numbers = sorted(random.sample(range(min, max + 1), quantity))

    return winning_numbers

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)

    # Варіант 2
    # Одна з умов:
    # Функція повертає список випадково вибраних, відсортованих чисел.
    # Числа в наборі не повинні повторюватися.
    # Якщо параметри не відповідають заданим обмеженням, функція повертає пустий список.
    # - ця умова буде виконуватися, якщо замість помилок повертати пустий список.

# def from_string_to_numbers(string: str) -> list[int]:
#     string = string.split()
    
#     if len(string) != 3:
#         return "Error: Please enter exactly three numbers"
    
#     for i in range(len(string)):
#         if not string[i].isdigit():
#             return "Error: All inputs must be numbers"
        
#         string[i] = int(string[i])

#     return string

# def random_number(min: int, max: int) -> int:
#     return random.randint(min, max)

# def get_numbers_ticket(min: int, max: int, quantity: int) -> list[int]:
#     if min < 1:
#         # return []
#         return "Error: Min value should not be less than 1"
#     if min > max:
#         # return []
#         return "Error: Min value should be less than Max value"
#     if max > 1000:
#         # return []
#         return "Error: Max value should not be greater than 1000"
#     if quantity > (max - min + 1):
#         # return []
#         return "Error: Quantity of numbers should not be greater than the range of numbers"
#     # №1 варіант    
#     #winning_numbers = set()
#     #while len(winning_numbers) < quantity:
#     #    winning_numbers.add(random_number(min, max))

#     # №2 варіант. Для цього варіанту не потрібна функція random_number
#     winning_numbers = sorted(random.sample(range(min, max + 1), quantity))

#     return winning_numbers

# def lottery(date):
#     try:
#         min, max, quantity = from_string_to_numbers(date)
#     except ValueError:
#         # повертає помилку, якщо не вдасться розпакувати значення
#         return from_string_to_numbers(date)
    
#     winning_numbers = get_numbers_ticket(min, max, quantity)

#     return winning_numbers

# enter_numbers = input("Enter min, max and quantity of numbers separated by space. Example: 1 10 5: ")

# print(lottery(enter_numbers))