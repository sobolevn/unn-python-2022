class Array(object):

    def __init__(self, *args):
        self._data = tuple(args)

    def append(self, new_arg):
        self._data += (new_arg, )

    def __add__(self, new):
        return self._data + new._data

    def __len__(self):
        return len(self._data)

    def index(self, arg):
        if arg in self._data:
            return self._data.index(arg)
        return -1

    def __iter__(self):
        return iter(self._data) 

    def __getitem__(self, item):
        return self._data[item]

    def print(self):
        print(self._data)

# init_test
print('Init test:')
A = Array(1, 2, 3, 4, 5)
print('Array A')
A.print()

# append_test
print('Append test:')
A.append('abc')
print('Append element "abc" to array A')
A.print()

# add_test
print('Addition test:')
B = Array(100, 200)
print('Add array (100, 200) to array A')
print(A + B)

#len_test
print('Length test:')
print('Length of last array = {0}'.format(len(A+B)))

# index_test
print('Index test:')
print('Index of element 2 in array A')
print(A.index(2))
print('Index of element 89 in array A')
print(A.index(89))

# for_test
print('For loop test:')
for arg in A: 
    print(arg)

# []_test
print('Indexing test:')
print('Print first element of the array A:')
print(A[0])