import pytest

from contract import Any, ContractError, contract

@contract(
    arg_types=(int, int, int),
    return_type=float,
    raises=(ZeroDivisionError,),
)
def add_and_divide(first, second, third):
    return (first + second) / third


@contract(arg_types=(Any,), return_type=int, raises=(ValueError,))
def to_int(obj):
    return int(obj)


# Tests
def test_return1():
    assert add_and_divide(1, 2, 3) == 1.0

def test_return2():
    assert to_int('12') == 12

def test_return_type1():
    assert isinstance(add_and_divide(12, 23, 46), float)

def test_return_type2():
    assert isinstance(to_int(3.5), int)

def test_invalid_args():
    with pytest.raises(ContractError):
        add_and_divide('1', '2', '3')

def test_in_raises1():
    with pytest.raises(ZeroDivisionError):
        add_and_divide(1, 2, 0)

def test_in_raises2():
    with pytest.raises(ValueError):
        to_int('asdfasdf')

def test_not_in_raises():
    with pytest.raises(ContractError):
        to_int({})


