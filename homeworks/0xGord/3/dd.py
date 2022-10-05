class ContractError(Exception):
    """We use this error when someone breaks our contract."""


#: Special value, that indicates that validation for this type is not required.
Any = object()


def contract(arg_types=None, return_type=None, raises=None):

    def decorator(func):

        def wrapped(*args):
            if arg_types is not None:
                for _arg, _type in zip(args, arg_types):
                    if _type is not Any:
                        if not isinstance(_arg, _type):
                            raise ContractError

            try:
                return_value = func(*args)
            except raises:
                raise
            except Exception:
                raise ContractError
            if return_type is not None:
                if not isinstance(return_value, return_type):
                    raise ContractError

            return return_value

        return wrapped

    return decorator
