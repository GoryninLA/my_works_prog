# Задание task_03_01_01.
# Выполнил: Горынин Л.А.
# Группа: ЦИБ-241

def sgn(x):
    """Вернуть результат сигнум-функции.

    Параметры:
        - x (float): аргумент x.

    Результат:
        float: значение функции.
    """
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0
    

x = int(input("Введите x: "))
y = int(input("Введите y: "))

z = round((sgn(x) + y ** 2) / (sgn(y) - (abs(x) ** 0.5)), 2)

print("Ответ:", z)


# Задание task_03_01_02.
# Выполнил: Горынин Л.А.
# Группа: ЦИБ-241

def avg(data):
    """Вернуть среднее значение 'data'.

    Параметры:
        - data (list): список чисел, включая None, который не будет учитываться.

    Результат:
        float: среднее значение.
    """
    cleaned_data = cleared_data(data)
    if cleaned_data:
        return sum(cleaned_data) / len(cleaned_data)
    return 0
    


def cleared_data(data):
    """Вернуть список без значений None.

    Параметры:
        - data (list): список данных со всеми возможными None.

    Результат:
        list: список без None.
    """
    return [value for value in data if value is not None]


n = int(input("Кол-во измерений: "))

# Если с клавиатуры вводится прочерк, измерения нет
# (необходимо добавить в список None)
data = []
for i in range(n):
    value = input(f"Измерение {i + 1}-е: ")
    if value == '-':
        data.append(None)
    else:
        data.append(float(value))


# Получить очищенный список и среднее значение
cleaned_data = cleared_data(data)  
average = avg(data)

print(f"Средняя температура: {round(average, 2)}")


# Задание task_03_01_03.
# Выполнил: Горынин Л.А.
# Группа: ЦИБ-241

def is_lucky(num):
    """Является ли 'num' номером счастливого билета?

    Параметры:
        - num (int): номер билета.

    Результат:
        bool: True - да, False - нет.
    """
    num_str = str(num)
    even = 0
    odd = 0
    for digit in num_str:
        if int(digit) % 2 == 0:
            even += 1
        else:
            odd += 1
    return even == odd

def lucky_numbers(a, b):
    """Вернуть список счастливых номеров от 'a' до 'b'.

    Параметры:
        - a (int): номер 1-го билета.
        - b (int): номер 2-го билета.

    Результат:
        list: список счастливых номеров билетов.
    """
    lucky = []
    for num in range(a, b + 1):
        if is_lucky(num):
            lucky.append(num)
    return lucky



a = int(input("Первый номер билета: "))
b = int(input("Последний номер билета: "))

# Вывод должен быть осуществлен в строку с одним пробелом-разделителем
lucky_list = lucky_numbers(a, b)
print(" ".join(map(str, lucky_list)))


# Задание task_03_01_04.
# Выполнил: Горынин Л.А.
# Группа: ЦИБ-241

def is_leap(year):
    """Является ли 'year' високосным годом?

    Параметры:
        - year (int): год.

    Результат:
        bool: True - да, False - нет.
    """
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False


def days(month, year):
    """Вернуть количество дней в месяце 'month' года 'year'.

    Параметры:
        - year (int): год.
        - month (int): месяц (1-12).

    Результат:
        int: количество дней в месяце.
    """
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year):
        days_in_month[1] = 29
    return days_in_month[month - 1]


def previous_date(day, month, year):
    """Вернуть день, месяц, год предыдущего дня.

    Параметры:
        - year (int): год.
        - month (int): месяц.
        - day (int): день.

    Результат:
        (int, int, int): день, месяц, год предыдущего дня.
    """
    if day == 1:
        if month == 1:
            return 31, 12, year - 1
        else:
            previous_month = month - 1
            previous_day = days(previous_month, year)
            return previous_day, previous_month, year
    else:
        return day - 1, month, year


def next_date(day, month, year):
    """Вернуть день, месяц, год следующего дня.

    Параметры:
        - day (int): день.
        - month (int): месяц.
        - year (int): год.

    Результат:
        (int, int, int): день, месяц, год следующего дня.
    """
    if day == days(month, year):
        if month == 12:
            return 1, 1, year + 1
        else:
            return 1, month + 1, year
    else:
        return day + 1, month, year


