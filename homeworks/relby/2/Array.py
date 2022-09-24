from typing import Generic, Iterator, SupportsIndex, TypeVar, Iterable, overload

T = TypeVar('T')

# TODO: Replace explicit type annotation of Array with Self
# when python 3.11 release comes out


class Array(Generic[T]):
    def __init__(self, *args: T) -> None:
        self._data: tuple[T, ...] = args

    @classmethod
    def from_iterable(cls, iterable: Iterable[T]) -> 'Array[T]':
        if isinstance(iterable, Iterable):
            return Array[T](*iterable)
        raise TypeError('Array can only be created with iterable object')

    # Modification methods
    def append(self, value: T) -> None:
        self._data += (value,)

    def extend(self, iterable: Iterable[T]) -> None:
        self._data += tuple(iterable)

    def pop(self, index: SupportsIndex | None = None) -> T:
        if not isinstance(index, SupportsIndex) and index is not None:
            raise TypeError(
                "'{0}' object cannot be interpreted as an integer".format(
                    index.__class__.__name__,
                ),
            )
        if self.empty():
            raise IndexError('pop from empty Array')

        ind = len(self) - 1 if index is None else index.__index__()
        if index is None:
            ind = len(self) - 1
        else:
            ind = x if (x := index.__index__()) > 0 else len(self) + x
            if ind < 0 or ind >= len(self):
                raise IndexError('pop index out of range')

        item = self._data[ind]
        self._data = self._data[:ind] + self._data[ind + 1:]
        return item

    def clear(self) -> None:
        self._data = ()

    def insert(self, index: SupportsIndex, value: T) -> None:
        self._data = self._data[index:] + (value,) + self._data[index:]

    def reverse(self) -> None:
        self._data = self._data[::-1]

    def remove(self, value: T) -> None:
        index = self.index(value)
        if index == -1:
            raise ValueError('{0} not in array'.format(value))
        self.pop(index)

    # Information methods
    def empty(self) -> bool:
        return not len(self)

    def copy(self) -> 'Array[T]':
        return self[:]

    def index(self, value: T) -> int:
        try:
            return self._data.index(value)
        except ValueError:
            return -1

    def count(self, value: T) -> int:
        return self._data.count(value)

    # Dunder methods
    @overload
    def __getitem__(self, key: SupportsIndex, /) -> T: ...

    @overload
    def __getitem__(self, key: slice, /) -> 'Array[T]': ...

    def __getitem__(self, key: SupportsIndex | slice, /) -> T | 'Array[T]':
        match key:
            case slice():
                return Array(*self._data[key])
            case SupportsIndex():
                return self._data[key]
            case _:
                raise TypeError(
                    "Array indices must be integers or slices, not '{0}'".format(
                        key.__class__.__name__,
                    ),
                )

    @overload
    def __setitem__(self, key: SupportsIndex, value: T, /) -> None: ...

    @overload
    def __setitem__(self, key: slice, value: Iterable[T], /) -> None: ...

    def __setitem__(self, key: SupportsIndex | slice, value: T | Iterable[T], /) -> None:
        match key:
            case slice():
                if not isinstance(value, Iterable):
                    raise TypeError('can only assign to iterable')
                # Don't wanna implement this myself
                data = list(self._data)
                data[key] = value
                self._data = tuple(data)
            case SupportsIndex():
                self._data = self._data[:key] + (value,) + self._data[key + 1:]  # type: ignore
            case _:
                raise TypeError(
                    "Array indices must be integers or slices, not '{0}'".format(
                        key.__class__.__name__,
                    ),
                )

    def __add__(self, array: 'Array[T]', /) -> 'Array[T]':
        if isinstance(array, Array):
            return Array(*self, *array)
        raise TypeError(
            "can only concatenate Array (not '{0}') to Array".format(
                array.__class__.__name__,
            ),
        )

    def __mul__(self, n: SupportsIndex, /) -> 'Array[T]':
        if isinstance(n, SupportsIndex):
            return Array(*self._data * n)
        raise TypeError(
            "can't multiply Array by non-int of type '{0}'".format(
                n.__class__.__name__,
            ),
        )

    def __len__(self) -> int:
        return len(self._data)

    # Comparisons
    def __eq__(self, other: object, /) -> bool:
        if isinstance(other, Array):
            return self._data == other._data
        return False

    def __lt__(self, other: object, /) -> bool:
        if isinstance(other, Array):
            return self._data < other._data
        return False

    def __le__(self, other: object, /) -> bool:
        if isinstance(other, Array):
            return self._data <= other._data
        return False

    # Iteration
    def __iter__(self) -> Iterator[T]:
        return iter(self._data)

    # Conversion to string
    def __str__(self) -> str:
        return '[{0}]'.format(', '.join(map(repr, self._data)))

    def __repr__(self) -> str:
        types = ' | '.join({x.__class__.__name__ for x in self._data})
        return '{0}[{1}](data={2})'.format(
            self.__class__.__name__,
            types,
            self,
        )
