def my_func(x, y, z):
    my_list = [x, y, z]
    try:
        my_list.remove(min(my_list))
        return sum(my_list)
    except TypeError:
        return 'enter only a numbers'
print(my_func(1, -10, 3))
