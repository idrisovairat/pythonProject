my_list = [9, 8 , 7, 6, 5, 4, 3, 2, 1]
new_number = int(input('введите новый элемент рейтинга'))
i = 0

for n in my_list:
    if new_number <= n:
        break


my_list.insert(i, float(new_number))
print(my_list)