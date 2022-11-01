class ContractError(Exception):
    """We use this error when someone breaks our contract."""
    pass

#: Special value, that indicates that validation for this type is not required.
Any = object()


def contract(arg_types=None, return_type=None, raises=None):
    def contract_decorator(function):
        def inner(*args):
            if arg_types != None and arg_types != Any:
                for ind in range(len(args)):
                    if arg_types[ind] != Any:
                        if type(args[ind]) != arg_types[ind]:
                            raise ContractError
            try:
                result = function(*args)
                if return_type != None and return_type != Any:
                    if return_type != type(result):
                        raise ContractError
            except Exception as ex:
                raises = ()
                if type(ex) in raises:
                    raise ex
                else:
                    raise ContractError from ex
            return result
        return inner
    return contract_decorator