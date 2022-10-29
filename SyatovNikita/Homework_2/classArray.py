class Array(object):
    def __init__(self, *args):
        self._data = tuple(args)

    def append(self, new_arg):
        self._data += (new_arg, )

    def __add__(self, other):
        return self._data + other._data

    def __len__(self):
        return self._data.__len__()

    def index(self, arg):
        if arg in self._data:
            return self._data.index(arg)
        return -1

    def __iter__(self):
        return self._data.__iter__()

    def __getitem__(self, item):
        return self._data[item]

# Testing:
A = Array(1, 2)
A.append(3)
print(Array(1) + Array(2))
print(len(Array(1, 2, 3)))
print(A.index(1))

for element in A:
    if element == 1:
        print(A[A.index(element)])
