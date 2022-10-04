class ContractError(Exception):
    """We use this error when someone breaks our contract."""

#: Special value, that indicates that validation for this type is not required.
Any = object()

def contract(arg_types=None, return_type=None, raises=None):
    def decorator_contract(func):
        def wrapper(*args, **kwargs):
            kor = tuple(args + tuple(kwargs))
            print(kor)
            if arg_types != None:
                for i in range(len(kor)):
                    if arg_types[i] != Any:
                        if (arg_types[i] != type(kor[i])):
                            raise ContractError("TypeError")
            try:
                result = func(*args, **kwargs)
            except (Exception if raises is None or Any in raises else raises) as exc:
                raise exc
            except Exception as exс:
                raise ContractError from exс
            if return_type is not None:
                if not isinstance(result, return_type):
                    raise ContractError("Invalid ReturnType Error")
            return result
        return wrapper
    return decorator_contract

@contract(arg_types = (int,Any), return_type = int, raises=None)
def add_two_numbers(first, second):
    print(first + second)
    return first + second

a = add_two_numbers(10,12)
