class BaseItem(object):
    def __init__(self, heading):
        self.heading = heading
        self.done = False  # TODO: make sure we can use it...

    def __repr__(self):
        return self.__class__.__name__

    @classmethod
    def construct(cls):
        raise NotImplementedError()


class ToDoItem(BaseItem):
    def __str__(self):
        return '{0} {1}: {2}'.format(
            '+' if self.done else '-',
            super().__str__()[:4],
            # super().__str__(self),
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
        return '{0} {1}: {2} for {3}'.format(
            '+' if self.done else '-',
            super().__str__()[:5],
            # super().__str__(self),
            self.heading,
            self.price,
        )

    @classmethod
    def construct(cls):
        heading = input('Input heading: ')
        price = input('Input price: ')
        return cls(heading, price)

# Делаю новый тип задачи
class ToReadItem(BaseItem):
    def __init__(self, heading, url):
        super().__init__(heading)
        self.url = url

    def __str__(self):
        return '{0} {1}: {2} {3}'.format(
            '+' if self.done else '-',
            super().__str__()[:6],
            self.heading,
            self.url
        )

    @classmethod
    def construct(cls):
        heading = input('Input heading: ')
        url = input('Input url: ')
        return cls(heading, url)