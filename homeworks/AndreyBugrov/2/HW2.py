import time


class Array(object):
    def __init__(self, *array):
        self._data = tuple(array)
    def __add__(self, other):
        self._data = (*self._data, *other._data)
        return self
    def __len__(self):
        return len(self._data)
    def index(self, item):
        if item in self._data:
            return self._data.index(item)
        else:
            return -1
    def __getitem__(self, key):
        if(type(key)!=type(1)):
            raise TypeError
        if key >= len(self._data):
            raise KeyError
        if key < 0:
            raise KeyError
        return self._data[key]
    def print(self):
        print(self._data)
    def append(self, elem):
        new_data = (*self._data, elem)
        self._data = new_data
    def __iter__(self):
        return iter(self._data)
a = Array(1,2,3)
a.print()
a.append(4)
a.print()
b = Array(5,6)
a = a+b
a.print()
print(f"a[3] = {a[3]}")
for i in a:
    print(i)
try:
    print(a[3])
   # print(a["Nikita Sobolev"])
    print(a[len(a)])
except TypeError:
    print("В Python удобное сравнение типов")
    print(type("Nikita Sobolev"))
except KeyError:
    print("Сравнение на границы обычное")
    print(len(a))
c = Array()
c.print()
time.sleep(5)





