class ContractError(Exception):
     """We use this error when someone breaks our contract."""

#: Special value, that indicates that validation for this type is not required.
Any = object()


def contract(arg_types=None, return_type=None, raises=None):
    def decorator(function):
        def argument_check(*args, **kwargs):
            if arg_types is not None:
                arguments = tuple(args) + tuple(kwargs.values())

                if len(arguments) != len(arg_types):
                    raise ContractError("Argument count error")
                else:
                    for index, arg_t in enumerate(arg_types):
                        if arg_t != Any and arg_t != type(arguments[index]):
                            raise ContractError("Argument type mismatch error")

            if return_type is None:
                pass
            else:
                if return_type != type(function(*args, **kwargs)) and return_type != Any:
                    raise ContractError("Return type error") 

            try:
                result = function(*args, **kwargs)
            except:
                raise raises

            return result
        return argument_check    
    return decorator



#First example
@contract(arg_types=(int, int), return_type=int)
def add_two_numbers(first, second):
    return first + second
print(add_two_numbers(1, 2))



#Second example
#add_two_numbers('a', 'b')



#Third example
#@contract(arg_types=(int, int), return_type=float, raises=(ZeroDivisionError,))
#def div(first, second):
#    return first / second
#
#print(div(1, 2))  # ok
#print(div(1, 0)) # raises ZeroDisionError
#print(div(1, None))  # raises ContractError from TypeError



#Fourth example
#validates only return type, args and raises are ignored:
#@contract(return_type=int)
#def return_myself(x):
#    return x
#
#print(return_myself(10))

# validation is completely disabled:
#@contract(return_type=None, arg_types=None, raises=None)
#def hello_world():
#    print('Hello, World!')
#hello_world()    

# return type and raises checks are disabled:
#@contract(arg_types=(str, str))
#def sum_string(x, y):
#    return x+y
#print(sum_string('abc', 'def'))



#Fifth example
#@contract(arg_types=(int, Any))
#def add_two_numbers(first, second):
#    return first + second
#
#print(add_two_numbers(1, 2))  # ok
#print(add_two_numbers(1, 3.4))  # ok
#print(add_two_numbers(2.1, 1))  # raises ContractError