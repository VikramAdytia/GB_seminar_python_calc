path = 'log.txt'


def logger(value_a, value_b, operator, result):
    log = f'{float (value_a)} {operator} {float (value_b)}  = {result}\n'  # log = f'{value_a} {operator} {value_b}  = {result}\n'
    with open(path, 'a') as data:
        data.write(log)


def writeLog(data, result):
    with open('log.csv', 'a+') as file:
            file.write('{};=;{}\n'.format(data, result))
