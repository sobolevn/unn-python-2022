# Класс списков

class Array(object):
    def __init__(self, *args):
        self._data = args

    def append(self, item):
        self._data += (item,)

    def __add__(self, other):
        result = Array()
        result._data = self._data + other._data
        return result

    def __len__(self):
        return len(self._data)

    def index(self, item):
        if item in self._data:
            return self._data.index(item)
        else:
            return -1

    def __iter__(self):
        return iter(self._data)

    def __getitem__(self, index):
        return self._data[index]

    def __str__(self):
        return str(self._data)
