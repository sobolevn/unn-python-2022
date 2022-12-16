class BaseItem(object):

    status = {False : '-', True : '+'}

    def __init__(self, heading):
        self.heading = heading
        self.done = False  # TODO: make sure we can use it...
        
    def __repr__(self):
        return self.__class__.__name__

    def __str__(self):
        return '{0} {1}'.format(
            self.status[self.done],
            self.__class__.__name__[:-4]
            )
        
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
        price = input('Input price: ')
        return cls(heading, price)


class ToReadItem(BaseItem):
    def __init__(self, heading, url):
        super().__init__(heading)
        self.url = url

    def __str__(self):
        return '{0}: {1} from {2}'.format(
            super().__str__(),
            self.heading,
            self.url,
        )

    @classmethod
    def construct(cls):
        heading = input('Input heading: ')
        url = input('Input url: ')
        return cls(heading, url)
