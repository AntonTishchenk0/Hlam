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
# Заданы две клетки шахматной доски. Напишите программу, которая определяет, имеют ли указанные клетки один цвет или нет. 
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
# Футбольная команда набирает девочек от 10 до 15 лет включительно. Напишите программу, которая запрашивает возраст и пол претендента, 
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
#задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки. 
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
# if max(n1, n2, n3) - min(n1, n2, n3) == n1 or max(n1, n2, n3) - min(n1, n2, n3) == n2 or max(n1, n2, n3) - min(n1, n2, n3) == n3:
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
