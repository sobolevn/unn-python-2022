class Array(object):

    def __init__(self, *args):
        self._data = args

    def append(self, *args):
            self._data += args

    def __add__(self, other):
        res = Array(*self._data)
        res._data += other._data
        return res

    def __len__(self):
        return len(self._data)

    def index(self, elem):
        ind = -1
        for i in range(len(self._data)):
            if (elem == self._data[i]):
                ind = i
        return ind

    def __iter__(self):
        return iter(self._data)

    def __getitem__(self, ind):
        return self._data[ind]
        

a1 = Array(1, 2, 3)
a2 = Array(4, 5, 6)
print(a1._data)
print(a2._data)
a2.append(7, 8)
print(a2._data)
a3 = a1 + a2
print(a3._data)
print(len(a3))
print(a3.index(4))
print(a3[4])
for element in a3:
    print(element*100)
