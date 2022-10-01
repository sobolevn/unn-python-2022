from typing import Optional, TypeAlias
from functools import wraps


class ContractError(Exception):
    """We use this error when someone breaks our contract."""

#: Special value, that indicates that validation for this type is not required.
Any: TypeAlias = object

ArgsType: TypeAlias = tuple[type, ...]
RaisesTypes: TypeAlias = tuple[type[Exception], ...]


def contract(
    arg_types: Optional[ArgsType] = None,
    return_type: Optional[type] = None,
    raises: Optional[RaisesTypes] = None,
):
    def _contract(func):
        def handle_kwargs(kwargs):
            if kwargs:
                raise NotImplementedError(
                    '`contract` decorator does not work with kwargs',
                )

        def handle_arg_types(args):
            if arg_types is None:
                return

            if len(args) != len(arg_types):
                raise ContractError(
                    'Length of `args_type` must be equal to length of `args`',
                )
            for arg, arg_type in zip(args, arg_types):
                if not isinstance(arg, arg_type):
                    raise ContractError('Args types do not match')
        
        def handle_raises(args):
            if raises is None:
                return

            try:
                func_result = func(*args)
            except Exception as ex:
                is_exception_in_raises = any(
                    (isinstance(ex, raising_ex) for raising_ex in raises),
                )
                if not is_exception_in_raises:
                    raise ContractError(
                        '`{0}` is not in raises'.format(type(ex).__name__),
                    ) from ex
                raise ex
            return func_result
        
        def handle_return_type(func_result, args):
            if return_type is None:
                return

            if func_result is None:
                func_result = func(*args)
            if not issubclass(type(func_result), return_type):
                raise ContractError('Return type does not match')
            return func_result


        @wraps(func)
        def wrapper(*args, **kwargs):
            handle_kwargs(kwargs)
            handle_arg_types(args)
            func_result = handle_raises(args)
            func_result = handle_return_type(func_result, args)
            if func_result is None:
                func_result = func(*args)
            return func_result
        return wrapper
    return _contract


@contract(arg_types=(int, int), return_type=float, raises=(ZeroDivisionError,))
def divide(first, second):
    "This function divides two ints"
    return first / second

@contract(arg_types=(str, str), return_type=str)
def concat(first, second):
    "This function concatenate two strings"
    return first + second

@contract(arg_types=(Any,), return_type=int, raises=(ValueError, TypeError))
def to_int(obj):
    return int(obj)
