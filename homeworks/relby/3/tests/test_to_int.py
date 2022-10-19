
import pytest

from contract.contract import contract
from contract.types import Any, ContractError


@contract(arg_types=(Any,), return_type=int, raises=(ValueError,))
def to_int(obj):  # noqa: WPS110
    return int(obj)


def test_return():
    assert to_int('12') == 12


def test_return_type():
    assert isinstance(to_int(3.5), int)


def test_in_raises():
    with pytest.raises(ValueError):
        to_int('asdfasdf')


def test_not_in_raises():
    with pytest.raises(ContractError):
        to_int({})
