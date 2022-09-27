class Array(object):

    data = ()
    __counter__ = 0

    def __init__(self,*arg):
        self.data = arg
        
    def append(self,*a1):
        self.data+=a1

    def __add__(self,other):
        c = Array()
        c.data = self.data + other.data
        return c
    
    def __len__(self):
        return len(self.data)

    def index(self,a1):
        if a1 in self.data:
            return self.data.index(a1)
        else:
            return -1

    def __getitem__(self,index):
        return self.data[index]

    def __iter__(self):
        return self
    
    def __next__(self):
        if(self.__counter__>=len(self.data)):
            raise StopIteration
        self.__counter__+=1
        return self.data[self.__counter__-1]
