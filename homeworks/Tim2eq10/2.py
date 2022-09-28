"""
Author : Timur Poletaev
Created : 23.09.2022
Updated : -
"""

class Array:

    def __init__(self, *args):
        self._data = args
    
    def append(self, element):
        self._data = self._data + (element,)

    def __add__(self, other):
        return Array(*(self._data + other._data))
    
    def __len__(self):
        return len(self._data)

    def index(self, element):
        for index_, el in enumerate(self._data):
            if el == element:
                return index_
        return -1

    def __iter__(self):
        self._iterator = iter(self._data)
        return self._iterator

    def __next__(self):
        return next(self._iterator)

    def __getitem__(self, index):
        return self._data[index]
    
    def __str__(self):
        return str(self._data)


def sample():
    lst = Array(1, 2, 3)
    for i in range(4, 6+1):
        lst.append(i)
    lst += Array(7, 8, 9)

    print("Our list : ", end='{')
    for x in lst:
        print(x, end=',')
    print('}')
    
    print(f"1 in list == {1 in lst}   index : {lst.index(1)}")
    print(f"10 in list == {10 in lst}   index : {lst.index(10)}")

    print(f"First element = {lst[0]}")
    print(f"Mid element = {lst[len(lst) // 2]}")
    print(f"Last element = {lst[-1]}")


if __name__ == "__main__":
    sample()
