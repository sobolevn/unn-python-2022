class ContractError(Exception):
    """We use this error when someone breaks our contract."""


#: Special value, that indicates that validation for this type is not required.
Any = object()


def contract(arg_types=None, return_type=None, raises=None):
    def decorated_contract(func):
        def wrapped(*args, **kwargs):
            if arg_types is not None:
                allArgs = tuple(args + tuple(kwargs.values()))
                for index in range(len(arg_types)):
                    if arg_types[index] != Any:
                        if not isinstance(allArgs[index], arg_types[index]):
                            raise ContractError("ArgsType Error")
            try:
                result = func(*args, **kwargs)
            except (Exception if raises is None or Any in raises else raises) as ex:
                raise ex
            except Exception as ex:
                raise ContractError from ex
            if return_type is not None:
                if not isinstance(result, return_type):
                    raise ContractError("ReturnType Error")
            return result
        return wrapped
    return decorated_contract


@contract(arg_types=(int, int), return_type=float, raises=(ZeroDivisionError,))
def div(one, two):
    return one / two


print(div(1, 234.5))
