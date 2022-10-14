class ContractError(Exception):
    """We use this error when someone breaks our contract."""


#: Special value, that indicates that validation for this type is not required.
Any = type(object())


def contract(arg_types=None, return_type=None, raises=None):
    """This function create contract decorator with the specified conditions"""
    def contract_decorator(function):
        def wrapped(*args, **kwargs):
            if arg_types is not None:
                all_args = (args + tuple(kwargs.values()))
                for arg_value, arg_type in zip(all_args, arg_types):
                    if not isinstance(arg_value, arg_type):
                        raise ContractError('Invalid argument type')

            if raises is None or Any in raises:
                return_value = function(*args, **kwargs)
            else:
                try:
                    return_value = function(*args, **kwargs)
                except raises as ex:
                    raise ex
                except Exception as ex:
                    raise ContractError from ex

            if return_type is not None:
                if not isinstance(return_value, return_type):
                    raise ContractError('Invalid return type')

            return return_value
        return wrapped
    return contract_decorator
