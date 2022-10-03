class ContractError(Exception):
    """We use this error when someone breaks our contract."""


#: Special value, that indicates that validation for this type is not required.
Any = object()


def contract(arg_types=None, return_type=None, raises=None):
    def contract_decorator(func):
        def wrapped(*args, **kwargs):
            all_args = tuple(args + tuple(kwargs.values()))
            if arg_types is not None:
                for elem in range(len(arg_types)):
                    if arg_types[elem] != Any:
                        if not isinstance(all_args[elem], arg_types[elem]):
                            raise ContractError("Invalid ArgType Error")
            try:
                result = func(*args, **kwargs)
            except (Exception if raises is None or Any in raises else raises) as exc:
                raise exc
            except Exception as ex:
                raise ContractError from ex
            if return_type is not None:
                if not isinstance(result, return_type):
                    raise ContractError("Invalid ReturnType Error")
            return result
        return wrapped
    return contract_decorator


@contract(arg_types=(Any, int), return_type=None, raises=(ZeroDivisionError,))
def add_two_numbers(first, second):
    return first + second


print(add_two_numbers(15, 7.5))