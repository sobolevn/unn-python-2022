import random
class Array(object):
    def __init__(self):
        self.array=[]
        
    def zapolnenie(self,x):
        for i in range(x):
            self.array= tuple(self.array)+tuple(str(random.randint(1,x)))
    def __init1__(self):
        self._data=self.array
    def append (self,y):     
        self.array=self.array+(y,)
        print("Список видоизменен:\nArray",self.array)
    def index(self,poisk):
        try:
            return self.array.index(poisk)
        except ValueError:
            return -1
flag=0
while flag!=10:
    print("Меню:\n[0] Выход из программы\n[1] Создать список\n[2] Дополнить список новым объектом\n[3] Объединить списки\n[4] Длина списка\n[5] Поиск элемента\n[6] Перебрать элементы списка\n[7] Получить значение по индексу")       
    vvod=int(input())       
    if vvod==0: 
        print("Выходим из программы...")
        flag=10
    elif vvod==1:
        print("Введите количество элементов в желаемом списке:")
        elements=int(input())
        mylist = Array()
        mylist.zapolnenie(elements)
        mylist.__init1__()  
        print("Список создан:\nArray",mylist.array)
    elif vvod==2:
        print("Введите объект:")
        newobject=input()
        mylist.append(newobject)
    elif vvod==3:
        print("Введите список, который хотите добавить:")
        spisok=input().split()
        mylist.array+=tuple(spisok)
        print("Списки обьединены:\nArray",mylist.array)
    elif vvod==4:
        print("Длина списка:", len(mylist.array))
    elif vvod==5:
        print("Введите объект, который хотите найти в списке:")
        poisk=input()
        print(mylist.index(poisk))
    elif vvod==6:
        for flag1 in range(len(mylist.array)):
            print(mylist.array[flag1])
    elif vvod==7:
        print("Введите индекс элемента, который вы хотите получить (учтите, в списке {0} объекта(ов)):".format(len(mylist.array)))
        _index=int(input())
        try:
            print(mylist.array[_index]) 
        except IndexError:
            print("Объект списка не найден")
    else:   
        print("Введены некорректные данные")
print("Новый список:\n", mylist.array)         
print("Старый список:\n",mylist._data)   
    


