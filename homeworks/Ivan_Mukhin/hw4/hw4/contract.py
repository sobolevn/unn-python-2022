class ContractError(Exception):
    """We use this error when someone breaks our contract."""


#: Special value, that indicates that validation for this type is not required.
Any = object()


def contract(arg_types=None, return_type=None, raises=None):
    def error_processing(function):
        def decor(*args, **kwargs):
            if arg_types != None:
                for i, elem in enumerate(arg_types):
                    if elem != Any and arg_types[i] != type(args[i]):
                        raise ContractError('Wrong arguments')
            try:
                res = function(*args, **kwargs)
            except (raises if raises is not None and Any not in raises else Exception) as ex:
                raise ex
            except Exception:
                raise ContractError from Exception
            if return_type is not None and not isinstance(res, return_type):
                raise ContractError('Return types not equal')

            return res
        return decor
    return error_processing









@contract(arg_types=(float, int), return_type=int, raises=None)
def add_two_numbers(first, second):
    return first + second

add_two_numbers('a', 'b')

@contract(arg_types=(int, int), return_type=float, raises=(ZeroDivisionError,))
def div(first, second):
    return first / second

div(1, 2)