day, month, year = map(int, input("День, месяц, год через пробел: ").split())

prev_day, prev_month, prev_year = previous_date(day, month, year)
next_day, next_month, next_year = next_date(day, month, year)

print(f"Предыдущий день: {prev_day:02d}/{prev_month:02d}/{prev_year}")
print(f"Следующий день: {next_day:02d}/{next_month:02d}/{next_year}")


# Задание task_03_01_05.
# Выполнил: Горынин Л.А.
# Группа: ЦИБ-241

def is_leap(year):
    """Является ли 'year' високосным годом?

    Параметры:
        - year (int): год.

    Результат:
        bool: True - да, False - нет.
    """
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False


def days(month, year):
    """Вернуть количество дней в месяце 'month' года 'year'.

    Параметры:
        - year (int): год.
        - month (int): месяц (1-12).

    Результат:
        int: количество дней в месяце.
    """
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year):
        days_in_month[1] = 29
    return days_in_month[month - 1]


def another_date(day, month, year, delta=1):
    """Вернуть день, месяц, год, отличающийся на 'delta' дней.

    Параметры:
        - day (int): день.
        - month (int): месяц.
        - year (int): год.
        - delta (int): сдвиг в днях (положительные для следующих, отрицательные для предыдущих)

    Результат:
        (int, int, int): день, месяц, год иной даты.
    """
    while delta != 0:
        if delta > 0:
            if day == days(month, year):
                day = 1
                if month == 12:
                    month = 1
                    year += 1
                else:
                    month += 1
            else:
                day += 1
            delta -= 1
        else:
            if day == 1:
                if month == 1:
                    month = 12
                    year -= 1
                else:
                    month -= 1
                day = days(month, year)
            else:
                day -= 1
            delta += 1
    
    return day, month, year


day, month, year = map(int, input("День, месяц, год через пробел: ").split())
delta = int(input("Свдиг (может быть отрицательным): "))

new_day, new_month, new_year = another_date(day, month, year, delta)
print(f"Новый день: {new_day:02d}/{new_month:02d}/{new_year}")


# Задание task_03_01_06.
# Выполнил: Горынин Л.А.
# Группа: ЦИБ-241

def gcd(first, second):
    """Вернуть НОД целых чисел 'first' и 'second'."""
    while second:
        first, second = second, first % second
    return first 
        

def lcm(first, second):
    """Вернуть НОК целых чисел 'first' и 'second'."""
    return abs(first * second) // gcd(first, second)

def gcd_nums(nums):
    """Вернуть НОД чисел из списка 'nums'.

    Параметры:
        - nums (list): список чисел.

    Результат:
        int: НОД списка чисел из списка 'nums'.
    """
    result = nums[0]
    for num in nums[1:]:
        result = gcd(result, num)
    return result

def lcm_nums(nums):
    """Вернуть НОК чисел из списка 'nums'.

    Параметры:
        - nums (list): список чисел.

    Результат:
        int: НОК списка чисел из списка 'nums'.
    """
    result = nums[0]
    for num in nums[1:]:
        result = lcm(result, num)
    return result

nums = list(map(int, input("Введите числа через пробел: ").split()))

print(f"НОД = {gcd_nums(nums)}")
print(f"НОК = {lcm_nums(nums)}")


# Задание task_03_01_07.
# Выполнил: Горынин Л.А.
# Группа: ЦИБ-241

def has_digits(sentence):
    """Вернуть предложение, которое имеет цифру/цифры."""
    if any(char.isdigit() for char in sentence): 
        return sentence
    return None 


def sentences_with_digits_count(sentences):
    """Вернуть количество предложений с цифрой."""
    count = 0
    for sentence in sentences:
        if has_digits(sentence):  
            count += 1
    return count


n = int(input("Введите количество предложений:"))
sentences = []
for i in range(1, n + 1):
    print(f"Введите предложение №{i}:")
    sentence = input()
    sentences.append(sentence)

print(f"Предложений с цифрой = {sentences_with_digits_count(sentences)}")


# Задание task_03_01_08.
# Выполнил: Горынин Л.А.
# Группа: ЦИБ-241

def print_with_border(string, char):
    """Вернуть текст с рамкой"""
    border = char * (len(string) + 2)
    framed = f"{char}{string}{char}"
    return f"{border}\n{framed}\n{border}"


