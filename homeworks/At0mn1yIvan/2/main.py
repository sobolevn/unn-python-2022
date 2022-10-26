class Array(object):

    def __init__(self, *args):
        self._data = tuple(args)

    def append(self, obj):
        self._data = (*self._data, obj)

    def __add__(self, other):
        return Array(*(self._data + other._data))

    def __radd__(self, other):
        return Array(*(other._data + self._data))

    def __len__(self):
        return len(self._data)

    def index(self, obj):

        if obj in self._data:
            return self._data.index(obj)
        else:
            return -1

    def __getitem__(self, index):
        return self._data[index]

    def printArr(self):
        print(self._data)


#test

#1
print("_______№1_______")
a = Array()
b = Array(1)
c = Array(1, 2, 3)
a.printArr()
b.printArr()
c.printArr()

#2
print("_______№2_______")
a.append(2)
a.printArr()

#3
print("_______№3_______")
a = b + c
a.printArr()
a += c
a.printArr()

#4
print("_______№4_______")
print(len(a))

#5
print("_______№5_______")
print(c.index(2))
print(c.index(5))

#6
print("_______№6_______")
for element in c:
    print(element)

#7
print("_______№7_______")
print(Array('a', 'b', 'c', 'd')[0])
print(c[2])