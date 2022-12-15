class Array(object):
#Конструктор. * Как раз и решает вопрос нескольких параметров
    def __init__(self, *ar):
         self._data = ar
#Добавление. По сути просто делаем новый кортеж с новым поледним элементом
    def append(self, last):
        self._data+= (last,)
#Сложение. Через магический метод.
    def __add__(self, other):
        return Array(*(self._data + other._data))
#Размер. Через магическйи метод
    def __len__(self):
        return len(self._data)
#Индекс. Пользуемся существующим
    def index(self, num):
        if num in self._data:
            return self._data.index(num)
        else:
            return -1
#Цикл. Нужен для перебора.
    def __iter__(self):
        return iter(self._data)
#Для работы с индексами.
    def __getitem__(self, num):
        return self._data[num]

a1=Array(1,2,3)
a1.append(2)
print(a1[3])
a2=Array(2,3)
a2=a2+a1
print(a2[4])
print(len(a2))
print(a2.index(2))
print(a2.index(-1))
for a in a2:
    print(a)






