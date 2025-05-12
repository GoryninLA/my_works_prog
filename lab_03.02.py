# Задание task_03_02_01.
# Выполнил: Горынин Л.А.
# Группа: ЦИБ-241



def foo(a):
    """
    Пузырьковая сортировка (Bubble Sort)
    Сложность: O(n^2) в худшем случае, O(1) по памяти..
    """
    for i in range(len(a), 0, -1): # O(n)
        for j in range(1, i): # O(n)
            if a[j-1] > a[j]: # O(1)
                a[j-1], a[j] = a[j], a[j-1] # O(1)
    return a # O(1)


a = [1, 2, 3, 4, 2, 1, 3, 4, 3, 5, -2, -2, 2, -2, 65, 2, 2]
print(foo(a))

# Общая сложность: O(n) * O(n) * O(1) = O(n^2)


# Задание task_03_02_02.
# Выполнил: Горынин Л.А.
# Группа: ЦИБ-241

def foo(i):
    """
    Преобразование целого числа i в строку

    Параметры:
        - i (int): число.

    Сложность: O(log n), n - входное число.
    """
    digits = "0123456789"  # O(1)
    if i == 0:   #O(1)
        return "0"  #O(1)
    result = ""  #O(1)
    while i > 0:  #O(log n)
        result = digits[i%10] + result  #O(1)
        i = i // 10  #O(1)
    return result  #O(1)




# Задание task_03_02_03.
# Выполнил: Горынин Л.А.
# Группа: ЦИБ-241

def foo(s):
    """вычисление суммы всех цифр в строке "s"

    Параметры:
        - s (str): строка.

    Сложность: O(n), n - длина строки.
    """
    val = 0  #O(1)
    for c in s:  #O(n)
        if c.isdigit():  #O(1)
            val += int(c)  #O(1)
    return val  #O(1)


# Задание task_03_02_04.
# Выполнил: Горынин Л.А.
# Группа: ЦИБ-241

def foo(n):
    """Возвращает список простых чисел от 1 до n

    Параметры:
        - n (int): число.

    Сложность: O(n^2).
    """
    res = [] 
    for i in range(1, n + 1): # O(n)
        divisors = 0 # O(1)
        j = 2 # O(1)
        while j < i and divisors == 0: # O(n)
            if i % j == 0: # O(1)
                divisors += 1 # O(1)
            j += 1 # O(1)

        if divisors == 0: # O(1)
            res.append(i) # O(1)

    return res # O(1)

#Общая сложность: O(n) * O(n) = O(n^2)


# Задание task_03_02_05.
# Выполнил: Горынин Л.А.
# Группа: ЦИБ-241

def foo(nums):
    """ Функция проверяет, есть ли в списке хотя бы одно четное число

    Параметры:
        - nums (list): список.

    Сложность: O(n).
    """
    for x in nums: # O(n)
        if x % 2 == 0: # O(1)
            return True # O(1)
    else: # O(1)
        return False # O(1)

#Общая сложность: O(n) = O(n)


# Задание task_03_02_06.
# Выполнил: Горынин Л.А.
# Группа: ЦИБ-241

def foo(nums):
    """Возвращает сумму первого числа списка nums и последнего числа, возведенного в квадрат

    Параметры:
        - nums (list): список.

    Сложность: O(1).
    """
    return (nums[0] + nums[-1] ** 2) #O(1)


# Задание task_03_02_07.
# Выполнил: Горынин Л.А.
# Группа: ЦИБ-241

def foo(low, high):
    """ Возвращает число, загаданное пользователем, используя двоичный поиск (делением диапазона каждый раз напополам)

    Параметры:
        - low (int): нижняя граница;
        - high (int): верхняя граница.

    Сложность: O(log n), так как каждый раз граница уменьшается вдвое, то нужно порйти только половину чисел, а не по всем.
    """
    guessing = True
    while guessing: # O(log n)
        guess = (low + high) // 2 # O(1)
        print("Загаданное число {0}?".format(guess)) # O(1)
        pointer = input( 
            "Введите '+', если Ваше число меньше.\n"
            "Введите '-' если Ваше число больше.\n"
            "Введите '=', если я угадал.\n").lower() # O(1)
        if pointer == "+": # O(1)
            high = guess # O(1)
        elif pointer == "-": # O(1)
            low = guess # O(1)
        elif pointer == "=": # O(1)
            guessing = False # O(1)
        else: # O(1)
            print("Введите '+', '-' или '='.") # O(1)

    return guess # O(1)


