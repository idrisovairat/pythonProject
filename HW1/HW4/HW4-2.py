my_list = [15, 16, 2, 3, 1, 5, 6, 7, 8, 123, 1234]
more_then = [my_list[num] for num in range(0, len(my_list)) if my_list[num] > my_list[num -1]]
print(more_then)