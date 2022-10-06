class ContractError(Exception):
    """We use this error when someone breaks our contract."""


#: Special value, that indicates that validation for this type is not required.
Any = object()


def contract(arg_types=None, return_type=None, raises=None):
    def decorator_contract(function): # Декоратор имеет доступ только к аргументам декоратора
        def wrapped(*args, **kwargs): #Обёртка имеет доступ к аргументам функции, и к аргументам декоратора
            if arg_types is not None:
                all_args = tuple(args)+tuple(kwargs.values())
                if len(arg_types)!=len(all_args):
                    raise ContractError("Wrong Argument Number")
            if arg_types is not None:
                for index, value in enumerate(arg_types):
                    if value != type(all_args[index]) and value != Any:
                        raise ContractError("Wriong Argument Type")
            if return_type is not None:
                if return_type != type(function(*args, **kwargs)):
                    raise ContractError("Wrong Return Type")
            try:
                return function(*args,**kwargs)
            except Exception as ex:
                raise raises from ex
        return wrapped
    return decorator_contract
















# This examples are copied from another person's Pull Request

@contract(arg_types=(int, int), return_type=int)
def add_two_numbers(first, second):
    return first + second


print(add_two_numbers(1, 2))  # ok


try:
    add_two_numbers('a', 'b')  # raises ContractError
except(ContractError):
    print("OK")


@contract(arg_types=(int, int), return_type=float, raises=(ZeroDivisionError,))
def div(first, second):
    return first / second

print(div(1, 2))  # ok
try:
    div(1, 0)  # raises ZeroDisionError
except(ZeroDivisionError):
    print("ZeroOK")
try:
    div(1, None)  # raises ContractError from TypeError
except(ContractError):
    print("OK")


# validates only return type, args and raises are ignored:
@contract(return_type=int)
def add_two_numbers_1(first, second):
    return first + second


print(add_two_numbers_1(1, 2))


# validation is completely disabled:
@contract(return_type=None, arg_types=None, raises=None)
def add_two_numbers_2(first, second):
    return first + second


print(add_two_numbers_2(1, 2))

# return type and raises checks are disabled:
@contract(arg_types=(str, str))
def add_two_numbers_3(first, second):
    return first + second


print(add_two_numbers_3('1', '2'))


@contract(arg_types=(int, Any))
def add_two_numbers_4(first, second):
    return first + second

print(add_two_numbers_4(1, 2))  # ok
print(add_two_numbers_4(1, 3.4))  # ok
try:
    add_two_numbers(2.1, 1)  # raises ContractError
except(ContractError):
    print("OK")

@contract(arg_types=(int, Any))
def add_two_numbers5(first, second):
    return first + second

add_two_numbers5(1, 2)  # ok
add_two_numbers5(1, 3.4)  # ok
try:
    add_two_numbers5(2.1, 1)  # raises ContractError
except(ContractError):
    print("OK")
#...  # TODO: implement