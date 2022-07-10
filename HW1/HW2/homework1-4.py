spring = input('ввдеите словосочетание или слово через пробел:').split()
for i, word in enumerate(spring, 1):
    print(f'{i}, {word[:10]}')