# # ЗАКОММЕНТИРУЙТЕ этот код перед запуском проверки
# low, high = 0, 100
# print("Пожалуйста, загадайте число от {0} до {1}!".format(low, high))
# guess = foo(low, high)
# print("Игра окончена, Вы загадали число: {0}.".format(guess))

#Общая сложность: O(log n)


# Задание task_03_02_08.
# Выполнил: Горынин Л.А.
# Группа: ЦИБ-241

import random
import time

def timeit(func, *args, **kw):
    """Выполнить функицю 'func' с параметрами '*args', '**kw' и
    вернуть время выполнения в мс."""

    time_start = time.time()
    res = func(*args, **kw)
    time_end = time.time()

    return (time_end - time_start) * 1000.0, res


def maxmin1(data):
    """Вернуть минимум и максимум из 'data'.

    Алгоритм:
        Последовательный перебор всего массива.

    Сложность: O(n).

    Параметры:
        - data (list of int): список целых чисел.

    Результат:
        tuple: мин. и макс. значения."""
    min_v = max_v = data[0]

    for num in data[1:]: # O(n)
        if num < min_v: # O(1)
            min_v = num # O(1)
        if num > max_v: # O(1)
            max_v = num # O(1)

    return (min_v, max_v) # O(1)


def maxmin2(data):
    """Вернуть минимум и максимум из 'data'.

    Алгоритм:
        Сортировка списка, и возврат первого и последнего элементов.

    Сложность: O(n log n) (если же использвать пузырьковую сортировку, а не встроенную функцию sorted, то будет O(n^2))

    Параметры:
        - data (list of int): список целых чисел.

    Результат:
        tuple: мин. и макс. значения."""

    sorted_data = sorted(data)  # O(n log n)
    return (sorted_data[0], sorted_data[-1]) 


def maxmin3(data):
    """Вернуть минимум и максимум из 'data'.

    Алгоритм:
        Используя встроенные функции min() и max().

    Сложность: O(n).

    Параметры:
        - data (list of int): список целых чисел.

    Результат:
        tuple: мин. и макс. значения."""

    min_v = min(data) # O(n)
    max_v = max(data) # O(n)
    return (min_v, max_v) # O(1)
    # сложности не перемножаются, будет O (n + n) = O(n)

if __name__ == "__main__":
    GEN_LIMIT = 1000000
    dataset = []
    for i in range(4, 7):
        dataset.append(random.sample(range(-GEN_LIMIT, GEN_LIMIT), 10**i))

    res = [["i", "1 способ (мс.)", "2 способ (мс.)", "3 способ (мс.)"]]
    for data in dataset:
        res.append([len(data),
                   timeit(maxmin1, data)[0],
                   timeit(maxmin2, data)[0],
                   timeit(maxmin3, data)[0]])

    # Вывод
    print("{:>15} {:>15} {:>15} {:>15}".format(*res[0]))
    for r in res[1:]:
        print("{:>15} {:>15.2f} {:>15.2f} {:>15.2f}".format(*r))


# Задание task_03_02_09.
# Выполнил: Горынин Л.А.
# Группа: ЦИБ-241

import random
import time


def timeit(func, *args, **kw):
    """Выполнить функицю 'func' с параметрами '*args', '**kw' и
    вернуть время выполнения в мс."""

    time_start = time.time()
    res = func(*args, **kw)
    time_end = time.time()

    return (time_end - time_start) * 1000.0, res


def is_ok_to_pass_1(db, passport_id):
    """Вернуть отметку о допуске из 'db' для паспорта с номером 'passport_id'.

    Если паспорт не найден в базе данных, возвращается отказ в допуске.

    Алгоритм:
        Последовательный перебор списка.

    Сложность: O(n).

    Параметры:
        - db (list of dict): база данных;
        - passport_id (str): номер паспорта.

    Результат:
        bool: отметка о допуске."""
    for record in db:
        if "passport_id" in record and record["passport_id"] == passport_id:
            if "allowed" in record:
                return record["allowed"]
            else:
                return False 
    return False


