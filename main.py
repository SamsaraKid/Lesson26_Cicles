# n1 = 22
#
# def f1():
#     n1 = 0
#     print(n1)
#     pass
#
# def f2(x):
#     n3 = 11
#     n3 += 100
#     # global n1
#     x += 100
#     print(x)
#     pass
#
# f1()
# f2(n1)
#
# def f3():
#     r = 2 + 12
#     return r
#
# print(f3())


# n = 100
# for i in range (10):
#     n += 1
#     pass
#
# print('=====================================')
#
# n = 100
# while n < 120:
#     n += 3
#     print(n)


# циклы

# h = 10.0
# for i in range(10):
#     h += 2.5
# print('Высота башни %f метров' % h)
#
# h1 = 10.0
# d = 0
#
# while h1 < 150.0:
#     h1 += 2.5
#     print(h1)
#     d += 1
#
# print('Нужно %d дней' % d)

# массивы

# students = ['Иван', 'Пётр', 'Саша', 'Лёня', 'Ольга']
# print(len(students))
# for i in range (len(students)):
#     print(students[i])
# print('===========================')
# for s in students:
#     print(s)
# print('===========================')
# x = 0
# while x < len(students):
#     print(students[x])
#     x += 1
# print('===========================')
# k = 0
# while True:
#     print(students[k])
#     k += 1
#     if k == len(students):
#         break

# ani = ['кот', 'собака', 'слон', 'тигр', 'хомяк', 'мышь']
# for i in ani:
#     print(i, 'спит')


# случайные числа
import random
# print(random.randint(1,5))

# from random import randint
# n = randint(1,5)
#
# import random as r
# n = r.randint(1,5)

# n = 0
# while True:
#     n = random.randint(1,100)
#     print(n)
#     if n == 33:
#         break

# n = 0
# croc = 0
# while croc < 25:
#     n = random.randint(1,5)
#     croc += n
# print('Крокодил наелся, съел %d кусков' % croc)
#
# import mylib
#
# mylib.cat()
# mylib.text('hello')
# mylib.dice()


x = int(input('Введите число\n'))
odd = 0
even = 0
for i in range(x):
    n = random.randint(1, 100)
    print(n)
    if n % 2 == 0:
        odd += n
    else:
        even += n
print('Сумма чётных:', odd)
print('Сумма нечётных:', even)

