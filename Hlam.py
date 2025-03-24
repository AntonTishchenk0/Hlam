# Task 1:

# color1 = input("Введите первый цвет для смешивания: ")
# color2 = input("Введите второй цвет для смешивания: ")
# if color1 == color2 in ("красный", "синий", "желтый"):
#     print(color1)
# elif (color1 == "красный" or color1 == "синий") and (color2 == "синий" or color2 == "красный"):
#     print("фиолетовый")
# elif (color1 == "красный" or color1 == "желтый") and (color2 == "желтый" or color2 == "красный"):
#     print("оранжевый")
# elif (color1 == "синий" or color1 == "желтый") and (color2 == "желтый" or color2 == "синий"):
#     print("зеленый")
# else:
#     print('ошибка цвета')

# Task 2:
# a = int(input("Введице число от 0 до 36: "))
# if a == 0:
#     print('зеленый')
# elif (1 <= a <= 10 and a % 2 == 0) or (11 <= a <= 18 and a % 2 != 0):
#     print('черный')
# elif (1 <= a <= 10 and a % 2 != 0) or (11 <= a <= 18 and a % 2 == 0):
#     print('красный')
# elif (19 <= a <= 28 and a % 2 == 0) or (29 <= a <= 36 and a % 2 != 0):
#     print("черный")
# elif (19 <= a <= 28 and a % 2 != 0) or (29 <= a <= 36 and a % 2 == 0):
#     print('красный')
# else:
#     print('ошибка ввода')

# Task 3:
# a1 = int(input("введите число а1: "))
# b1 = int(input("введите число b1: "))
# a2 = int(input("введите число a2: "))
# b2 = int(input("введите число b2: "))
# if b1 < a2 or b2 < a1:
#     print('пустое множество')
# else:
#     if a1 > a2:
#         a2 = a1
#     if b1 > b2:
#         b1 = b2
#     if a2 == b1:
#         print(a2)
#     else:
#         print(a2, b1)

# Task 4:
# Напишите программу, которая определяет, оканчивается ли год с данным номером на два нуля. 
# Если год оканчивается, то выведите «YES», иначе выведите «NO».

# a = int(input())
# a1 = a % 10
# b = a % 100 / 10
# if a1 == 0 and b == 0:
#     print('YES')
# else:
#     print('NO')

# Task 5:
# Заданы две клетки шахматной доски. Напишите программу, которая определяет,
# имеют ли указанные клетки один цвет или нет.
# Если они покрашены в один цвет, то выведите слово «YES», а если в разные цвета, то «NO».

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# if (a % 2 != 0 and b % 2 != 0) and (c % 2 == 0 and d % 2 == 0): 
#     print('YES')
# elif (a % 2 == 0 and b % 2 == 0) and (c % 2 != 0 and d % 2 != 0):
#     print('YES')
# elif (a + b) % 2 == 0 and (c + d) % 2 == 0:
#     print('YES')
# elif (a + b) % 2 != 0 and (c + d) % 2 != 0:
#     print("YES")
# else:
#     print('NO')

# Task 6:
# Футбольная команда набирает девочек от 10 до 15 лет включительно.
# Напишите программу, которая запрашивает возраст и пол претендента,
# используя обозначение пола буквы m (от male – мужчина) и f (от female – женщина) 
# и определяет подходит ли претендент для вступления в команду или нет. Если претендент подходит, 
# то выведите «YES», иначе выведите «NO».

# a = int(input())
# b = input()
# if 10 <= a <= 15 and b == "f":
#     print("YES")
# else:
#     print('NO')

# Task 7:
# Напишите программу, которая считывает целое число и выводит соответствующую ему римскую цифру. 
# Если число находится вне диапазона 1−10, то программа должна вывести текст «ошибка».

# a = int(input())
# if a == 1:
#     print('I')
# elif a == 2:
#     print('II')
# elif a == 3:
#     print('III')
# elif a == 4:
#     print('IV')
# elif a == 5:
#     print('V')
# elif a == 6:
#     print('VI')
# elif a == 7:
#     print('VII')
# elif a == 8:
#     print('VIII')
# elif a == 9:
#     print('IX')
# elif a == 10:
#     print('X')
# else:
#     print("ошибка")

