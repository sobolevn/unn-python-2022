class Storage(object):  # storage = Storge()
    """
    Singleton storage.

    Read more about singleton design pattern:
    https://stackoverflow.com/questions/6760685/creating-a-singleton-in-python
    https://en.wikipedia.org/wiki/Singleton_pattern

    It is used to emulate in-memory storage.
    It should be replaced with a database in a real application.
    """

    obj = None
    items = None

    @classmethod
    def __new__(cls, *args):
        if cls.obj is None:
            cls.obj = object.__new__(cls)
            cls.items = []
        return cls.obj

    def is_empty(self):
        return len(self.items) == 0

    def print(self):
        if self.is_empty():
            print('There are no items in the storage.')
            return

        for index, obj in enumerate(self.items):
            print('{0}: {1}'.format(index, str(obj)))
