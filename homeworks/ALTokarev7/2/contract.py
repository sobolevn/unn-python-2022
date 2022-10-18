class ContractError(Exception):
    """We use this error when someone breaks our contract."""


#: Special value, that indicates that validation for this type is not required.
Any = object()


def contract(arg_types=None, return_type=None, raises=None):
    def decorator(func):
        def wrapped(*args):
            if arg_types is not None:
                for num in range(len(args)):
                    if arg_types[num] != Any and arg_types[num] is not None:
                        if type(args[num]) != arg_types[num]:
                            raise ContractError
            try:
                ret = func(*args)
            except Exception as ex:
                if type(ex) in raises:
                    raise ex
                else:
                    raise ContractError from ex
            if return_type is not None and return_type != Any:
                if type(ret) != return_type:
                    raise ContractError
            return ret
        return wrapped
    return decorator
