class Array(object):
    def __init__(self, *args):
        self._data = [*args]

    def append(self, element):
        self._data.append(element)

    def add_array(self, mas):
        self._data += mas

    def len(self):
        sum = 0
        for i in self._data:
            sum += 1
        return sum

    def index(self, ind):
        for i in range(0, self.len()):
            if ind == self._data[i]:
                return i
        return -1

    def element_to_ind(self, ind):
        try:
            return self._data[ind]
        except:
            return "list index out of range"

A = Array(3, 4, 5)
B = (31, 38)
A.append(7)
print(A._data)
A.add_array(B)
print(A._data)
print(A.len())
print(A.index(31))
print(A.element_to_ind(2))
print(A.element_to_ind(9))
