from fractions import Fraction
import re 


def view_data(data):
    print(f'Результат {data} или {float(data)}') 


def get_value():
    while True:
        a = input('Введите число. Для десятичного используйте ".", для дробного "/": \n')
        if re.match(r'(-?\d+([./]\d+)?$)', a):
            return Fraction(a)
        else:
            print('Некорректный ввод.')   


def get_operator():
    while True:
        b = input('Введите символ операции +, -, * или / \n ')
        if re.match(r'[-+*\/]$', b):
            return b
        else:
            print('Некорректный ввод.')   
