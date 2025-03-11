# Задание task_02_01.
# Выполнил: Горынин Л.А.
# Группа: ЦИБ-241


x = float(input("Введите чсило x: "))

if x >= 0:
    f = x ** (1/2) + x ** 2   
else:
    f = 1 / x

print(f"f = {round(f, 2)}")


# Задание task_02_02.
# Выполнил: Горынин Л.А.
# Группа: ЦИБ-241
# E-mail: goruninl@bk.ru


a1 = int(input("Введите первое число: "))
a2 = int(input("Введите второе число: "))

if a1 > a2:
    print(f"Максимум: {a1}, минимум: {a2}")
elif a1 < a1:
    print(f"Максимум: {a2}, минимум: {a1}")
else:
    print(f"Максимум: {a1}, минимум: {a1}")
 

# Задание task_02_03.
# Выполнил: Горынин Л.А.
# Группа: ЦИБ-241

a = int(input("Ширина форточки: "))
b = int(input("Высота форточки: "))
d = int(input("Диаметр головы: "))

if a != 0 and b != 0 and d != 0:
    fix = 1
    hypotenuse = ((a - 2 * fix) ** 2 + (b - 2 * fix) ** 2) ** (1 / 2)
    if hypotenuse >= d:
        print("Да, голова пролезет")
    else:
        print("Нет, голова слишком большая")
else:
    print("Проверьте ваш код")


# Задание task_02_04.
# Выполнил: Горынин Л.А.
# Группа: ЦИБ-241


year_today = int(input("Введите текущий год: "))
month_today = int(input("Введите текущий месяц: "))

year = int(input("Введите год рождения: "))
month = int(input("Введите месяц рождения: "))

age = year_today - year
if month_today < month:
    age -= 1

print("Число полных лет: ", age)


# Задание task_02_05.
# Выполнил: Горынин Л.А.
# Группа: ЦИБ-241


x = int(input("Введите координату x: "))
y = int(input("Введите координату y: "))

if x == 0 and y == 0:
    print("Начало координат")
elif x == 0 or y == 0:
    print("Находится на пересечении четвертей")
else:
    if x > 0 and y > 0:
        print("1-я четверть")
    elif x < 0 and y > 0:
        print("2-я четверть")
    elif x < 0 and y < 0:
        print("3-я четверть")
    else:
        print("4-я четверть")


# Задание task_02_06.
# Выполнил: Горынин Л.А.
# Группа: ЦИБ-241


a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

if a == 0:
    print("Это линейное уравнение")
else:
    D = b ** 2 - 4 * a * c
    if D > 0:
        x1 = round((-b + D ** (1/2)) / (2 * a), 1)
        x2 = round((-b - D ** (1/2)) / (2 * a), 1)
        print(f"x1 = {x1}, x2 = {x2}")
    elif D == 0:
        x = -b / (2 * a)
        print(f"x = {x}")
    else:
        print("Нет корней")


# Задание task_02_07.
# Выполнил: Горынин Л.А.
# Группа: ЦИБ-241

nums_sum = 0  # сумма
nums_count = 0  # количество

x = int(input("Введите 1-e число: "))  
while x != 0:  
    nums_sum += x  
    nums_count += 1  
    x = int(input(f"Введите {nums_count + 1}-е число: "))  

print("Сумма:", nums_sum) 
print("Количество чисел:", nums_count)


# Задание task_02_08.
# Выполнил: Горынин Л.А.
# Группа: ЦИБ-241


n = float(input("n = "))
start = 0 
while n >= start:
    print(start)
    start += 5


# Задание task_02_09.
# Выполнил: Горынин Л.А.
# Группа: ЦИБ-241


a = float(input("a = "))
n = 1 
x_sum = 1
while x_sum <= a:
    n += 1
    x_sum += 1 / n
print(f"n = {n}")


# Задание task_02_10.
# Выполнил: Горынин Л.А.
# Группа: ЦИБ-241
# E-mail: goryninl@bk.ru


n = int(input("n = "))
n_sum = 0
n_count = 0
while n > 0:
    n_sum += n % 10  
    n_count += 1  
    n //= 10  
# Выводим результаты
print(f"Сумма = {n_sum}")
print(f"Количество = {n_count}")


# Задание task_02_11.
# Выполнил: Горынин Л.А.
# Группа: ЦИБ-241


start = int(input("start = "))
k = int(input("k = "))
s = int(input("s = "))
n_count = []
for num in range(start, start + 1000000):
    if num % 10 == k and num % s == 0:
        n_count.append(num)
    if len(n_count) == 10:
        break
print(" ".join(map(str, n_count)))


