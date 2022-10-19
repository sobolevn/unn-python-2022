from contract.types import ContractError


def handle_kwargs(kwargs):
    if kwargs:
        raise NotImplementedError(
            '`contract` decorator does not work with kwargs',
        )


def handle_arg_types(arg_types, args):
    if arg_types is None:
        return

    if len(args) != len(arg_types):
        raise ContractError(
            'Length of `args_type` must be equal to length of `args`',
        )
    for arg, arg_type in zip(args, arg_types):
        if not isinstance(arg, arg_type):
            raise ContractError('Args types do not match')


def handle_raises(raises, args, *, func):
    if raises is None:
        return None

    try:
        func_result = func(*args)
    except raises as ex:  # noqa: WPS329
        raise ex
    except Exception as ex:
        raise ContractError(
            '`{0}` is not in raises'.format(type(ex).__name__),
        ) from ex
    return func_result


def handle_return_type(
    return_type,
    func_result,
    args,
    *,
    func,
):
    if return_type is None:
        return None

    if func_result is None:
        func_result = func(*args)
    if not isinstance(func_result, return_type):
        raise ContractError('Return type does not match')
    return func_result
