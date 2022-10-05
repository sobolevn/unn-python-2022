class ContractError(Exception):
    """We use this error when someone breaks our contract."""


#: Special value, that indicates that validation for this type is not required.
Any = object()


def contract(arg_types=None, return_type=None, raises=None):
    def contract_decorator(function):
        def wrapped(*args, **kwargs):
            if arg_types is not None:
                for index in range(len(arg_types)):
                    this_type = arg_types[index]
                    this_arg = (args + tuple(kwargs.values()))[index]
                    if this_type is not Any:
                        if not isinstance(this_arg, this_type):
                            raise ContractError('Invalid input data type')

            try:
                return_value = function(*args, **kwargs)
            except (Exception if raises is None or
                    Any in raises else raises) as ex:
                raise ex
            except Exception as error:
                raise ContractError from error

            if return_type is not None:
                if not isinstance(return_value, return_type):
                    raise ContractError('Invalid output data type')

            return return_value
        return wrapped
    return contract_decorator