def is_ok_to_pass_2(db_opt, passport_id):
    """Вернуть отметку о допуске из 'db_opt' для паспорта с номером 'passport_id'.

    Если паспорт не найден в базе данных, возвращается отказ в допуске.

    Алгоритм:
        Обращение по ключу в словаре.

    Сложность: O(1).

    Параметры:
        - db_opt (dict): оптимизированная база данных для поиска;
        - passport_id (str): номер паспорта.

    Результат:
        bool: отметка о допуске."""
    return db_opt.get(passport_id, False)


def ok_str(flag):
    return "Да" if flag else "Нет"


if __name__ == "__main__":
    print("Загрузка базы данных... ")

    GEN_LIMIT = 1000000
    # База данных
    db = [{"id": "{:07d}".format(i), "ok": random.random() < 0.9}
          for i in random.sample(range(GEN_LIMIT, 10 * GEN_LIMIT), GEN_LIMIT)]

    # Структура db_opt должна быть оптимизированным хранилищем
    db_opt = {record["id"]: record["ok"] for record in db}


    print("Загружено записей: {:,}.\n\nПримеры:".format(GEN_LIMIT))
    print("Первый элемент:", db[0])
    print("Последний элемент:", db[-1])
    print("\n")

    passport_id = input("Введите номер паспорта (7 цифр): ").strip()

    output = """
                  1 способ   2 способ
    Допущен     {:>10s} {:>10s}
    Время (мс.) {:>10.2f} {:>10.2f}\
    """

    res1 = timeit(is_ok_to_pass_1, db, passport_id)
    res2 = timeit(is_ok_to_pass_2, db_opt, passport_id)

    print(output.format(ok_str(res1[1]),
                        ok_str(res2[1]),
                        res1[0],
                        res2[0]))


# Задание task_03_02_10.
# Выполнил: Горынин Л.А.
# Группа: ЦИБ-241

import random
import time


def timeit(func, *args, **kw):
    """Выполнить функицю 'func' с параметрами '*args', '**kw' и
    вернуть время выполнения в мс."""

    time_start = time.time()
    res = func(*args, **kw)
    time_end = time.time()

    return (time_end - time_start) * 1000.0, res


def top3_1(db):
    """Вернуть список из ТОП-3 клиентов по сумме активов.

    Алгоритм:
        Сортировка (встроенный метод sort()) и возврат 3-х элементов.

    Сложность: O(n log n).

    Параметры:
        - db (list of dict): список клиентов.

    Результат:
        tuple of dict: 3 клиента с максимальной суммой активов."""
    db.sort(key=lambda x: x['assets'], reverse=True)
    
    return tuple(db[:3])


def top3_2(db):
    """Вернуть список из ТОП-3 клиентов по сумме активов.

    Алгоритм:
        Прямой перебор (1 проход в цикле).

    Сложность: O(n).

    Параметры:
        - db (list of dict): список клиентов.

    Результат:
        tuple of dict: 3 клиента с максимальной суммой активов."""
    top_clients = []
    for client in db:
        if len(top_clients) < 3:
            top_clients.append(client)
        else:
            min_client = min(top_clients, key=lambda x: x['assets'])
            if client['assets'] > min_client['assets']:
                top_clients.remove(min_client)
                top_clients.append(client)

    return tuple(top_clients)


if __name__ == "__main__":
    print("Загрузка базы данных... ")

    GEN_LIMIT = 10000000
    # Список клиентов
    db = []
    for client_id, assets in enumerate(
      random.sample(range(0, 10 * GEN_LIMIT), GEN_LIMIT),
      start=1):
        db.append(dict(client_id=client_id, assets=assets))

    print("Загружено записей: {:,}.\n\nПримеры:".format(GEN_LIMIT))
    print("Первый элемент:", db[0])
    print("Последний элемент:", db[-1])
    print("\n")

    res1 = timeit(top3_1, db)
    res2 = timeit(top3_2, db)

    for i, (func_time, res) in enumerate((res1, res2), start=1):
        print("Способ №{}".format(i))
        print("Время: {:.2f} мс.".format(func_time))
        for j, client in enumerate(res, start=1):
            print("{}-е место: ID={client_id} Активы={assets:,} руб.".
                  format(j, **client))
        print()
