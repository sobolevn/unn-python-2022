from typing import MutableSequence, Generic, TypeVar, Iterator, SupportsIndex, Iterable, overload

T = TypeVar('T')

# TODO: Replace explicit type annotation of Array with Self
# when python 3.11 release comes out


class Array(MutableSequence[T], Generic[T]):
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

    def insert(self, index: SupportsIndex, value: T) -> None:
        self._data = self._data[:int(index)] + (value,) + self._data[int(index):]

    def remove(self, value: T) -> None:
        index = self.index(value)
        if index == -1:
            raise ValueError('{0} not in array'.format(value))
        self.pop(index)

    # Information methods
    def empty(self) -> bool:
        return not len(self)

    def index(
        self,
        value: T,
        start: SupportsIndex | None = None,
        stop:  SupportsIndex | None = None,
    ) -> int:
        if start is None: start = 0
        if stop  is None: stop  = len(self)
        if not isinstance(start, SupportsIndex) or not isinstance(stop, SupportsIndex):
            raise TypeError('slice indices must be integers or have an __index__ method')
        try:
            return self._data.index(value, start, stop)
        except ValueError:
            return -1

    # Dunder methods
    # Math
    def __add__(self, array: 'Array[T]') -> 'Array[T]':
        if isinstance(array, Array):
            return Array(*self, *array)
        raise TypeError(
            "can only concatenate Array (not '{0}') to Array".format(
                array.__class__.__name__,
            ),
        )

    def __mul__(self, n: SupportsIndex) -> 'Array[T]':
        if isinstance(n, SupportsIndex):
            return Array(*self._data * n)
        raise TypeError(
            "can't multiply Array by non-int of type '{0}'".format(
                n.__class__.__name__,
            ),
        )

    def __len__(self) -> int:
        return len(self._data)

    def __contains__(self, value: object) -> bool:
        return value in self._data

    # Comparisons
    def __eq__(self, other: object) -> bool:
        if isinstance(other, Array):
            return self._data == other._data
        return False

    def __lt__(self, other: object) -> bool:
        if isinstance(other, Array):
            return self._data < other._data
        return False

    def __le__(self, other: object) -> bool:
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

    @overload
    def __getitem__(self, key: SupportsIndex) -> T: ...

    @overload
    def __getitem__(self, key: slice) -> 'Array[T]': ...

    def __getitem__(self, key: SupportsIndex | slice) -> T | 'Array[T]':
        match key:
            case slice():
                return Array(*self._data[key])
            case SupportsIndex():
                if not self._is_valid_index(key):
                    raise IndexError('Array index out of range')
                return self._data[key]
            case _:
                raise TypeError(
                    "Array indices must be integers or slices, not '{0}'".format(
                        key.__class__.__name__,
                    ),
                )

    @overload
    def __setitem__(self, key: SupportsIndex, value: T) -> None: ...

    @overload
    def __setitem__(self, key: slice, value: Iterable[T]) -> None: ...

    def __setitem__(self, key: SupportsIndex | slice, value: T | Iterable[T]) -> None:
        match key:
            case slice():
                if not isinstance(value, Iterable):
                    raise TypeError('can only assign to iterable')
                # Don't wanna implement this myself
                data = list(self._data)
                data[key] = value
                self._data = tuple(data)
            case SupportsIndex():
                if not self._is_valid_index(key):
                    raise IndexError('Array assignment index out of range')
                self._data = self._data[:key] + (value,) + self._data[int(key) + 1:]  # type: ignore
            case _:
                raise TypeError(
                    "Array indices must be integers or slices, not '{0}'".format(
                        key.__class__.__name__,
                    ),
                )

    @overload
    def __delitem__(self, key: SupportsIndex) -> None: ...

    @overload
    def __delitem__(self, key: slice) -> None: ...

    def __delitem__(self, key: SupportsIndex | slice) -> None:
        match key:
            case slice():
                self[key] = ()
            case SupportsIndex():
                if not self._is_valid_index(key):
                    raise IndexError('Array deletion index out of range')
                self._data = self._data[:key] + self._data[int(key) + 1:]  # type: ignore
            case _:
                raise TypeError(
                    "Array indices must be integers or slices, not '{0}'".format(
                        key.__class__.__name__,
                    ),
                )

    # Private methods
    def _is_valid_index(self, index: SupportsIndex) -> bool:
        ind = int(index)
        return -len(self) <= ind and ind < len(self)
