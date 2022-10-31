class Array(object):
    def __init__(self, *args):
        self._data = args

    def __len__(self):
        return len(self._data)

    def __getitem__(self, index):
        return self._data[index]

    def __add__(self, other):
        tmp = Array()
        tmp._data = self._data + other._data
        return tmp

    def __iter__(self):
        return iter(self._data)

    def append(self, obj):
        self._data = self._data + (obj,)
        return self

    def index(self, obj):
        if self._data.count(obj) > 0:
            return self._data.index(obj)
        else:
            return -1


# тестовая программа (проверим по очереди пункты задания):

a = Array()
b = Array("give", "you", "up")
a.append("never").append("gonna")
c = a + b
print("len(c) =", len(c))
print("index(\"up\") = {}".format(c.index("up")))
print("index(\"down\") =  {}".format(c.index("down")))
print("here is your array:")
for elem in c:
    print(elem)
print("c[2] = ", c[2])