# or

# n, roman_numbers = int(input()), ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X']
# print(roman_numbers[n-1] if 1 <= n <= 10 else 'ошибка')

# Task 8:
# Напишите программу, которая принимает на вход число и в зависимости от условий выводит текст «YES», либо «NO».
# если число нечётное, то вывести «YES»;
# если число чётное в диапазоне от 2 до 5 (включительно), то вывести «NO»;
# если число чётное в диапазоне от 6 до 20 (включительно), то вывести «YES»;
# если число чётное и больше 20, то вывести «NO».

# a = int(input())
# if a % 2 != 0:
#     print("YES")
# elif a % 2 == 0 and 2 <= a <= 5:
#     print('NO')
# elif a % 2 == 0 and 6 <= a <= 20:
#     print('YES')
# elif a > 20 and a % 2 == 0:
#     print("NO")

# Task 9:
# Даны две различные клетки шахматной доски. Напишите программу, которая определяет, может ли слон 
# попасть с первой клетки на вторую одним ходом. Программа получает на вход четыре числа от 1 до 8 каждое, 
# задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки.
# Программа должна вывести «YES», если из первой клетки ходом слона можно попасть во вторую или «NO» в противном случае.

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# if (a - b) == (c - d) or (a + b) == (c + d):
#     print("YES")
# else:
#     print('NO')

# Task 10:
# Даны две различные клетки шахматной доски. Напишите программу,  которая определяет, может ли конь 
# попасть с первой клетки на вторую одним ходом. Программа получает на вход четыре числа от 1 до 8 каждое, 
# задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки. 
# Программа должна вывести «YES», если из первой клетки ходом коня можно попасть во вторую или «NO» в противном случае.

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# if (a + b + c + d) % 2 != 0 and a != c and b != d:
#     print('YES')
# else:
#     print("NO")

# Task 11:
# Даны две различные клетки шахматной доски. Напишите программу,  которая определяет, может ли ферзь 
# попасть с первой клетки на вторую одним ходом. Программа получает на вход четыре числа от 1 до 8 каждое, 
# задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки. 
# Программа должна вывести «YES», если из первой клетки ходом ферзя можно попасть во вторую или «NO» в противном случае.

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# if (a == c or b == d) or ((a - b) == (c - d) or (a + b) == (c + d)):
#     print('YES')
# else:
#     print("NO")


# for i in range(5):
#     print(i, end= "! ")
# print()

# print(*range(5), sep="! ", end= "! ")
# print()

# for i in range(5):
#     print(i, sep="! ")

# Task 12:
# Назовем число интересным, если в нем разность максимальной и 
# минимальной цифры равняется средней по величине цифре. Напишите программу, которая определяет, 
# интересное число или нет. Если число интересное, следует вывести «Число интересное», 
# иначе - «Число неинтересное».

# n = int(input())
# n1 = n // 100
# n2 = n // 10 % 10
# n3 = n % 10
# if max(n1, n2, n3) - min(n1, n2, n3) == n1 or max(n1, n2, n3) - min(n1, n2, n3) == n2
# or max(n1, n2, n3) - min(n1, n2, n3) == n3:
#     print('Число интересное')
# else:
#     print('Число неинтересное')

# Task 13:
# Рекурсионный метод возведения в степень.

# def f(a, b):
#     res = a ** b
#     return res

# a, b = int(input('Input a number: ')), int(input('Input a number: '))
# print(f(a, b))

# Task 14: 
# Сложение чисел через рекурсию, не используя сложения.

# def sum(a, b):
#     if a == 0:
#         return b
#     return sum(a - 1, b + 1)

# a = int(input("Введите число a: "))
# b = int(input("Введите число b: "))

# print(sum(a, b))

# Task 15:
# На вход программе подается три натуральных числа 
# m: стартовое количество организмов;
# p: среднесуточное увеличение в %;
# n: количество дней для размножения.
# Напишите программу, которая предсказывает размер популяции организмов. 
# Программа должна выводить размер популяции в каждый день, начиная с 1 и заканчивая n-м днем.

