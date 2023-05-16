"""
Имитационное моделирование
"""

import datetime, random

def getBirthdays(numBDays):
    """
    Функция берет число, введенное пользователем и возвращает список из случайных дат
    """
    birthdays = []
    for i in range(numBDays):
        startBirthday = datetime.date(2001, 1, 1)
        deltaBirthday = datetime.timedelta(random.randint(0, 364))
        birthday = startBirthday + deltaBirthday
        birthdays.append(birthday)
    return birthdays

def getMatches(birthdays):
    """
    Функция берет список из случайных дат и возвращает одинаковые элементы, если они есть
    """
    if len(birthdays) == len(set(birthdays)):
        return None
    else:
        for a, birthdayA in enumerate(birthdays):
            for b, birthdayB in enumerate(birthdays):
                if birthdayA == birthdayB:
                    return birthdayA


print('Это имитационное моделирование, которая показывает, что даже в маленькой группе людей')
print('вероятность совпадения день рождения нескольких человек очень высокая.')
print()
print()

while True: # Запрашивает пользователя ввести число до тех пор, пока пользователь не введет корректные данные
    print('Сколько дат вы хотитие генерировать? (Макс 100)')
    response = input('> ')
    if response.isdecimal() and 0 < int(response) <= 100:
        numBDays = int(response)
        break

# Кортеж из имен месяцев для красивого и понятного вывода дат
MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', "May", 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

# Вызов функции, которая генерирует случайные даты, которые присваиваются к переменной
birthdays = getBirthdays(numBDays)

# Выводим случайно сгенерированные даты
print('Вот случайные даты:\n')
for i, birthday in enumerate(birthdays):
    if i != 0:
        print(', ', end='')
    monthName = MONTHS[birthday.month - 1]
    dateText = f'{monthName} {birthday.day}'
    print(dateText, end='')
print()
print()

# Вызов функции, которая ищет соответствия в списке
match = getMatches(birthdays)

# Проверка на совпадение
if match != None:
    monthName = MONTHS[match.month - 1]
    dateText = f'{monthName} {match.day}'
    print(f'В этом списке совпедение есть это: {dateText}')
else:
    print('В этом списке совпадение нет')
print()
print()

print('Генерация еще 100,000 таких случайных дат')
input('Чтобы начать имитационное моделирование нажмите Enter...')
# Начинаем 100,000 имитационного моделирования
simMatchs = 0

for i in range(100_000):
    if i % 10_000 == 0:
        print(i, 'имитационных моделировании выполнены...')
    birthdays = getBirthdays(numBDays)
    if getMatches(birthdays) != None:
        simMatchs += 1
print('Имитационное моделирование выполнено.')
print()

probability = round(simMatchs / 100_000 * 100, 2)

print('Было выполнено 100,000 имитационных моделировании из', numBDays, 'людей.')
print("Из них в", simMatchs, 'были совпадения.')
print('Это означает, что вероятность совпадении в группе из', numBDays, 'людей', probability, '%,')
print('если генерировать такие случайные группы 100,000 раз.')
