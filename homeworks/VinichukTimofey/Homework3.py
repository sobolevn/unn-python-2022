#-------------------------------------------------------------------------------
# Name:        HomeWork3
# Purpose:
#
# Author:      Тимофей
#
# Created:     02.10.2022
# Copyright:   (c) Тимофей 2022

#-------------------------------------------------------------------------------
class ContractError(Exception):
    """We use this error when someone breaks our contract."""
Any = object()
def contract(arg_types=None, return_type=None, raises=None):
    def new_decor(func):
        def arg_check(*susp, **ksusp):

## По сути: мы не знаем, какой набор аргументов у подлежащей функции
## Этот екоратор же занимается проверкой подлежащей функции
## Склейка (декорирование) происходит исключительно для этого
## Поэтому ставим *susp, **ksusp от слова неизвестность
            if arg_types is not None:
                args=tuple(susp+tuple(ksusp.values()))

                if len(args)!=len(arg_types):
                    raise ContractError('discrepancy between the number of arguments and the required')
                else:
                    for ind, arg_t in enumerate(arg_types):
                        if arg_t!=Any:
                            if arg_t!=type(args[ind]):
                                raise ContractError('arg type mismatch')

                    ##return 'ok'

            try:
                err_sch=func(*susp, **ksusp)

            except (Exception if raises is None or Any in raises else raises) as err:
                raise err

            except Exception as err:
                raise ContractError('error not in list') from err
            if return_type is not None:
                if isinstance( err_sch, return_type):
                            raise ContractError('return type mismatch')
            return err_sch


        return arg_check

    return new_decor

@contract(arg_types=(int, Any), return_type=int, raises=(ArithmeticError,))
def add(a, b):
    return a + b
print (add(1,"b"))
