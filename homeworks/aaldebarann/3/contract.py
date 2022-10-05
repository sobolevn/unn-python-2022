
class ContractError(Exception):
    pass
    """We use this error when someone breaks our contract."""


#: Special value, that indicates that validation for this type is not required.
Any = object()

def contract(arg_types=None, return_type=None, raises=None):
    def decorator(function):
        def inner(*args):
            if not (arg_types is None):
                # should check arg_types
                for i in range(len(arg_types)):
                    if arg_types[i] == Any:
                        continue
                    if not isinstance(args[i], arg_types[i]):
                        raise ContractError("{0} arg {1} type is {2} (must be {3})"
                                            .format(function, i, type(args[i]), arg_types[i]))
            # now we know argument types are correct
            try:
                result = function(*args)
                if not (return_type is None):
                    # should check return_type
                    if not isinstance(result, return_type):
                        raise ContractError("{0} return type is {1} (must be {2})"
                                            .format(function, type(result), return_type))
                return result
            except Exception as e:
                # here is an exception - should we check it's type?
                if not (raises is None):
                    # should check exception types
                    if not (raises is Any or isinstance(e, raises)):
                        raise ContractError("{0} raises exception {1} (must be {2})"
                                            .format(function, type(e), raises)) from TypeError
                raise e
        return inner
    return decorator