# m = int(input())
# p = int(input())
# n = int(input())
# for i in range(n):
#     print(i + 1, m)
#     m += m * p / 100


# total = 0
# for i in range(1, 6):
#     total += i
#     print(total, end=" ")

# Task 16:
# Задача про ведьмака и монеты

# n = int(input())
# count = 0
# while n >= 25:
#     count += 1
#     n = n - 25
# while 10 <= n < 25:
#     count += 1
#     n = n -10
# while 5 <= n < 10:
#     count += 1
#     n = n - 5
# while 1 <= n < 5:
#     count += 1
#     n = n - 1
# print(count) 

# Task 17:
# for i in range(10):
#     print(i, end='*')
#     if i > 6:
#         break

# Task 18:
# i = 100
# while i > 0:
#     if i == 40:
#         break
#     print(i, end='*')
#     i -= 20

# Task 19:
# result = 0
# for i in range(10):
#     if i % 2 == 0:
#         continue
#     result += i
# print(result)

# Task 20:
# mult = 1
# for i in range(1, 11):
#    if i % 2 == 0:
#       continue
#    if i % 9 == 0:
#       break
#    mult *= i
# print(mult)

# n = int(input())
# for i in range(1, n):
#     print(i)

# Task 21:
# На обработку поступает последовательность из 10 целых чисел (каждое на отдельной строке). 
# Нужно написать программу, которая выводит на экран количество неотрицательных чисел 
# последовательности и их произведение. Если неотрицательных чисел нет, требуется вывести на экран «NO». 
# Программист торопился и написал программу неправильно.
# Найдите все ошибки в этой программе (их ровно 4). 
# Известно, что каждая ошибка затрагивает только одну строку 
# и может быть исправлена без изменения других строк.

# count = 0
# p = 1
# for i in range(1, 11):
#     x = int(input())
#     if x >= 0:
#         p = p * x
#         count = count + 1
# if count > 0:
#     print(count)
#     print(p)
# else:
#     print('NO')

# Task 22:
# На обработку поступает натуральное число. Нужно написать программу, 
# которая выводит на экран максимальную цифру числа, кратную 3. Если в числе нет цифр, кратных 3, 
# требуется на экран вывести «NO». Программист торопился и написал программу неправильно.

# n = int(input())
# max_digit = -1
# while n > 0:
#     last_digit = n % 10
#     if last_digit > max_digit and last_digit % 3 == 0:
#         max_digit = last_digit    
#     n = n // 10
# if max_digit == -1:
#     print('NO')
# else:
#     print(max_digit)

# Task 23:
# На обработку поступает натуральное число. Нужно написать программу, 
# которая выводит на экран его первую (старшую) цифру. 
# Программист торопился и написал программу неправильно.

# n = int(input())
# while n > 9:
#     n //= 10
# print(n)

# Task 24:
# На обработку поступает натуральное число. Нужно написать программу, 
# которая выводит на экран произведение цифр введенного числа. 
# Программист торопился и написал программу неправильно.

# n = int(input())
# product = 1
# while n > 0:
#     digit = n % 10
#     product *= digit
#     n //= 10
# print(product)

# mini Task*
# a = 2
# b = 3
# print(a + b)

# Task 25:

# Решите уравнение в натуральных числах  28n+30k+31m=365.

# for n in range(1, 14):
#     for k in range(1, 13):
#         for m in range(1, 12):
#             if 28 * n + 30 * k + 31 * m == 365:
#                 print('n =', n, 'k =', k, 'm =', m)

# Task 26:  

# Имеется 100 рублей. Сколько быков, коров и телят можно купить на все эти деньги, 
# если плата за быка – 10 рублей, за корову – 5 рублей, за теленка – 0.5 рубля 
# и надо купить 100 голов скота?

# 10b + 5k + 0.5t = 100

# for b in range(1, 11):
#     for k in range(1, 21):
#         for t in range(1, 201):
#             if 10 * b + 5 * k + 0.5 * t == 100:
#                 if b + k + t == 100:
#                     print('b =', b, 'k =', k, 't =', t)

