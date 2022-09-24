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
    mas_a = Array(1,2) 
    print(f'first array = {mas_a}' )
    mas_b = Array(3,4,5,6)
    print(f'second array = {mas_b}' )
    mas_a.append(33) 
    print(f'first array after append(33) = {mas_a}')
    mas_sum = mas_a + mas_b  
    print(f'array of sum first and second: {mas_sum}')
    print(f'length of sum array is {len(mas_sum)}')
    print(f'index of element 1 in sum array is {mas_sum.index(1)}')

    for el in mas_sum: #array working with for loop
        print(el)

    print(f'Sum array el number [1] is {mas_sum[1]}')

if __name__ == "__main__":
    main()


