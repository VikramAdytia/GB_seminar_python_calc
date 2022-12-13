#!/usr/bin/env python3

from fractions import Fraction
from math import *
import re 

# x = Fraction(input('Введите первое число. Для десятичного используйте ".", для дробного "/": \n'))
# oper = input('Введите символ операции +, -, *, или / :\n ')
# y = Fraction(input('Введите второе число. Для десятичного используйте ".", для дробного "/": \n'))


# def check_num():
#     while True:
#         a = input('Введите число. Для десятичного используйте ".", для дробного "/": \n')
#         if re.match(r'(-?\d+([./]\d+)?$)', a):
#             return Fraction(a)
#         else:
#             print('Некорректный ввод.')   

# print(check_num())

def check_symb():
    while True:
        c = input('Введите символ операции +, -, * или / :\n ')
        if re.match(r'[-+*\/]$', c):
            return c
        else:
            print('Некорректный ввод.')   

print(check_symb())


 
# Проверка корректности ввода знака 
# Определение операции 

# print(x+y)  

#def operation()

# def input_num():
#     while True:
#         num = int(input('Введите число от 1 до 28 включительно: ')) 
#         if 1 <= num <=28: 
#             return num  
#         else: 
#             print('Некорректное число!')
 
