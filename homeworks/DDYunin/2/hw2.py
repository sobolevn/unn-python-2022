class Array(object):
    
    # Конструктор (инициализирует данные)
    def __init__(self, *args):
        self._data = tuple(args)
        # print(type(self._data))
    
    # Печатает элементы array
    def printdata(self):
        for item in self._data:
            print(f"Элемент массива = {item}")
        print()

    # Добавляет элемент к array
    def append(self, arg):
        self._data = self._data + (arg,)
    
    # складывает элементы array (складываем 2 tuple и распаковываем его с помощью *)
    def __add__(self, array):
        return Array(*(self._data + array._data))
         
    # функция, которая выдаёт длину array
    def __len__(self):
        return len(self._data)
    
    # Определяет index элемента в array
    # Как будто есть ещё какой-то вариант
    def index(self, elem):
        if elem in self._data:
            return self._data.index(elem)
        return -1

    # позволяет получить значение array с помощью []
    def __getitem__ (self, index):
        return self._data[index]

    # Позволяет делать итерацию в цикле for по array
    def __iter__(self):
        return iter(self._data)

# 1) Создавать себя как на примере: `Array()` - пустой списо,
#  `Array(1)` = список из одного объекта `1`, `Array(1, 2, 3)`
# список из трех объектов. `Array` должен уметь работать с любым количеством аргументов 

print("\nТест № 1\n")
a = Array()
b = Array(1)
c = Array(1, 'c', "Hello", (2,3,4), 0.2)

# 2) Добавлять новый объект внутрь списка через метод `.append()`

print("\nТест № 2\n")
b.printdata()
b.append('Hello')
b.printdata()

# 3) Складываться с другими `Array`. Например: `Array(1) + Array(2) == Array(1, 2)`

print("\nТест № 3\n")
d = b + c
d.printdata()

# 4) Узнавать свою длину через функцию `len()`

print("\nТест № 4\n")
print(f"Длина Array d = {len(d)}")

# 5) находить индекс переданного объекта через метод `.index()`, возвращаем `-1`, 
# если такого объекта в списке нет. Например: `Array('a', 'b').index('b') == 1`

print("\nТест № 5\n")
print(d.index(1))
print(d.index("c"))
print(d.index(2))

# 6) Работать с циклом `for`: `for element in Array(1, 2, 3):`

print("\nТест № 6\n")
for elem in d:
    print(elem)

# 7) Получать значение по индексу при помощи `[]`. Пример: `Array('a')[0] == 'a'`

print("\nТест № 7\n")
print(d[0])
print(d[3])
