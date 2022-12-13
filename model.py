from fractions import Fraction
 

x = Fraction(0)
y = Fraction(0)
op = ''

def init(a, b, operator):
    global x
    global y 
    global op
    x = a 
    y = b 
    op = operator 

def do_it(): 
    match op:
        case '+': return x + y 
        case '*': return x * y 
        case '-': return x - y 
        case '/': return x / y 

