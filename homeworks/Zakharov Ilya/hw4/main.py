class ContractError(Exception):
    def contract(arg_types=None, return_type=None):
        def func_decorator(func):
            def check(*args, **kwargs):
                if arg_types is None:
                    pass
                else:
                    for i, arg_type in enumerate(arg_types):
                        if type(args[i]) != arg_type:
                            raise ContractError("Ошибка типизации")
                        if args[1] == 0:
                            raise ZeroDivisionError("Ошибка типизации")
                if return_type is None:
                    pass
                else:
                    if type(func(*args, **kwargs)) != return_type:
                        raise ContractError("Ошибка типизации")
                return func(*args, **kwargs)

            return check

        return func_decorator
    Any = object()

    @contract(arg_types=(float, int), return_type=float)
    def add_two_numbers(first, second):
       return first / second


print(ContractError.add_two_numbers(3.3, 3))