
class Array(object):
    def __init__(self, *args):
        self.data = tuple(args)

    def __add__(self, other):
        return Array(*self.data, *other.data)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, ind):
        return self.data[ind]

    def append(self, p):
        self.data = (*self.data, p)

    def index(self, p):
        for i in range(len(self.data)):
            if self.data[i] == p:
                return i
        return(-1)
    def print(self):
        print(self.data)


Null = Array() #Создание пустого списка 

Arr = Array(1, 2, 3) #Список из трех объектов 
Array.print(Arr)

Arr.append(4) #Добавляем в конец списка новый элемент 
Array.print(Arr)

__Arr = Array(6)
X = Arr + __Arr #Сложение двух списков 
Array.print(X)

print(Arr[2]) #Получение значения по индексу 






    

    