string = input("Введите строку: ")
char = input("Введите символ: ")
result = print_with_border(string, char)
print(result)


# Задание task_03_01_09.
# Выполнил: Горынин Л.А.
# Группа: ЦИБ-241

LETTERS_EX = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
DIGITS_EX = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}


def to_base(number, base):
    """Преобразовать десятичное число 'number' в с.с. 'base'.

    Параметры:
        number (int): десятичное число;
        base (int): система счисления.

    Результат:
        str: число в с.с. 'base'."""
    if number == 0:
        return "0"
    
    digits = []
    is_negative = False
    
    if number < 0:
        is_negative = True
        number = abs(number)
    
    while number > 0:
        remainder = number % base
        if remainder >= 10:
            digits.append(LETTERS_EX[remainder])
        else:
            digits.append(str(remainder))
        number = number // base
    
    if is_negative:
        digits.append('-')
    
    return ''.join(reversed(digits))


def from_base(number, base):
    """Преобразовать число 'number' из с.с. 'base' в десятичное.

    Параметры:
        number (str): число в исходной системе счисления;
        base (int): система счисления исходного числа.

    Результат:
        int: число в 10-й с.с."""
    number = str(number).upper()
    is_negative = False
    
    if number.startswith('-'):
        is_negative = True
        number = number[1:]
    
    decimal_value = 0
    for i, digit in enumerate(reversed(number)):
        if digit.isalpha():
            value = DIGITS_EX[digit]
        else:
            value = int(digit)
        
        if value >= base:
            raise ValueError(f"Invalid digit {digit} for base {base}")
        
        decimal_value += value * (base ** i)
    
    return -decimal_value if is_negative else decimal_value


# Задание task_03_01_10.
# Выполнил: Горынин Л.А.
# Группа: ЦИБ-241

def sentence_stats(sentence):
    """Вернуть символьную статистику 'sentence'. Регистр не учитывается.

    Параметры:
        - sentence (str): введенное предложение.

    Результат:
        dict: словарь, в котором ключами являются буквы, а значениями количество этих букв в 'sentence'
    """
    stats = {}
    for char in sentence.lower():
        if char in stats:
            stats[char] += 1
        else:
            stats[char] = 1
    return stats


sentence = input("Введите предложение: ")
print(f"{sentence_stats(sentence)}")


# Задание task_03_01_11.
# Выполнил: Горынин Л.А.
# Группа: ЦИБ-241

def ceasar(text, shift):
    """Вернуть измененную строку 'text' со сдвигом 'shift'.

    Параметры:
        - text (str): строка;
        - shift (int): свдиг.

    Результат:
        str: измененная строка."""
    # Набор кириллических букв
    letters = [chr(i) for i in range(ord('а'), ord('я') + 1)]
    upper_letters = [char.upper() for char in letters]
    result = []
    
    for char in text:
        if char in letters:
            index = letters.index(char)
            new_index = (index + shift) % 33
            result.append(letters[new_index])
        elif char in upper_letters:
            index = upper_letters.index(char)
            new_index = (index + shift) % 33
            result.append(upper_letters[new_index])
        else:
            result.append(char)
    return ''.join(result)
    


text = input("Введите предложение: ")
shift = int(input("Введите сдвиг: "))

encoded = ceasar(text, shift)
decoded = ceasar(encoded, -shift) 

print("Зашифрованная строка:", encoded)
print("Расшифрованная строка:", decoded)


# Задание task_03_01_12.
# Выполнил: Горынин Л.А.
# Группа: ЦИБ-241

# В данной задаче ввод с клавиатуры не нужен.
# Используйте пример данных ниже, при необходимости измените его для
# проверки правильности решения

data = [
    {1: 'м', 2: 'м', 3: 'м', 4: 'ж'},
    {1: 'ж', 2: 'м', 3: 'ж', 4: 'ж'},
    {1: 'ж', 2: 'ж', 3: 'ж', 4: 'ж'},
    {1: 'м', 2: 'м', 3: 'м', 4: 'м'},
    {1: None, 2: None, 3: None, 4: None},
    {1: 'м', 2: None, 3: None, 4: 'ж'},
    {1: None, 2: None, 3: None, 4: None},
    {1: 'м', 2: 'м', 3: None, 4: 'м'},
    {1: 'ж', 2: None, 3: None, 4: 'ж'}
]