# Task 27:

# n = int(input())
# for i in range(1, n + 1):
#     if i == 1 or i == n:
#         print('*' * 19)
#     else:
#         print('*' + ' ' * 17 + '*')

# Task 28:
# n = int(input())
# while n > 999: 
#     n //= 10
# print(n % 10)

# Task 29:

# n = input()
# for i in range(-1, -len(n) - 1, -1):
#     print(n[i], sep='')  

# Task 30:
# n = int(input())
# my_list = list('abcdefghijklmnopqrstuvwxyz')
# my_lst = []
# for i in range(n):
#     my_lst += my_list[i]
# print(my_lst)

# Task 31

# languages = ['Chinese', 'Spanish', 'English', 'Hindi',
# 'Arabic', 'Bengali', 'Portuguese', 'Russian', 'Japanese', 'Lahnda']
# print(languages[-1::-1])

# Task 32

# numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]
# sp = []
# for i in range(len(numbers)):
#     sp.append(numbers[i]*numbers[i])
# print(sum(sp))

# Task 33

# n = int(input())
# sp = []
# for _ in range(n):
#     x = int(input())
#     sp.append(x)
# sp1 = []
# for i in range(len(sp)):
#     sp1.append(sp[i] * sp[i] + 2 * sp[i] + 1)     
# print(*sp, sep='\n')
# print()
# print(*sp1, sep='\n')

# Task 34

# sp = []
# for i in range(int(input())):
#     sp.append(i)
# print(sp)

# Task 35


# def set_plus(a, b):
#     res = a + b
#     return res
#
#
# def set_multi(a, b):
#     res = a * b
#     return res
#
#
# x = set_plus(5, 6)
# s = set_multi(5, 10)
# print(x)
# print(s)

# Task 36
#
#
# def func_decorator(func):
#     def wrapper(x, *args, **kwargs):
#         dx = 0.0001
#         res = (func(x + dx, *args, **kwargs) - func(x, *args, **kwargs)) / dx
#         return res
#
#     return wrapper
#
#
# def sin_df(x):
#     return math.sin(x)
#
#
# df = sin_df(math.pi / 3)
# print(df)

# Task 37

# def fact(num):
#     sp = []
#     for i in range(1, num + 1):
#         if num % i == 0:
#             sp.append(i)
#     return sp
#
#
# print(fact(5))

# Task 38

# def find_all(target, symbol):
#     n = 0
#     sp = []
#     for i in target:
#         if i == symbol:
#             sp.append(n)
#         n += 1
#     return sp
#
#
# s = 'abcdabcaaa'
# char = 'a'
# print(find_all(s, char))

# Task 39

# def merge(list1, list2):
#     res = list1 + list2
#     res.sort()
#     return res
#
#
# # считываем данные
# numbers1 = [int(c) for c in input().split()]
# numbers2 = [int(c) for c in input().split()]
#
# # вызываем функцию
# print(merge(numbers1, numbers2))

# Task 40

# def quick_merge(lst1, lst2):
#     result = []
#     p1, p2 = 0, 0
#     while p1 < len(lst1) and p2 < len(lst2):
#         if lst1[p1] < lst2[p2]:
#             result.append(lst1[p1])
#             p1 += 1
#         else:
#             result.append(lst2[p2])
#             p2 += 1
#     if p1 == len(lst1):
#         result += lst2[p2:]
#     else:
#         result += lst1[p1:]
#     return result
#
#
# res = []
# for _ in range(int(input())):
#     num = [int(c) for c in input().split()]
#     res = quick_merge(res, num)
# print(*res)

# Task 41

# sec = 1000000
# secInMin = 60
# secInHours = secInMin * 60
# secInDay = secInHours * 24
#
# days = sec / secInDay
# hours = (sec % secInDay) / secInHours
# minutes = ((sec % secInDay) % secInHours) / secInMin
# sInD = int(days) * secInDay
# sInH = int(hours) * secInHours
# sInM = int(minutes) * secInMin
# seconds = sec - sInD - sInH - sInM
#
# m = sec / 60
# h = m / 60
# d = h / 24
#
# print(int(m), int(h), int(d))
# print(secInMin, secInHours, secInDay)
# print(int(days), int(hours), int(minutes), int(seconds))

