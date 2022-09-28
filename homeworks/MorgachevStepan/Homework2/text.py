class Array(object):
    def __init__(self, *args):
        self._data = args

    def get_array(self):
        print(self._data)

    def append(self, number):
        self._data += (number, ) 

    def __len__(self):
        return len(self._data)

    def __add__(self, other):
        self._data += other._data

    def index(self, number):
        if number in self._data:
            return self._data.index(number)
        else:
           return -1

    def __iter__(self):
        return iter(self._data)

    def __getitem__(self, index):
        if index >= len(self._data) or index < 0:
            return "Error, such element does not exist"
        return self._data[index]
