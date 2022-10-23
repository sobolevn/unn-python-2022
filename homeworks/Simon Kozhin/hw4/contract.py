

class ContractError(Exception):
    """We use this error when someone breaks our contract."""
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None
    def __str__(self):
        if self.message:
            return (f"ContractError {self.message}")
        else:
            return ("ContractError has been raised")




#: Special value, that indicates that validation for this type is not required.
Any = object()


def contract(arg_types=None, return_type=None, raises=None):
    def decorator(func):
        def wrapped(*args, **kwargs):
            for index, value in enumerate(tuple((*args, *kwargs,))):
                if type(value) is not Any and type(value) != arg_types[index]:
                    raise ContractError ("Не поддерживаемый тип данных") from TypeError
            
            try:
                a = func(*args, **kwargs)
            except(Exception
                    if raises is None or Any in raises
                    else raises) as ex:
                raise ex
            
            except(Exception) as ex:
                raise ContractError(f"Непредвиденная ошибка {type(ex)} ")

            if type(a) != return_type and type(a) is not Any:               
                raise ContractError("Неверный тип возвращаемых данных")
            return a
                
        return wrapped
    return decorator
   
@contract(arg_types=(int, Any))
def add_two_numbers(first, second):
    return first + second

add_two_numbers(1, 2)  # ok
add_two_numbers(1, 3.4)  # ok
add_two_numbers(2.1, 1)  # raises ContractError