# Task 42
# def draw_triangle():
#     for i in range(8):
#         print(' ' * (8 - 1 - i) + '*' * (1 + i * 2))
#
#
# draw_triangle()

# Task 43

# def get_shipping_cost(quantity):
#     sum = 1000
#     res = sum + 120 * (quantity - 1)
#     return res
#
#
# n = int(input())
#
# print(get_shipping_cost(n))

# Task 44

# import random

# for i in range(10):
#     print(random.random())
# num = random.random()
# print(num)

# num = random.uniform(10, 17)
# print(num)

# random.seed(17)   # явно устанавливаем начальное значение для генератора случайных чисел

# for _ in range(10):
#     print(random.randint(1, 100))

# COINS = [500, 200, 100, 50, 10, 5, 1]  # 5р, 2р, 1р, 50к, 10к, 5к, 1к
# COIN_NAMES = {
#     500: "5 рублей",
#     200: "2 рубля",
#     100: "1 рубль",
#     50: "50 копеек",
#     10: "10 копеек",
#     5: "5 копеек",
#     1: "1 копейка"
# }
#
# print("Введите сумму сдачи в копейках:")
# amount = int(input("> "))
#
# result = {}
# for coin in COINS:
#     if amount >= coin:
#         count = amount // coin
#         result[coin] = count
#         amount -= count * coin
#
# print("Необходимые монеты:")
# for coin, count in result.items():
#     if count > 0:
#         print(f"- {count} x {COIN_NAMES[coin]}")


# from random import randrange
# MIN_NUM = 1
# MAX_NUM = 49
# NUM_NUMS = 6
#
# ticket_nums = []
#
# for i in range(NUM_NUMS):
#     rand = randrange(MIN_NUM, MAX_NUM + 1)
#     while rand in ticket_nums:
#         rand = randrange(MIN_NUM, MAX_NUM + 1)
#     ticket_nums.append(rand)
#
# ticket_nums.sort()
# print('Номер вашего билета: ', end="")
# for n in ticket_nums:
#     print(n, end=' ')

# from random import randrange
# min_num = 1
# max_num = 49
# num_nums = 6
#
# ticket_nums = set()
# while len(ticket_nums) < num_nums:
#     ticket_nums.add(randrange(min_num, max_num + 1))
#
# ticket_nums = sorted(ticket_nums)
#
# print('Номер вашего билет: ', end="")
# for n in ticket_nums:
#     print(n, end=' ')

# list_1 = []
# word = input("Введите ваше первое слово: ")
# list_1.append(word)
# for i in list_1:
#     if word == 'End the program':
#         list_1.pop()
#         print(list_1)
#         break
#     else:
#         word = input('Введите ваше следующее слово: ')
#         print('Для завершения ввода введите "End the program": ')
#         list_1.append(word)
#
# list_1 = set(list_1)
# print(list_1)

# lst = []
# while lst != '':
#     print('Для завершения введите: "End the program"')
#     word = input('Введите ваше первое слово: ')
#     if word != 'End the program':
#         lst.append(word)
#     else:
#         lst.sort()
#         print('Программа завершена!')
#         break
# lst = set(lst)
# for i in lst:
#     print(i)

# lst = []
# while lst != '':
#     print('Для завершения введите: "End the program"')
#     word = input('Введите ваше первое слово: ')
#     if word not in lst:
#         lst.append(word)
#         if word == 'End the program':
#             lst.pop()
#             break
#
# [print(i) for i in lst]


# lst = []
# sm = 0
# count = 0
# while True:
#     numb = input('Введите ваше число: ')
#     if numb != '':
#         lst.append(numb)
#     else:
#         break
# for i in lst:
#     sm += int(i)
#     count += 1
# avg = sm / count
#
# print(sm, count, avg)


