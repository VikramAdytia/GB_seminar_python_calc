path = 'log.txt'
def logger(value_a, value_b, operator, result):
    log = f'{value_a} {value_b} {operator} = {result}\n'
    with open(path, 'a') as data:
        data.write(log)

