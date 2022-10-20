from functools import wraps
from typing import Optional

from contract.handlers import (
    handle_arg_types,
    handle_kwargs,
    handle_raises,
    handle_return_type,
)
from contract.types import ArgsType, RaisesTypes


def contract(
    arg_types: Optional[ArgsType] = None,
    return_type: Optional[type] = None,
    raises: Optional[RaisesTypes] = None,
):
    def _contract(func):  # noqa: WPS430
        @wraps(func)
        def wrapper(*args, **kwargs):
            handle_kwargs(kwargs)  # type: ignore
            handle_arg_types(arg_types, args)  # type: ignore
            func_result = handle_raises(  # type: ignore
                raises,
                args,
                func=func,
            )
            func_result = handle_return_type(  # type: ignore
                return_type,
                func_result,
                args,
                func=func,
            )
            if func_result is None:
                func_result = func(*args)
            return func_result
        return wrapper
    return _contract
