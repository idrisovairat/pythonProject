from functools import reduce

def mul_lust(el_1, el_2):
    return el_1 * el_2

uniq_list = [el for el in range(100, 1001, 2)]
print(f"List\n{uniq_list}\nMultriplocation of numbers\n{reduce(mul_lust, uniq_list)}")