# Задание task_02_12.
# Выполнил: Горынин Л.А.
# Группа: ЦИБ-241

a = int(input("a = "))
b = int(input("b = "))

if b > a: 
    for x in range(a, b + 1):
        print(x, end=' ')
    print()
    for i in range(b, a - 1, -1):
        print(i)
elif a > b:
    for x in range(b, a + 1):
        print(x, end=' ')
    print()
    for i in range(a, b - 1, -1):
        print(i)
else:
    print("a и b - равны")


# Задание task_02_13.
# Выполнил: Горынин Л.А.
# Группа: ЦИБ-241
# E-mail: goryninl@bk.ru


a = int(input("a = "))
b = int(input("b = "))

numbers = range(a, b + 1)
n_sum = sum(numbers)
n_mult = 1
start = 0 
for num in range(a, b + 1):
    n_mult *= num
    start += num
n_avg = round(start / len(range(a, b + 1)), 2)
def geom(numbers):
    count = 0
    product = 1
    for number in numbers:
        if number % 2 != 0:
            product *= number
            count += 1
    return product ** (1 / count)
n_avg_geom = round(geom(numbers), 2)

print("Сумма =", n_sum)
print("Произведение =", n_mult)
print("Среднее арифметическое = {}".format(n_avg))
print("Среднее геометрическое нечетных чисел = {}".format(n_avg_geom))


# Задание task_02_14.
# Выполнил: Горынин Л.А.
# Группа: ЦИБ-241


s = int(input("Пробег за 1-й день (км.) = "))
p = int(input("Насколько увеличивает пробег (%) = "))

total = s
count = 1

while count < 10:
    s = s * (1 + (p / 100))
    count += 1
    total += s
    print(f"Пробег за {count}-й день: {round(s, 1)} ")


print("Суммарный пробег: {:.1f} км.".format(total))


# Задание task_02_15.
# Выполнил: Горынин.Л.А.
# Группа: ЦИБ-241


p = int(input("Грузоподъемность грузовика (кг.) = "))
n = int(input("Количество предметов = "))

total = 0
count = 0
while p >= total:
    total += 3
    count += 1
    print(f"Масса {count}-го предмета (кг.) = 3")
    if count == n:
        break 
if total <= p:
    print("Да")
else:
    print("Нет")


# Задание task_02_16.
# Выполнил: Горынин.Л.А.
# Группа: ЦИБ-241


n = int(input("Количество районов = "))

count = 1
total = 0
while count <= n:
    s = float(input(f"Площадь {count}-го райога (га.) = "))
    yield_s = float(input(f"Урожайность в {count}-м районе (ц/га.) = "))
    count += 1
    product = s * yield_s
    total += product

print(f"Собрано пщеницы: {round(total, 1)} ц.")


# Задание task_02_17.
# Выполнил: Горынин.Л.А.
# Группа: ЦИБ-241


nums_sum = 0  # сумма
nums_count = 0  # количество

x = int(input("Введите 1-e число: "))  
while True:  
    nums_sum += x  
    nums_count += 1  
    x = int(input(f"Введите {nums_count + 1}-е число: ")) 
    if x == 0:
        break

print("Сумма:", nums_sum) 
print("Количество чисел:", nums_count)


# Задание task_02_18.
# Выполнил: Горынин.Л.А.
# Группа: ЦИБ-241



sentence = str(input("Введите предложение: "))
lower_sent = sentence.lower()
count_gl = 0  # Кол-во гласных
count_sogl = 0  # Кол-во согласных
char_list = list(lower_sent)
gl = ["а", "е", "ё", "и", "о", "у", "ы", "э", "я", "ю"]

for char in char_list:
    if char == " ":
        continue
    if char in gl:
        count_gl += 1
    else:
        count_sogl += 1

print(f"Количество букв в предложении: гласных - {count_gl}, согласных - {count_sogl}")


# Задание task_02_19.
# Выполнил: Горынин.Л.А.
# Группа: ЦИБ-241


a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

for num in range(a, b + 1):
    if num % c == 0:
        print(num, end=" ")


# Задание task_02_20.
# Выполнил: Горынин.Л.А.
# Группа: ЦИБ-241


n = int(input("n = "))

for num in range(100, 1000):
    nums = [int(digit) for digit in str(num)]
    total = sum(nums)
    if total == n:
        print(num, end=" ")


# Задание task_02_21.
# Выполнил: Горынин.Л.А.
# Группа: ЦИБ-241


n = int(input("n = "))

girls = []
boys = []
count = 1

while count <= n:
    hight = int(input(f"Рост {count}-го ученика = "))
    count += 1
    if hight > 0:
        girls.append(hight)
    elif hight < 0:
        boys.append(hight)
    else:
        continue

