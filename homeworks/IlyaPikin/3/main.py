class ContractError(Exception):
    """We use this error when someone breaks our contract."""


#: Special value, that indicates that validation for this type is not required.
Any = object()


def contract(arg_types=None, return_type=None, raises=None):
    def my_decorator(func):
        def wrapper(*args):
            # Проверка наличия типа ошибки в списке
            def in_raises(exc_, raises_):
                for raise_class_ in raises_:
                    if isinstance(exc_, raise_class_):
                        return True
                return False

            # Проверка типов входящих аргументов
            if arg_types is not None:
                if len(args) != len(arg_types):
                    raise ContractError
                for arg, arg_type in zip(args, arg_types):
                    if type(arg) is not arg_type and arg_type is not Any:
                        raise ContractError

            try:
                result = func(*args)

            except Exception as exc:
                if in_raises(exc, raises):
                    raise exc
                else:
                    raise ContractError from exc

            # Проверка типа выходящего значения
            if return_type is not None:
                if type(result) is not return_type and return_type is not Any:
                    raise ContractError

            return result

        return wrapper

    return my_decorator

# Tests
@contract(arg_types=(int, int), return_type=int)
def add_two_numbers(first, second):
    return first + second


add_two_numbers(1, 2)  # ok


# add_two_numbers('a', 'b')  # raises ContractError


@contract(arg_types=(int, int), return_type=float, raises=(ZeroDivisionError,))
def div(first, second):
    return first / second

div(1, 2)  # ok
#div(1, 0)  # raises ZeroDisionError
#div(1, None)  # raises ContractError from TypeError


# validates only return type, args and raises are ignored:
@contract(return_type=int)
def add_two_numbers_1(first, second):
    return first + second


add_two_numbers_1(1, 2)


# validation is completely disabled:
@contract(return_type=None, arg_types=None, raises=None)
def add_two_numbers_2(first, second):
    return first + second


add_two_numbers_2(1, 2)

# return type and raises checks are disabled:
@contract(arg_types=(str, str))
def add_two_numbers_3(first, second):
    return first + second


add_two_numbers_3('1', '2')


@contract(arg_types=(int, Any))
def add_two_numbers_4(first, second):
    return first + second

add_two_numbers_4(1, 2)  # ok
add_two_numbers_4(1, 3.4)  # ok
#add_two_numbers(2.1, 1)  # raises ContractError