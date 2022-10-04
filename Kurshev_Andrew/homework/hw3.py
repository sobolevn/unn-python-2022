class ContractError(Exception):
    pass




Any = object()


def contract(arg_types=None, return_type=None, raises=None):

    def decorator(func):
        
        def wrapped(*args):
            
            if (Any in arg_types) and (arg_types.count(Any) == 1):

                return func(*args)

            elif (Any in arg_types) and (arg_types.count(Any) > 1):

                raise ContractError("Слишком много Any")
                    

            if tuple(map(type,args)) !=arg_types:
                            
                raise ContractError("Неверный тип аргументов")


            for i in raises:
                try:
                    func(*args)
                except i:
                    raise i
                except Exception:
                    if Exception not in raises:
                        raise ContractError()

            return func(*args)

        return wrapped

    return decorator


@contract(arg_types=(int,Any) )
def add_numbers(first,second):
    return first+second

@contract(arg_types=(int,int), return_type = float, raises=(ZeroDivisionError,))
def div(first,second):
    return first/second



print(add_numbers(1,2.5))

print(div(1,1))

print(div(1,"1"))


 