def vacant_compartments(data):
    """Вернуть список полностью свободных купе. Нумерация купе идет с 1.

    Параметры:
        - data (list of dict): данные о занятости мест в вагоне.

    Результат:
        list of int."""
    result = []
    for i, compartment in enumerate(data, 1):
        if all(seat is None for seat in compartment.values()):
            result.append(i)
    return result


def vacant_seats(data, compartments_condition=None, seat_condition=None):
    """Вернуть список свободных мест при соблюдении условий
    'compartments_condition' и 'seat_condition'.
    Нумерация купе и мест идет с 1.

    Параметры:
        - data (list of dict): данные о занятости мест в вагоне;
        - compartments_condition (function):
          функция c 1 параметром (словарь - купе), возвращающая True/False;
        - seat_condition (function):
          функция c 2 параметрами (номер места, значение),
          возвращающая True/False.

    Результат:
        list of tuple: список кортежей вида (номер купе, номер места)."""
    result = []
    for compartment_num, compartment in enumerate(data, 1):
        # Проверяем условие для купе, если оно задано
        if compartments_condition is None or compartments_condition(compartment):
            for seat_num, value in compartment.items():
                # Место свободно и удовлетворяет условию места
                if value is None and (seat_condition is None or seat_condition(seat_num, value)):
                    result.append((compartment_num, seat_num))
    return result


def is_same_sex_and_vacant(compartment, sex):
    """Вернуть True, если в купе 'compartment' есть свободные места,
    а остальные пассажиры только пола 'sex'.

    Параметры:
        - compartment (dict): данные о купе;
        - sex (str): пол ("м" или "ж").

    Результат:
        bool."""
    has_vacant = any(seat is None for seat in compartment.values())
    if not has_vacant:
        return False
    
    for passenger_sex in compartment.values():
        if passenger_sex is not None and passenger_sex != sex:
            return False
    return True


# Список полностью свободных купе
print("Полностью свободные купе:", vacant_compartments(data))

# Список всех свободных мест в вагоне
print("Все свободные места:", vacant_seats(data))

# Список свободных нижних мест (нечетные номера)
print("Свободные нижние места:", vacant_seats(data, seat_condition=lambda seat, _: seat % 2 != 0))

# Список свободных верхних мест (четные номера)
print("Свободные верхние места:", vacant_seats(data, seat_condition=lambda seat, _: seat % 2 == 0))

# Список свободных мест в купе с исключительно мужской компанией
print("Свободные места в мужских купе:", vacant_seats(data, lambda x: is_same_sex_and_vacant(x, "м")))

# Список свободных мест в купе с исключительно женской компанией
print("Свободные места в женских купе:", vacant_seats(data, lambda x: is_same_sex_and_vacant(x, "ж")))


# Задание task_03_01_13.
# Выполнил: Горынин Л.А.
# Группа: ЦИБ-241

# В данной задаче ввод с клавиатуры не нужен.
# Используйте значения 'votes', при необходимости измените его для
# проверки правильности решения

votes = [
    2, 3, -1, 2, 5, 1, 1, 4, 1, 1, 1, 3, 1, 3, 5, -1, 5, 2, 5, 5,
    3, 3, 2, 3, 3, 2, 2, 1, 3, 2, 5, 2, 2, 4, 1, 1, 3, 2, 2, 3, 3,
    3, 1, 4, 2, 1, 4, 2, 3, 3, 3, -1, 5, 3, 1, 4, 5, 1, 1, 3, 3,
    3, -1, 5, 3, 3, 2, 5, 1, 1, 5, -1, 1, 2, 2, 3, -1, 4, 2, 5, 4,
    2, -1, 3, 1, 4, 3, 5, 4, 1, 5, 3, 2, 4, 2, 1, 3, 4, 1, 1, 3, 4
]

parties = {
    1: "Партия №1", 2: "Партия №2", 3: "Партия №3",
    4: "Партия №4", 5: "Партия №5", -1: "Испорчено"
}


