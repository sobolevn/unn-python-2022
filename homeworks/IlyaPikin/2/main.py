class Array(object):
    def __init__(self, *args):
        self._data = tuple(args)

    def __add__(self, other):
        return Array(*self._data, *other._data)

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        if self.i < len(self._data):
            ind = self.i
            self.i += 1
            return self._data[ind]
        else:
            raise StopIteration

    def __getitem__(self, key):
        return self._data[key]

    def append(self, x):
        self._data = (*self._data, x)

    def index(self, x):
        for i in range(len(self._data)):
            if self._data[i] == x:
                return i
        return -1

    def print(self):
        print(self._data)


# test 1
print('test 1')
print('Создание списка объектов.')
my_arr = Array(1, 2, 3)
Array.print(my_arr)
print()

# test 2
print('test 2')
print('Добавление нового элемента.')
my_arr.append(4)
my_arr.print()
print()

# test 3
print('test 3')
print('Сложение списков.')
array_sum = (Array('a') + Array('b'))
array_sum.print()
print()

# test 4
print('test 4')
print('Нахождение длины.')
print(len(my_arr))
print()

# test 5
print('test 5')
print('Нахождение индекса элемента.')
print('Какой индекс у элемента "2"?')
print(my_arr.index(2))
print('Существует ли элемент "5"?')
print(my_arr.index(5))
print()

# test 6
print('test 6')
print('Работа с циклом `for`.')
for el in my_arr:
    print(el, end=' ')
print('\n')

it = iter(my_arr)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print()

for el in array_sum:
    print(el, end=' ')
print('\n')

# test 7
print('test 7')
print('Получение элемента с индексом [1]:')
print(my_arr[1])
