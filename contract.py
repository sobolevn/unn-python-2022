class ContractError(Exception):
    """We use this error when someone breaks our contract."""


#: Special value, that indicates that validation for this type is not required.
Any = object()


def contract(arg_types=None, return_type=None, raises=None):
    def decorator(func):
        def wrapper(*args,**kwargs):        
            if arg_types != None:
                Arg_types_check = args+tuple(kwargs.values())
                for i in range(len(arg_types)):
                    if arg_types[i] is not Any:
                        if not isinstance(Arg_types_check[i],arg_types[i]):
                            raise ContractError("ArgsTypeError")
            try:
                Return_check = func(*args,**kwargs)
            except (Exception if Any in raises or raises is None else raises) as Raises_check:
                raise Raises_check
            except Exception as ex:
                raise ContractError from ex
            if return_type != None:
                if not isinstance(Return_check,return_type):
                    raise ContractError("ReturnTypeError")
            return Return_check        
        return wrapper   
    return decorator



#test
@contract(arg_types=(int, int), return_type=float, raises=(ZeroDivisionError,))
def div(first, second):
    return first / second
