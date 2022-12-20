class Array(object):
    def __init__(self, *args):
        self._data = args

    def append(self, obj):
        l = list(self._data)
        l.append(obj)
        self._data = tuple(l)

    def __add__(self, other):
        l1 = list(self._data)
        l2 = list(other._data)
        l1.extend(l2)
        self._data = tuple(l1)
        return tuple(l1)

    def __len__(self):
        return len(self._data)

    def index(self, obj):
        if obj in self._data:
            return self._data.index(obj)
        else:
            return -1

    def __getitem__(self, index):
        return self._data[index]

    def show(self):
        print(self._data)