if len(boys) != 0 and len(girls) != 0:
    r_sr_m = round(float(abs(sum(boys) / len(boys))), 1)
    r_sr_d = round(float(sum(girls) / len(girls)), 1)
elif len(boys) == 0 and len(girls) != 0:
    r_sr_m = 0.0
    r_sr_d = round(float(sum(girls) / len(girls)), 1)
elif len(boys) != 0 and len(girls) == 0:
    r_sr_d = 0.0
    r_sr_m = round(float(abs(sum(boys) / len(boys))), 1)
else:
    r_sr_m = 0.0
    r_sr_d = 0.0

print("Средний рост мальчиков: {:.1f}".format(r_sr_m))
print("Средний рост девочек: {:.1f}".format(r_sr_d))


# Задание task_02_22.
# Выполнил: Горынин Л.А.
# Группа: ЦИБ-241
# E-mail: goryninl@bk.ru


n = float(input("n = "))
count = 1
nums = []
a_max = None
a_min = None

while count <= n:
    num = float(input(f"{count}-е число = "))
    count += 1
    nums.append(num)

a_max = max(nums)
a_min = min(nums)

print("Максимум: {:.2f}".format(a_max))
print("Минимум: {:.2f}".format(a_min))


# Задание task_02_23.
# Выполнил: Горынин Л.А.
# Группа: ЦИБ-241


n = int(input("n = "))

