from random import randint

my_list = [randint(-1000, 1000) for _ in range(20000)]

uniq_list = [el for el in my_list if my_list.count(el) == 1]

print(my_list)