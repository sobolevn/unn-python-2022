
class Array(object):
    
    def __init__(self, *args):
        self._data = args
    
    def append(self, item):
        self._data = self._data + (item,);

    def __len__(self):
        return len(self._data)

    def index(self, elem):
        if (elem in self._data):
            return self._data.index(elem)
        return -1
    
    def __getitem__(self, index_of_elem):
        return self._data[index_of_elem]

    def __add__(self, other):
        result = Array()
        result._data = self._data + other._data
        return result

    def __iadd__(self, other):
        self._data += other._data
        return self

    def __str__(self):
        return str(self._data)



print('Create: \n\ta = Array()\n\tb = Array("qwe")\n\tc = Array("asd","zxc")')

a = Array()
b = Array("qwe")
c = Array("asd","zxc")

print("We have:\n\ta = {0}\n\tb = {1}\n\tc  = {2}\n".format(str(a),str(b),str(c)))
print('Trying to find index "qwe" in a, get : ' + str(a.index("qwe")))
print('Trying to find index "qwe" in b, get : ' + str(b.index("qwe")))

print("\nLen of c == " + str(len(c)))

print('\nc[1] = ' + c[1])

print('\nc = a + b')
c = a + b
print("c = " + str(c))


print('\nc += b')
c += b
print("b = " + str(b))
print("c = " + str(c))


print('\nc.append("SomeText")')
c.append("SomeText")
print("c = " + str(c))
print('\ntryign to use "for elem in c" and get :')

for elem in c:
    print(elem)