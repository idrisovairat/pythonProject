my_list = [(-1 + 0j), 1, 4.4, True, None, 'Srting', [3,4],
           (5.5, 4, 3), {7: 'seven', 8: 'eight'}, {9, 10}, range(11)]

for i, item in enumerate (my_list, 1):
    print(f'{i}) {item} - {type(item)}')

