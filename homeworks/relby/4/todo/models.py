class BaseItem(object):
    def __init__(self, heading):
        self.heading = heading
        self.done: bool = False

    def get_class_name(self):
        return self.__class__.__name__[:-4]

    def __str__(self):
        return '{0} {1}'.format(
            '+' if self.done else '-',
            self.get_class_name(),
        )

    def mark_done(self):
        self.done = True

    def mark_undone(self):
        self.done = False

    @classmethod
    def construct(cls):
        raise NotImplementedError()


class ToDoItem(BaseItem):
    def __str__(self):
        return '{0}: {1}'.format(
            super().__str__(),
            self.heading,
        )

    @classmethod
    def construct(cls):
        heading = input('Input heading: ')
        return cls(heading)


class ToBuyItem(BaseItem):
    def __init__(self, heading, price):
        super().__init__(heading)
        self.price = price

    def __str__(self):
        return '{0}: {1} for {2}'.format(
            super().__str__(),
            self.heading,
            self.price,
        )

    @classmethod
    def construct(cls):
        heading = input('Input heading: ')
        while True:
            try:
                price = int(input('Input price: '))
            except ValueError:
                print('Price must be an integer')
            else:
                if price >= 0:
                    break
                print("Price can't be negative")
            
        return cls(heading, price)
