"""
Производим вычисление произведение всех чисел от 1 до введенного (вычисление факториала)
Название файла '03.for.py'

Version: 0.1
Author: Andrej Marinchenko
Date: 2023-03-04
"""

n = int(input('Введите число n = '))  # вводим значение до которого считаем произведение всех числе
result = 1  # начальный результат умножения берется за единицу
for x in range(1, n + 1):  # перебираем все числа от 1 до введенного Вами
    result *= x  # на каждом шагу умножаем результат на х
print('Факториал %d! = %d' % (n, result))  # выводим результат
