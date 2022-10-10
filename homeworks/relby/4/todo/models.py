class BaseItem(object):
    def __init__(self, heading: str):
        self.heading: str = heading
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
    def __init__(self, heading: str, price: int):
        super().__init__(heading)
        self.price: int = price

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


class ToReadItem(BaseItem):
    def __init__(self, heading: str, url: str):
        super().__init__(heading)
        self.url: str = url

    def __str__(self):
        return '{0}: {1} {2}'.format(
            super().__str__(),
            self.heading,
            self.url,
        )

    @classmethod
    def construct(cls):
        heading = input('Input heading: ')
        url = input('Input url: ')
        return cls(heading, url)
