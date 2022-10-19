from math import isclose

import pytest

from contract.contract import contract
from contract.types import ContractError


@contract(
    arg_types=(int, int, int),
    return_type=float,
    raises=(ZeroDivisionError,),
)
def add_and_divide(first, second, third):
    return (first + second) / third


def test_return():
    assert isclose(add_and_divide(1, 2, 3), 1.0)


def test_return_type():
    assert isinstance(add_and_divide(12, 23, 46), float)


def test_invalid_args():
    with pytest.raises(ContractError):
        add_and_divide('1', '2', '3')


def test_in_raises():
    with pytest.raises(ZeroDivisionError):
        add_and_divide(1, 2, 0)
