class ContractError(Exception):
    """We use this error when someone breaks our contract."""


#: Special value, that indicates that validation for this type is not required.
Any = object()

def contract(arg_types=None, return_type=None, raises=None):
    def decorator_contract(my_function):
        def wrapper(*args,**kwargs):
            try:
                my_function(*args,**kwargs)
            except raises:
                raise raises
            except:
                raise ContractError("ContractError")
            if return_type!=None:
                if return_type!=type(my_function(*args,**kwargs)):
                    raise ContractError("ContractError")
            if arg_types!=None:
                for n,tp in enumerate(arg_types):
                    if tp!=type(args[n]) and Any!=tp  :
                        raise ContractError("ContractError")
            return my_function(*args,**kwargs)
        return wrapper
    return decorator_contract

            
if __name__ == '__main__':
    @contract(arg_types=(int, int), return_type=float, raises=(ZeroDivisionError,))
    def div(first, second):
        return first / second

    print(div(1, 2))  # ok
    #print(div(1, 0))  # raises ZeroDisionError
    #print(div(1, None))  # raises ContractError from TypeError


    @contract(arg_types=(int, int), return_type=int)
    def add_two_numbers(first, second):
        return first + second

    print(add_two_numbers(1, 2))  # ok


    @contract(arg_types=(int, Any))
    def add_two_numbers2(first, second):
        return first + second

    print(add_two_numbers2(1, 2))  # ok
    print(add_two_numbers2(1, 3.4))  # ok
    #print(add_two_numbers2(2.1, 1))  # raises ContractError
                    