# numbers = []
# while True:
#     s = input("Введите число или пустую строку для завершения: ")
#     if s == "":
#         break
#     numbers.append(float(s))
#
# if not numbers:
#     print("Не введено ни одного числа.")
#     exit()
#
# average = sum(numbers) / len(numbers)
# below = [x for x in numbers if x < average]
# equal = [x for x in numbers if x == average]
# above = [x for x in numbers if x > average]
#
# print(f"Среднее значение: {average:.2f}")
#
# print("Числа ниже среднего:")
# print(', '.join(map(str, below)) if below else "Нет чисел")
#
# if equal:
#     print("Числа равные среднему:")
#     print(', '.join(map(str, equal)))
#
# print("Числа выше среднего:")
# print(', '.join(map(str, above)) if above else "Нет чисел")

# coord = input("Введите координаты клетки: ").strip().lower()
#
# # Разделение на букву и цифру
# letter = coord[0]
# number = int(coord[1])
#
# # Преобразование буквы в число (1-8)
# letter_num = ord(letter) - ord('a') + 1
#
# # Цвет первой клетки столбца (вертикаль 1)
# first_sum = letter_num + 1
# if first_sum % 2 == 0:
#     first_color = "черная"
# else:
#     first_color = "белая"
#
# # Определение цвета текущей клетки
# if number % 2 == 1:  # Нечетная вертикаль
#     current_color = first_color
# else:  # Четная вертикаль
#     current_color = "белая" if first_color == "черная" else "черная"
#
# print(f"Клетка {coord} – {current_color}")

# scrabble = {1: "A, E, I, L, N, O, R, S, T, U", 2: "D, G",
#             3: "B, C, M, P", 4: "F, H, V, W, Y", 5: "K",
#             8: "J, X", 10: "Q, Z"}
# word = str(input("Введите ваше слово: ").upper())
# count = 0
# for char in word:
#     for key in scrabble:
#         if char in list(scrabble[key]):
#             count += key
# print(count)

# lst = []
# while True:  # Бесконечный цикл до прерывания
#     print('Для завершения введите пустую строку! ')
#     word = input('Введите ваше первое слово: ').lower()
#
#     if word == '':
#         break  # Выход из цикла при вводе "End the program"
#
#     if word not in lst:
#         lst.append(word)  # Добавляем слово, если его нет в списке
#
# # Выводим список уникальных слов
# print("\nВведенные слова:")
# for word in lst:
#     print(word)

# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         print('Fizz-Buzz!', end='\n')
#     elif i % 3 == 0:
#         print('Fizz!', end='\n')
#     elif i % 5 == 0:
#         print('Buzz!', end='\n')
#     else:
#         print(i, end='\n')

# n = int(input("Введите число n: "))
#
# if n < 2:
#     print("Нет простых чисел.")
# else:
#     # Инициализация списка
#     primes = list(range(n + 1))
#     primes[0], primes[1] = 0, 0  # 0 и 1 не простые
#
#     # Алгоритм решета Эратосфена
#     for i in range(2, int(n**0.5) + 1):
#         if primes[i] != 0:
#             # Обнуляем все кратные i, начиная с i^2
#             for j in range(i * i, n + 1, i):
#                 primes[j] = 0
#
#     # Вывод всех чисел от 2 до n с заменой непростых на 0
#     print(f"Числа от 2 до {n} (непростые заменены на 0):")
#     for number in primes[2:]:
#         print(number)


# def sieve_of_eratosthenes(n):
#     if n < 2:
#         return []
#
#     primes = list(range(n + 1))  # Создаем список от 0 до n
#     primes[0], primes[1] = 0, 0  # 0 и 1 не являются простыми
#
#     for i in range(2, int(n ** 0.5) + 1):
#         if primes[i] != 0:
#             # Вычеркиваем все кратные i, начиная с i^2
#             for j in range(i * i, n + 1, i):
#                 primes[j] = 0
#
#     # Фильтруем ненулевые элементы (кроме 0 и 1)
#     result = [x for x in primes if x != 0]
#     return result
#
#
# # Ввод пользователя
# n = int(input("Введите число n: "))
# primes = sieve_of_eratosthenes(n)
# print(f"Простые числа до {n}:")
# print(primes)

