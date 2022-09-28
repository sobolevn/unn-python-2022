class Array(object):
    def __init__(self, *args):
        self._data = tuple(args)

    def append(self, element):
        self._data += element,

    def __iadd__(self, other):
        self._data += other._data
        return self

    def __add__(self, other):
        return Array(self._data + other._data)

    def __len__(self):
        return len(self._data)

    def index(self, element):
        if element in self._data:
            return self._data.index(element)
        else:
            return -1

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        if self.i < len(self._data):
            temp = self.i
            self.i += 1
            return self._data[temp]
        else:
            raise StopIteration

    def __getitem__(self, key):
        return self._data[key]

    def __str__(self):
        return str(self._data)