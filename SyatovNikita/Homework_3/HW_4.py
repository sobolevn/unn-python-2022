class ContractError(Exception):
    """We use this error when someone breaks our contract."""
    pass

#: Special value, that indicates that validation for this type is not required.
Any = object()


def contract(arg_types=None, return_type=None, raises=None):
    def decorator(function):
        def inner(*args, **kwargs):
            if arg_types is not None:
                this_args = (tuple(args) + tuple(kwargs.values()))
                for i in range(len(arg_types)):
                    if arg_types[i] is not Any:
                        if not isinstance(this_args[i], arg_types[i]):
                            raise ContractError('Argument: not that type')
            if return_type is not None:
                if not isinstance(function(*args, **kwargs), return_type):
                    raise ContractError("Return: not that type")
            try:
                result = function(*args, **kwargs)
            except (Exception if raises is None or Any in raises else raises) as error:
                raise error
            except Exception as ex:
                raise ContractError from ex

            return result
        return inner
    return decorator




#checking
@contract(arg_types=(int, float), return_type=int, raises=(ContractError, ))
def add_two_numbers(first, second):
    return first + second

#print(add_two_numbers(2, 3))
#print(add_two_numbers('a', 'b'))

@contract(arg_types=(int, int), return_type=float, raises=(ZeroDivisionError,))
def div(first, second):
    return first / second

#print(div(1, 2))
#print(div(1, 0))
#print(div(1, None))
