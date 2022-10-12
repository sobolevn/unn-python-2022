from typing import Any
class Array(object):

    def __init__(self, *args):
        self._data = tuple(args)
    def len(self):
        return len(self._data)
    def append(self, elem: Any):
        self._data = tuple((*self._data, elem))
    def __add__(self, other):
        result = Array()
        result._data = tuple((*self._data, *other))
        return result
    def index(self, arg):
        i = 0
        while i != len(self._data):
            if self._data[i] != arg:
                i+=1
                continue
            else:
                return i
        else:
            return -1
    def __getitem__(self, item):
        return self._data[item]

    def __iter__(self):
        self. iter = 0
        return self

    def __next__(self):
        if self.iter<self.len():
          x = self[self.iter]
          self.iter += 1
        else: raise StopIteration
        return x

#tests
MyArray=Array(1,2,3)
MyArray2=Array(1,2,3)
MyArray=MyArray+MyArray2
print(MyArray[3])
print(MyArray.index(2))
print(MyArray.len())
result = 0
for element in Array(1, 2, 3):
    result+=element
print(result)



