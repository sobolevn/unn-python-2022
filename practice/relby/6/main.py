from typing import get_type_hints


class ValidateTypes(type):
    def __call__(self, *args, **kwargs):
        if args:
            raise TypeError('Can only work with kwargs')
        type_hints = get_type_hints(self)

        for key, value in kwargs.items():
            typ = type_hints.get(key, None)
            if typ is None:
                raise TypeError('`{0}` not in class definition'.format(key))
            if not isinstance(value, typ):
                raise TypeError(
                    'The field `{0}` has a type `{1}` but the argument of type `{2}` were given'.format(
                        key,
                        typ.__name__,
                        type(value).__name__,
                    )
                )
            setattr(self, key, value)
        return self


class User(object, metaclass=ValidateTypes):
    email: str
    age: int

x = User(email='a', age=18)
User(email=1, age=19)
User(email='a', age='b')
