class Array(object):
    def __init__(self,*args):
        self._data=(args)
    def append(self,*args):
        self._data=self._data+args
    def __add__(self,other):
            help=Array()
            for i in self:
                help.append(i)
            for i in other:
                help.append(i)
            return help
            #return Array=self._data + other._data
    def __len__(self):
        return len(self._data)
    def index(self,*args):
        if len(args)==1:
            if args[0] in self._data:
                return self._data.index(args[0])
            else:
                return -1
        help=[]
        for i in args:
            if i in self._data:
                help.append(self._data.index(i))
            else:
                help.append(-1)
        return help
    def __getitem__(self,i):
        return self._data[i]
    def print(self):
        print(self._data)

# Проверка
# """
# myclass=Array('a')
# myclass.print()
# arr=Array('a','b','c')
# arr.print()
# mysecond=Array()
# mysecond.print()
# fird=Array()
# for i in myclass:
#     print(i)
# fird=myclass+mysecond
# fird.print()
# print(len(fird))
# fird.append('b')
# print(fird._data)
# fird.print()
# print(fird.index('a'))
# print(fird.index('a','b'))
# print(fird[0])
# """