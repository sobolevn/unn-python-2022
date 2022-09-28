class Array(object):
    """ "List" class """

    def __init__(self, *args):
        self._data = args

    def __len__(self):
        return len(self._data)

    def __add__(self, other):
        res = Array()
        res._data = self._data + other._data
        return res

    def __str__(self):
        return str(self._data)

    def __getitem__(self, item):
        return self._data[item]

    def __iter__(self):
        self._iterator = iter(self._data)
        return self._iterator

    def __next__(self):
        return next(self._iterator)

    def index(self, item):
        for i in self._data:
            if self[i] == item:
                return i
        return -1

    def append(self, elem):
        self._data += tuple(elem)


arr1 = Array(1, 2, 3, 4, 5)
arr2 = Array(6, 7, 8)
arr0 = Array()
arr1.append("+")
print("Printing the sum of arrays:")
print(arr1 + arr2)
print("Printing an empty arr:")
print(arr0)
print("Printing the element of the first array at number 5:")
print(arr1[5])
print("Printing the index of the element '+':")
print(arr1.index('+'))
print("Printing the len of the sum of arrays:")
print(len(arr1+arr2))



