class ContractError(Exception):
    """We use this error when someone breaks our contract."""
    pass


#: Special value, that indicates that validation for this type is not required.
Any = object()


def contract(arg_types=None, return_type=None, raises=None):
    def decorator(function):
        def wrapped(*args, **kwargs):
            if arg_types != None:
                this_args = (tuple(args) + (tuple(kwargs.values())))
                for el in range(len(arg_types)):
                    if arg_types[el] != Any:
                        if not isinstance(this_args[el], arg_types[el]):
                            raise ContractError
            if return_type != None:
                if not isinstance(function(*args, **kwargs), return_type):
                    raise ContractError
            try:
                result = function(*args, **kwargs)
            except (Exception if raises != None or Any in raises else raises) as ex1:
                raise ex1
            except Exception as ex2:
                raise ContractError from ex2
            return result
        return wrapped
    return decorator



@contract(arg_types=(int, int), return_type=int, raises = (ContractError, ))
def add_two_numbers(first, second):
    return first + second

@contract(arg_types=(int, int), return_type=float, raises=(ZeroDivisionError,))
def div(first, second):
    return first / second


#print(div(1, 2))
#print(div(1, 0))
print(add_two_numbers(15, 7.5))
