#class ContractError(Excepetion):
    """We use this error when someone breaks our contract."""


#: Special value, that indicates that validation for this type is not required.
Any = object()


def contract(arg_types=None, return_type=None, raises=None):
    ...  # TODO: implement

@contract(arg_types = (int,int), return_type = double)
def div(first,second):
    return a / b;