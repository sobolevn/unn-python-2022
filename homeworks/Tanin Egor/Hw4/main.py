class ContractError(Exception):
    """We use this error when someone breaks our contract."""
    pass


#: Special value, that indicates that validation for this type is not required.
Any = object


def contract(arg_types=None, return_type=None, raises=(None,)):
    def decorator(func):
        return_value = None                                             # Var for checking return type

        def wrapped(*args):
            if arg_types is not None:
                for ind_of_arg, argument in enumerate(args):            # Check if types of args are appropriate
                    if not isinstance(argument, arg_types[ind_of_arg]):
                        raise ContractError(" unsupported operand")

            nonlocal return_value
            if arg_types is not None and return_type is not None:       # Deal with exceptions if needed
                try:
                    return_value = func(*args)
                    return return_value
                except Exception as e:
                    if e in raises:     # Not sure how to correctly write check if we got exception which is in raises
                        raise e
                    else:
                        raise ContractError from e
            else:                                                       # If we don't care about exceptions
                return_value = func(*args)
            return return_value

        if return_type is not None:
            if isinstance(return_value, return_type):                   # Check if return type is appropriate
                return wrapped
            else:
                raise ContractError("unsupported return type")
        else:
            return wrapped

    return decorator


@contract(arg_types=(int, int), return_type=Any, raises=(ZeroDivisionError,))
def add(x, y):
    return x/y


print(add(1, 0))