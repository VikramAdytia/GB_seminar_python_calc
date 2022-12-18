#!/usr/bin/env python3

from fractions import Fraction


import model 
import view
import logger
import complexCalc


def button_click():
    menu = ["Запустить калькулятор для вещественных чисел", "Запустить калькулятор для комплексных чисел"]
    for i in range(len(menu)):
        print(f"{i + 1}. {menu[i]}")
    match  input("Введите пункт меню(без точки) и нажмите Enter: "):
        case '1':
            value_a = view.get_value()
            operator = view.get_operator()
            value_b = view.get_value()
            model.init(value_a, value_b, operator)
            result = model.do_it()
            view.view_data(result)
            logger.logger(value_a, value_b, operator, result)
        case '2':
            comp_num1_str = input('Введите первое комплексное число. Например, a+bi: ')
            comp_num2_str = input('Введите второе комплексное число. Например, с+di: ')
            comp_num1 = complexCalc.complex_input(comp_num1_str)
            comp_num2 = complexCalc.complex_input(comp_num2_str)
            operation = input('Введите желаюмую операцию (+,-,*,/): ')
            result = complexCalc.complex_operations(comp_num1, comp_num2, operation)
            user_input = comp_num1_str + operation + comp_num2_str
            logger.writeLog(user_input, result)
            view.view_result(user_input, result)
