class ContractError(Exception):
    """We use this error when someone breaks our contract."""
#: Special value, that indicates that validation for this type is not required.
Any = object()

def contract(arg_types=None,return_type=None,raises=None):
    def decor(func):
        def wrapper(*args):
            counter=0
            for i in range(0,2):
                if arg_types[i]!=type(args[i]) and type(arg_types[i])==type(Any):
                    counter+=1
                elif arg_types[i]==type(args[i]):
                    counter+=1
            if counter==2:
                print("Каждый тип в кортеже - соответсвует типу аргумента")
            else:
                print("Типы аргументов в кортеже не соответствуют")
                raise ContractError("ContractError")
            try:
                result=func(*args)
                print("Result=", result)
            except raises:
                raise raises
            except:
                raise ContractError("ContractError")
        return wrapper
    return decor      
@contract(arg_types=(int, int),return_type=int)
def add_two_numbers(first,second): 
    return first+second  
add_two_numbers(1,2)
        
        
@contract(arg_types=(int, int), return_type=float, raises=(ZeroDivisionError,))
def div(first, second):
    return first / second

div(1, 2)  # ok
'''div(1, 0) # raises ZeroDisionError
   div(1, None)'''  # raises ContractError from TypeError

@contract(arg_types=(int, Any))
def new_add_two_numbers(first,second): 
    return first+second  
new_add_two_numbers(1, 2)  # ok
new_add_two_numbers(1, 3.4)  # ok
new_add_two_numbers(2.1, 1)  # raises ContractError

