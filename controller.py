#!/usr/bin/env python3

from fractions import Fraction


import model 
import view 

def button_click():
    value_a = view.get_value() 
    operator = view.get_operator() 
    value_b = view.get_value()
    model.init(value_a, value_b, operator)
    result = model.do_it() 
    view.view_data(result)