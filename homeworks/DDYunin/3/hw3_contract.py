class ContractError(Exception):
    """We use this error when someone breaks our contract."""
    # Для того, чтобы выдать исключения требуются: __init__ и __str__
    def __init__(self, *args):
        if args is None:
            self.message = "Стандартный текст ошибки контракта!"
        else:
            self.message = args[0]

    def __str__(self):
        return f"Произошла ошибка с текстом: {self.message}"

#: Special value, that indicates that validation for this type is not required.
Any = object()


def contract(arg_types=None, return_type=None, raises=None):
    def my_decorator(my_function):
        def wrapped(*args):
            # Сначала првоеряем на соответствие
            if arg_types is None:
                pass
            else:
                for arg, arg_type in zip(args, arg_types):
                    if type(arg) != arg_type and arg_type != Any:
                        raise ContractError("Error! Contract fail! Uncorrect arg_types") from TypeError
            # Проверяем возвращаемый тип на соответствие
            if return_type is None:
                pass
            else:
                if return_type != type(my_function(*args)) and return_type != Any:
                    raise ContractError("Error! Contract fail! Uncorrect return type") 
            try:
                # вызов функции
                result = my_function(*args)
            except:
                raise raises
            return result
        return wrapped
    return my_decorator

if __name__ == '__main__':
    
    @contract(arg_types=(int, int), return_type=Any)
    def add_two_numbers(first, second):
        return first + second

    add_two_numbers(1, 2)  # ok
    # add_two_numbers('a', 'b')  # raises ContractError

    @contract(arg_types=(int, int), return_type=float, raises=(ZeroDivisionError,))
    def div(first, second):
        return first / second

    div(1, 2)  # ok
    # div(1, 0)  # raises ZeroDisionError
    # div(1, None)  # raises ContractError from TypeError

    # validates only return type, args and raises are ignored:
    @contract(arg_types=(int, Any))
    def subtract_two_numbers(first, second):
        return first - second

    subtract_two_numbers(1, 2)  # ok
    subtract_two_numbers(1, 3.4)  # ok
    # subtract_two_numbers(2.1, 1)  # raises ContractError