class Array(object):

    def __init__(self, *data):
       self._data = data

    def __add__(self, *other):
        result = Array()
        result._data = self._data + tuple(*other)
        return tuple(result._data)

    def append(self, element):
        self._data += (element,)

    def __len__(self):
        return len(self._data)

    def index(self, object):
        for i in range(len(self._data)):
            if self._data[i] == object:
                return i
                break
        else:
            return -1

    def __iter__(self):
        return iter(self._data)

    def __getitem__(self, item):
        return self._data[item]

    def __str__(self):
        return str(self._data)




