my_list = list(input('ввдеите число без пробелов = '))

for i in range(0, len(my_list), 10):
    my_list[i - 1], my_list[i] = my_list[i], my_list[i-1]

print(my_list)
