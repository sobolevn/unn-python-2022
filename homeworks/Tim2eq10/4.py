"""
Author : Timur Poletaev
Created : 03.10.2022
Updated : -
"""

class ContractError(Exception):
    """We use this error when someone breaks our contract."""
    pass


#: Special value, that indicates that validation for this type is not required.
Any = object()


def contract(arg_types=None, return_type=None, raises=None):
    def decorator(func):
        def dec_inner(*args):

            if arg_types is not None:
                for type_, expected_type_ in zip(args, arg_types):
                    if expected_type_ is not Any:
                        if not isinstance(type_, expected_type_):
                            raise ContractError("Bad type") from TypeError

            if raises is not None:
                try:
                    result = func(*args)
                except raises:
                    raise
                except Exception as ex:
                    raise ContractError("raised exception not in raises")
            else:
                try:
                    result = func(*args)
                except Exception as ex:
                    raise ContractError("raised exception not in raises") from ex

            if return_type is not None:
                if expected_type_ is not Any:
                    if not isinstance(result, return_type):
                        raise ContractError("Bad type") from TypeError

            return result

        return dec_inner

    return decorator        
