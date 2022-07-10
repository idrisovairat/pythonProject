from itertools import count, cycle

for i in count(int(input('введите стартовое число:'))):
    print(i, end='')
    quit = input()
    if quit == 'q':
        break

u_list = input('ввдеите список, разделяя элементы пробелом').split()
iter_ = cycle(u_list)
quit = None

while quit != 'q':
    print(next(iter_), end='')
    quit = input()