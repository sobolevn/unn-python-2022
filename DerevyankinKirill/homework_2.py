class Array(object):
    def __init__(self, *args):
        self._data = [*args]

    def __len__(self):
        return len(self._data)
    
    def __str__(self):
        return str(self._data)

    def __getitem__(self, index):
        return self._data[index]

    def __iter__(self):
        return iter(self._data)
    
    def __add__(self, other):
        res = Array()
        res._data = self._data + other._data
        return res
    
    def _append(self, item):
        self._data.append(item)
        print(f'Append = {self._data}')
        
    def _index(self, obj):
        if obj in self._data:
            print(f'index =',self._data.index(obj))
        else:
            print(f'index = {-1}')
        
    def _len(self):
        return len(self._data)
    
array = Array()
print(f'Empty array =',array)
array_1 = Array(6)
print(f'First array =', array_1)
array_2 = Array(1,2,3)
print(f'Second array =', array_2)
array_1._append(52)
array._data = array_1._data + array_2._data
print('Sum of first and second arry =',array._data)
array._len()
print('Length sum array =',len(array))
array._index(52)
array._index(152)

print('All element from sum array:')

for element in array._data:
    print(element)

print(f'Elemet number 4 from sum array =', array[3])
