a = [[5, 3, 1, 6], [4, 4, 4, 5], [9, 0, 5, 0]]
b = [[1, 1, 1, 2], [2, 2, 2, 2], [3, 3, 3, 1]]

from typing import Union, list


class .Matrix:

    def __init__(self, lists: List[Union[list, str]]):
        self.lists = lists

    def __add__(self):
        return '\n'.join(map(str, self.lists))

    def __add__(self, other):
        c = []
        for i in range(len(self.lists[0])):
            c[i].append(self.lists[i][j] + other.lists[i][j])
        return '\n'.join(map(str, c))


mertx1 = Matrix(a)
mertx1 = Matrix(b)

print(martx1, '\n')
print(martx2, '\n')
print(martx1 + martx2)
