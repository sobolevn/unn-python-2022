class ContractError(Exception):
    def __init__(self,*args):
        self.messege = args[0] if args else None

    def __str__(self):
        return f"Mistake: {self.messege}"

Any = object()

def contract(arg_types=None, return_type=None, raises=None):
    def decorator(func):
        def wrapped(*args, **kwargs):
            for index,value in enumerate(tuple((*args,*kwargs))):
                if type(value) is not Any and type(value) != arg_types[index]:
                    raise ContractError("Type argument not support") from TypeError

            try:
                res = func(*args, **kwargs);
            except (Exception if raises is None or Any in raises else raises) as ex:
                raise ex          
            except Exception as ex: 
                raise ContractError("Error isn't in raises: " + type(ex).__name__) from ex

            if type(value) is not Any and type(res) != return_type:
                raise ContractError("Type return not support") from TypeError

            return res
        return wrapped
    return decorator

@contract(arg_types=(int, int), return_type=float, raises=(NameError,))
def sum(first, second):
    return first / second