def is_fibonacci(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return b == n

print("Является" if is_fibonacci(n) else "Не является")


# Задание task_02_24.
# Выполнил: Горынин Л.А.
# Группа: ЦИБ-241


n = int(input("n = "))
count = 1
nums = []
while count <= n :
    num = float(input(f"{count}-е число = "))
    nums.append(num)
    count += 1

for i in range(1, n):
    if nums[i] <= nums[i - 1]:
        print(i + 1)
        break
else:
    print("Является")


# Задание task_02_25.
# Выполнил: Горынин Л.А.
# Группа: ЦИБ-241

n = int(input("n = "))
width = 2

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(f"{i} + {j} = {i * j:>{width}}", end='  ')
    print()


# Задание task_02_26.
# Выполнил: Горынин Л.А.
# Группа: ЦИБ-241

n = int(input("n = "))

for i in range(1, n + 1):
    count = 0
    for j in range(1, i + 1):
        if i % j == 0:
            count += 1
    print(f"{i} " + '*' * count)


# Задание task_02_27.
# Выполнил: Горынин Л.А.
# Группа: ЦИБ-241

n = int(input("n = "))

prime_numbers = []
num = 2

while len(prime_numbers) < n:
    prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0: 
            prime = False
            break
    if prime:
        prime_numbers.append(num)
    num += 1

print(" ".join(map(str, prime_numbers)))


# Задание task_02_28.
# Выполнил: Горынин Л.А.
# Группа: ЦИБ-241

k = int(input("k = "))
width = 2

for x in range(1, 31):
    for y in range(1, 31):
        for z in range(1, 31):
            if x ** 2 + y ** 2 + z ** 2 == k ** 2:
                print(f"x = {x:>{width}}, y = {y:>{width}}, z = {z:>{width}}")


# Задание task_02_29.
# Выполнил: Горынин Л.А.
# Группа: ЦИБ-241

n = int(input("n = "))

nums = []
while len(nums) < n:
    num = int(input(f"Введите {len(nums)}-й элемент списка:"))
    nums.append(num)

print(f"Исходный список: {nums}")

nums_pos = [p for p in nums if p > 0]
nums_neg = []
for x in nums:
    if x < 0:
        nums_neg.append(x)

sr_ar = round(sum(nums_pos) / len(nums_pos), 2)
start = 1
for c in nums_neg:
    start *= c
sr_geom = round(abs(start) ** (1 / len(nums_neg)),2)

print(f"Положительные числа: {nums_pos}")
print(f"Отрицательные числа: {nums_neg}")
print(f"Ср. фрифм.: {sr_ar}")
print(f"Ср. геом.: {sr_geom}")


# Задание task_02_30.
# Выполнил: Горынин Л.А.
# Группа: ЦИБ-241

# Все разделенные пробелом элементы будут преобразованы в список целых чисел
nums = [int(item) for item in input().split()]

# 1. Все положительные
for item in nums:
    if item <= 0:
        all_pos_1 = False
        break
else:
    all_pos_1 = True

all_pos_2 = all([item > 0 for item in nums])

# 2. Хотя бы 1 нулевой элемент
for item in nums:
    if item == 0:
        any_zero_1 = True
        break
else:
    any_zero_1 = False

any_zero_2 = any([item == 0 for item in nums])

# 3. Все четные
for items in nums:
    if item % 2 == 0:
        all_even_1 = True
else:
    all_even_1 = False 

all_even_2 = all([item % 2 == 0 for item in nums])
# 4. Хотя бы 1 нечетный элемент
for item in nums:
    if item % 2 != 0:
        any_odd_1 = True
        break
else:
    any_odd_1 = False 

any_odd_2 = any([item % 2 != 0 for item in nums])
print("Все положительные:", all_pos_1, all_pos_2)
print("Хотя бы 1 нулевой элемент:", any_zero_1, any_zero_2)
print("Все четные:", all_even_1, all_even_2)
print("Хотя бы 1 нечетный элемент:", any_odd_1, any_odd_2)


# Задание task_02_31.
# Выполнил: Горынин Л.А.
# Группа: ЦИБ-241

s = str(input("Введите предложение = "))
k = str(input("Введите букву = "))
words = s.split()
filtered = []
for word in words:
    if k.lower() not in word.lower():
        filtered.append(word)

print(" ".join(filtered))


# Задание task_02_32.
# Выполнил: Горынин Л.А.
# Группа: ЦИБ-241

n = int(input("Количество рядов = "))

# 1. Заполнение мест
seats = []
for i in range(n):
    row = list(map(int, input().split()))
    seats.append(row)

# 2. Всего свободных мест
count = 0
for row in seats:
        count += row.count(0)

print(f"Всего свободных мест: {count}")
# 3. Ввод значений для поиска
#    Учитывайте, что пользователь привык считать с 1, а не с 0,
#    поэтому введенные сообщения необходимо скорректировать
n_p, m_p = [int(item) for item in
            input("Введите ряд и место через пробел: ").split()]


# n_p, m, p не должны выходить за границы
# Если выходит, необходимо указать, что "Такого места не существует"
if n_p < 1 or n_p > len(seats):
    print("Неверный номер ряда.")
else:
    if m_p < 1 or m_p > len(seats[n_p - 1]):
        print("Неверный номер места.")
    else:
        is_free = seats[n_p - 1][m_p - 1] == 0
        print(f"Место свободно: {is_free}")


# Задание task_02_33.
# Выполнил: Горынин Л.А.
# Группа: ЦИБ-241

# 1. Заполнение списка
n = int(input("Количество сотрудников = "))

employees = []
for _ in range(n):
    entry = input('')
    surname, name, surname2, gender, experience = entry.split()
    int_exp = int(experience)
    employees.append([surname, name, surname2, gender, int_exp])

# 2. Cамый «молодой» и самый «старый» сотрудник

youngest_employee = min(employees, key=lambda x: x[4])
oldest_employee = max(employees, key=lambda x: x[4])
print(f'Самый "молодой": {youngest_employee[0]} {youngest_employee[1]} {youngest_employee[2]}')
print(f'Самый "старый": {oldest_employee[0]} {oldest_employee[1]} {oldest_employee[2]}')

# # 3. Отдельные списки мужчин и женщин
men = [emp for emp in employees if emp[3]== 'М']
women = [emp for emp in employees if emp[3]== 'Ж']

k = input('Введите букву начала имени = ').lower()

men_k_count = sum(1 for emp in men if emp[1].lower().startswith(k))

women_k_count = sum(1 for emp in women if emp[1].lower().startswith(k))
if men_k_count > women_k_count:
  print('У мужчин таких имен больше')
elif men_k_count < women_k_count:
    print('У женщин таких имен больше')
else:
    print('Таких имен поровну у мужчин и женщин')
print("")


# Задание task_02_34.
# Выполнил: Горынин Л.А.
# Группа: ЦИБ-241

# 1. Заполнение списка
n = int(input(("Количество банков = ")))

deposits = []
for i in range(n):
  l = input()
  name, initial_sum, rate = l.split()
  deposits.append({
        "name": name,
        "initial_sum": int(initial_sum),
        "rate": float(rate)
    })

# 2. Самый доступный банк (с наименьшей первоначальной суммой)

banр = min(deposits, key=lambda bank: bank["initial_sum"])

# 3. Самый выгодный банк
#    прибыль = сумма * процент / 100

for bank in deposits:
    bank["profit"] = bank["initial_sum"] * bank["rate"] / 100

profitable_bank = max(deposits, key=lambda bank: bank["profit"])


print(f"Самый доступный банк: {banр['name']}, первоначальная сумма: {banр['initial_sum']:.2f} руб.")
print(f"Самый выгодный банк: {profitable_bank['name']}, прибыль: {profitable_bank['profit']:.2f} руб.")