# year = float(input('Введите возраст для перевода: '))
# x = 10.5
# y = 4
# if year <= 21:
#     life = year / x
# else:
#     life = 2 + (year - 21) / 4
# print('Собачий возраст равен %.1f' % life)

# n = int(input("Введите число n: "))
#
# if n < 2:
#     print("Нет простых чисел.")
# else:
#     primes = list(range(n + 1))
#     primes[0], primes[1] = 0, 0
#     for i in range(2, int(n**0.5) + 1):
#         if primes[i] != 0:
#             for j in range(i * i, n + 1, i):
#                 primes[j] = 0
#
#     print(f"Простые числа от 2 до {n}:")
#     for number in primes[2:]:  # Начинаем с индекса 2 (число 2)
#         if number != 0:
#             print(number)

# human_age = float(input("Введите человеческий возраст: "))
#
# if human_age <= 21:
#     dog_age = human_age / 10.5
# else:
#     dog_age = 2 + (human_age - 21) / 4
#
# print(f"Собачий возраст: {dog_age:.1f}")

# Task
# Условие. Представьте, что в вашем регионе устаревшим является формат номерных автомобильных знаков из трех (букв,
# следом) за которыми идут три цифры. Когда все номера такого шаблона закончились, было решено обновить формат,
# поставив в начало четыре цифры, а за ними три буквы. Напишите функцию, которая будет генерировать случайный номерной
# знак. При этом номера в старом и новом форматах должны создаваться примерно с одинаковой вероятностью. В основной
# программе нужно сгенерировать и вывести на экран случайный номерной знак.

# from random import randint
#
#
# def new_car_number():
#     result = ''
#     for i in range(4):
#         random_number = chr(randint(48, 57))
#         result += random_number
#     for i in range(3):
#         random_number = chr((randint(65, 90)))
#         result += random_number
#
#     return result
#
#
# def main():
#     plate = new_car_number()
#     print(f'Ваши случайные номера (Нового образца!): {plate}')
#     print(f'Ваши случайные номера (Старого образца!) {plate[4::] + plate[1:4]}')
#
#
# if __name__ == '__main__':
#     main()

# Task
# Условие. Напишите две функции с именами hex2int и int2hex для конвертации значений из шестнадцатеричной
# системы счисления (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E и F) в десятичную (по основанию 10) и обратно.
# Функция hex2int должна принимать на вход строку с единственным символом в шестнадцатеричной системе и
# преобразовывать его в число от нуля до 15 в десятичной системе, тогда как функция int2hex будет выполнять
# обратное действие – принимать десятичное число из диапазона от 0 до 15 и возвращать шестнадцатеричный эквивалент.
# Обе функции должны принимать единственный параметр со входным значением и возвращать преобразованное число.
# Удостоверьтесь, что функция hex2int корректно обрабатывает буквы в верхнем и нижнем регистрах. Если введенное
# пользователем значение выходит за допустимые границы, вы должны вывести сообщение об ошибке.


# def hex2int(symbol):
#     hex_digits = '0123456789ABCDEF'
#     symbol = symbol.upper()
#     if len(symbol) != 1 or symbol in hex_digits:
#         return hex_digits.index(symbol)
#
#
# def int2hex(numb):
#     hex_digits = '0123456789ABCDEF'
#     if 0 <= numb <= 15:
#         return hex_digits[numb]
#     else:
#         return 'Ошибка! Число должно быть в диапазоне от 0 до 15'
#
#
# def main():
#     try:
#         print(hex2int(input("Введите символ 0 - 9 или A - F: ")))
#     except ValueError:
#         print('Ошибка: Недопустимый символ для шестнадцатеричной системы')
#         print(hex2int(input("Введите символ 0 - 9 или A - F: ")))
#
#     try:
#         print(int2hex((int(input("Введите число от 0 до 15: ")))))
#     except TypeError:
#         print('Ошибка! Число должно быть в диапазоне от 0 до 15')
#         print(int2hex(int(input("Введите число от 0 до 15: "))))
#
#
# if __name__ == '__main__':
#     main()

# Task
# Условие. Это творческая задача. Представьте, что вы проектируете беспилотный автомобиль. Вам необходимо продумать,
# какими свойствами он обладает и какие действия совершает. Создайте класс беспилотный автомобиль и сохраните его
# в виде программного модуля. Импортируете класс и инициализируйте новый объект.

