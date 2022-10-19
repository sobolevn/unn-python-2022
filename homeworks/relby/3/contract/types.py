from typing import TypeAlias


class ContractError(Exception):
    """We use this error when someone breaks our contract."""


#: Special value, that indicates that validation for this type is not required.
Any: TypeAlias = object

ArgsType: TypeAlias = tuple[type, ...]
RaisesTypes: TypeAlias = tuple[type[Exception], ...]