def parties_votes(parties, votes):
    """Вернуть информацию о голосах 'votes', отданных за партии 'parties'.
    Испорченные бланки также присутствуют в результате.

    Параметры:
        - parties (dict): информация о партиях (номер голоса: название);
        - votes (list): номера голосов.

    Результат:
        dict: название: кол-во отданных голосов."""
    results = {party_name: 0 for party_name in parties.values()}
    for vote in votes:
        if vote in parties:
            party_name = parties[vote]
            results[party_name] += 1
    return results


def print_results(votes_for_p):
    """Вывести результаты голосования в формате:

    1. Партия №2 | 1111 | 58.21%
    2. Партия №4 |  999 | 38.14%

    Параметры:
        - votes_for_p (dict): результат функции parties_votes().
    """
    total_votes = sum(votes_for_p.values()) 
    sorted_parties = sorted(votes_for_p.items(), key=lambda item: item[1], reverse=True)
    
    for i, (party, count) in enumerate(sorted_parties, 1):
        percentage = (count / (total_votes)) * 100
        print(f"{i}. {party} | {count:4d} | {percentage:5.2f}%")

votes_result = parties_votes(parties, votes)
print_results(votes_result)


# Задание task_03_01_14.
# Выполнил: Горынин Л.А.
# Группа: ЦИБ-241

def split_numbers(*nums):
    """Вернуть кортеж из 2 списков - отрицательных и неотицательных значений.

    Параметры:
        - nums(str): строка чисел

    Результат:
        tuple: (list: отрицательные значения, list: неотицательные значения )."""
    negative_numbers = []
    positive_numbers = []
    
    for num in nums:
        if num < 0:
            negative_numbers.append(num)
        else:
            positive_numbers.append(num)
    
    return (sorted(negative_numbers), sorted(positive_numbers))

print(split_numbers(1, 4, -5, 0, -33))


# Задание task_03_01_15.
# Выполнил: Горынин Л.А.
# Группа: ЦИБ-241

def gdp(c, i, g, ex, im):
    """Вернуть значение ВВП.

    Параметры:
        - c(int): конечное потребление;
        - i(int): валовое накопление капитала;
        - g(int): государственные расходы;
        - ex(int): экспорт;
        - im(int): импорт.

    Результат:
        int: значение ВВП.
    """
    Y = c + i + g + ex - im
    return Y


info_dict = {}
info_list = [info_dict]
c = int(input("Конечное потребление: "))
i = int(input("Валовое накопление капитала: "))
g = int(input("Государственные расходы: "))
ex = int(input("Экспорт: "))
im = int(input("Импорт: "))
info_dict["c"] = c
info_dict["i"] = i
info_dict["g"] = g
info_dict["ex"] = ex
info_dict["im"] = im

results = gdp(c, i, g, ex, im)
print(f"ВВП = {results}")


# Задание task_03_01_16.
# Выполнил: Горынин Л.А.
# Группа: ЦИБ-241

def pow1(value, power):
    """Вернуть 'value' в степени 'power'.

    Параметры:
        - value(int): число, которое необходимо возвести в степень "power";
        - rower(int): степень, в которую будут возводить число "value".

    Результат:
        int: 'value' в степени 'power'."""
    return value ** power


def pow2(value, power):
    """Вернуть 'value' в степени 'power'. Рекурсивный алгоритм.

    Параметры:
        - value(int): число, которое необходимо возвести в степень "power";
        - rower(int): степень, в которую будут возводить число "value".

    Результат:
        int: 'value' в степени 'power'."""
    if power == 0:
        return 1
    elif power < 0:
        return 1 / pow2(value, -power)
    else:
        return value * pow2(value, power - 1)


print(pow1(5, 3))
print(pow2(5, 3))


# Задание task_03_01_17.
# Выполнил: Горынин Л.А.
# Группа: ЦИБ-241

def digits_sum(value):
    """Вернуть сумму цифр числа 'value'. Рекурсивная реализация.

    Параметры:
        - value(int): число.

    Результат:
        int: сумма цифр числа 'value'.
    """
    if value == 0:
        return 0
    else:
        return value % 10 + digits_sum(value // 10)  


def digits_count(value):
    """Вернуть количество цифр числа 'value'. Рекурсивная реализация.

    Параметры:
        - value(int): число.

    Результат:
        int: количество цифр числа 'value'.
    """
    value = abs(value)
    if  value < 10:
        return 1
    else:
        return 1 + digits_count(value // 10)


print(digits_sum(12345))
print(digits_count(12345))