# class SelfDrivingCar:
#     def __init__(self, brand: str, model: str, current_location: str):
#         self.brand = brand
#         self.model = model
#         self.current_location = current_location
#         self.current_speed = 0.0
#         self.battery_level = 100.0  # Проценты
#         self.route = None
#         self.is_on = False
#         self.safety_system_active = True
#
#     def start(self):
#         if self.battery_level <= 5.0:
#             print("Ошибка: Заряд батареи слишком низкий для запуска.")
#             return
#         self.is_on = True
#         print(f"{self.brand} {self.model} запущен. Текущее местоположение: {self.current_location}")
#
#     def stop(self):
#         self.is_on = False
#         self.current_speed = 0.0
#         print(f"{self.brand} {self.model} остановлен.")
#
#     def accelerate(self, speed: float):
#         if not self.is_on:
#             print("Автомобиль не запущен.")
#             return
#         max_speed = 120.0  # Км/ч
#         new_speed = self.current_speed + speed
#         if new_speed > max_speed:
#             self.current_speed = max_speed
#             print(f"Достигнута максимальная скорость {max_speed} км/ч")
#         else:
#             self.current_speed = new_speed
#             print(f"Скорость увеличена до {self.current_speed} км/ч")
#
#     def decelerate(self, speed: float):
#         if not self.is_on:
#             print("Автомобиль не запущен.")
#             return
#         new_speed = self.current_speed - speed
#         if new_speed < 0:
#             self.current_speed = 0.0
#             print("Автомобиль полностью остановлен")
#         else:
#             self.current_speed = new_speed
#             print(f"Скорость снижена до {self.current_speed} км/ч")
#
#     def set_route(self, destination: str):
#         self.route = destination
#         print(f"Назначен маршрут: {self.current_location} → {destination}")
#
#     def navigate(self):
#         if not self.route:
#             print("Маршрут не установлен")
#             return
#         print(f"Начинаю движение к {self.route}...")
#         # Здесь можно добавить логику навигации
#
#     def check_obstacles(self):
#         # Пример обнаружения препятствий (можно расширить сенсорной логикой)
#         obstacles = ["Car", "Pedestrian"]  # Пример виртуальных препятствий
#         if obstacles:
#             print(f"Обнаружены препятствия: {', '.join(obstacles)}. Запускаю экстренное торможение...")
#             self.decelerate(self.current_speed)  # Полная остановка
#         else:
#             print("Путь свободен")
#
#     def charge(self, percentage: float):
#         if self.is_on:
#             print("Не могу заряжаться при работающем автомобиле")
#             return
#         self.battery_level = min(self.battery_level + percentage, 100.0)
#         print(f"Заряд батареи: {self.battery_level}%")
#
#     def get_status(self):
#         status = (
#             f"Статус {self.brand} {self.model}:\n"
#             f"Маршрут: {self.route or 'Не задан'}\n"
#             f"Текущая скорость: {self.current_speed} км/ч\n"
#             f"Заряд батареи: {self.battery_level}%\n"
#             f"Включён: {'Да' if self.is_on else 'Нет'}\n"
#         )
#         print(status)
#
#
# # Создание экземпляра автомобиля
# tesla = SelfDrivingCar("Tesla", "Model X", "Санкт-Петербург")
#
# # Запуск автомобиля
# tesla.start()
#
# # Установка маршрута
# tesla.set_route("Москва")
#
# # Ускорение
# tesla.accelerate(80)
#
# # Проверка препятствий
# tesla.check_obstacles()
#
# # Навигация
# tesla.navigate()
#
# # Снижение скорости
# tesla.decelerate(30)
#
# # Проверка состояния
# tesla.get_status()
#
# # Зарядка
# tesla.stop()
# tesla.charge(20)
#
# # Попытка запустить при низком заряде
# low_battery_car = SelfDrivingCar("Tesla", "Model Y", "Новосибирск")
# low_battery_car.battery_level = 3.0
# low_battery_car.start()
