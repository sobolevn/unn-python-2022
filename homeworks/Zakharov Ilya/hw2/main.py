class Array(object):
    def __init__(self, *item):
        super().__init__()
        self._data = [*item]

    def append(self, item):
        self._data.append(item)

    def index(self, obj):
        if obj in self._data:
            return(self._data.index(obj))
        return -1

    def __len__(self):
        return len(self._data)


array0 = Array()
array1 = Array(7)
array2 = Array(0, 1, 2)
array1.append(123)
array0._data = array1._data + array2._data
print(array0._data)
len(array0)
print(array0.index(123))
print(array0.index(321))
for element in array0._data:
    print(element)
print(array0._data[1])