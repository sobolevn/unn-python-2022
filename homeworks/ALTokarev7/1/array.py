class Array(object):

    def __init__(self, *args):
        self._data = args 
    
    def __len__(self):
        return len(self._data)

    def __str__(self):
        return str(self._data)

    def __getitem__(self, ind):
        return self._data[ind]
    
    def __iter__(self):
        return iter(self._data) 
    
    def __add__(self, other):
        res = Array()
        res._data = self._data + other._data
        return res 

    def append(self, arg):
        self._data = self._data + (arg,)

    def index(self, obj):
        if obj in self._data:
            return( self._data.index(obj) )
        return -1

def main():
    array_a = Array()
    array_b = array_a + Array(1,2,3)
    print(Array(1,2,3,4,5))

if __name__ == "__main__":
    main()


