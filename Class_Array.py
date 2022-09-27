class Array(object):
    
    data = ()
    i = 0
    
    def __init__(self,*args):
        self.data = ()
        self.data = self.data + args


    def __len__(self):
        return len(self.data)


    def append(self,*args):
        self.data = self.data + args


    def __add__(self,nself):
        c = Array()
        c.data = c.data + self.data
        c.data = c.data + nself.data
        return c


    def index(self,arg):
        for i in range(len(self.data)):
            if self.data[i] == arg:
                return i
        return -1

    def __getitem__(self,i):
        return self.data[i]

    def __iter__(self):
        return self

    def __next__(self):
        if self.i<len(self.data):
            s = self.i
            self.i += 1
            return self.data[s]
        else:
            self.i = 0
            raise StopIteration

##test
##a = Array(1,2)
##b = Array(4,5,6,7,8,9)
##c = Array()
##c = a+b
##c.append(17)
##print(a.data,b.data,c.data)
####test
##print(len(a),len(b),len(c))
##print(a.index(1),b.index(4),c.index(1))
##print(a[-1],b[0],c[-1])
##for i in a:
##    print(i,' a element')
##for i in b:
##    print(i,' b element')
##for i in c:
##    print(i,' c element')

