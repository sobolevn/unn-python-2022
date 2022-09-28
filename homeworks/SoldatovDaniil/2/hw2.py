class Array(object):

    def __init__(self, *args):
        self._data = tuple(args)

    def append(self, elem):
        self._data = (*self._data, elem)

    def __add__(self, other):
        return Array(*(self._data + other._data))

    def __radd__(self, other):
        return Array(*(other._data + self._data))

    def show(self):
        print(self._data)

    def __len__(self):
        return len(self._data)

    def index(self, elem):
        if elem in self._data:
            return self._data.index(elem)
        else:
            return -1

    def __getitem__(self, index):
        return self._data[index]


a = Array(1, 2, 123, 56)
b = Array(1, 1000)

a.show()
b.show()

a += b
a = a + b
b = a + Array(0)

a.show()
b.show()
print(a[3])

for i in a:
    print(i)
