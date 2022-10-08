# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class Array(object):
    def __init__(self, *number):
        self._data=number
    def append(self,elem):
        self._data+=tuple(elem)
    def __add__(self,Array):
        return self._data+Array._data
    def __len__(self):
        return len(self._data)
    def __getitem__(self,item):
        return self._data[item]
    def index(self,elem):
        if elem in self._data:
            return self._data.index(elem)
        else:
            return -1
    def __str__(self):
        return str(self._data)


    def __iter__(self):
        return iter(self._data)
    def __next__(self):
        return next(iter(self._data))
A1=Array(0,1,2,3,4)
A2=Array(5,)
print("array A1:")
print(A1)
print("Array A2:")
print(A2)
print("concatenation A1 & A2")
print(A1+A2)
A0=Array()
print("empty Array:")
print(A0)
print("length of A1")
print(len(A1))
print("checking of for working:")
for element in Array(1,2,3):
    print(element)
print("the second element in A1:")
print(A1[1])
print("adding an element in A1")
A1.append("6")
print(A1)