class Array(object):

    def __init__(self, *numbers):
        self.arr = []
        for num in numbers:
            if type(num) == int or type(num) == float:
                self.arr.append(num)
            #elif type(num) == list or type(num) == tuple or type(num) == set:
             #   self.arr += list(num)
            else:
                try:
                    self.arr.append(int(num))
                except ValueError:
                    raise ValueError("Array can't contains strings")

        self._data = (self.arr, )

    def __len__(self):
        return len(self.arr)

    def __add__(self, other):
        if type(other) == int or type(other) == float:
            self.arr.append(other)
            return self
        elif type(other) == Array:
            self.arr += other.arr
            return self
        elif type(other) == list or type(other) == tuple or type(other) == set:
            self.arr += list(other)
            return self
        else:
            try:
                self.arr.append(int(other))
                return self
            except ValueError:
                raise ValueError("Array can't contains strings")

    def index(self, num):
        for i, elem in enumerate(self.arr):
            if num == elem:
                return i
        return -1

    def __iter__(self):
        return iter(self.arr)

    def __getitem__(self, key):
        return self.arr[key]

    def __setitem__(self, key, value):
        if type(value) == int or type(value) == float:
            self.arr[key] = value


a = Array(1, 2, '4', 6) + Array('100') + '87' + 4
print(a.arr)
a[0] = 10
print(a.arr)
