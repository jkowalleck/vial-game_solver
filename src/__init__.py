from typing import Iterable, Union, Tuple, TypeGuard
from collections import Counter
from itertools import chain

_VIAL_LEN = 4
_T_VIAL = Union[
    Tuple[None, None, None, None],
    Tuple[None, None, None, object],
    Tuple[None, None, object, object],
    Tuple[None, object, object, object],
    Tuple[object, object, object, object],
]

EMPTY_VIAL = [None, None, None, None]

_ITEM_COUNT = 4

def validate(vials) -> TypeGuard[Iterable[_T_VIAL]]:
    for v, vial in enumerate(vials):
        assert (l := len(vial)) == _VIAL_LEN, \
            f'veil #{v} has len {l} - expected {_VIAL_LEN}'
        nones = tuple(v is None for v in vial)
        assert nones == (True, True, True, True) \
               or nones == (True, True, True, False) \
               or nones == (True, True, False, False) \
               or nones == (True, False, False, False) \
               or nones == (False, False, False, False), \
            f'veil #{v} has holes: {vial!r}'
    ic = Counter(chain.from_iterable(vials))
    del ic[None]
    for i, c in ic.items():
        assert c == _ITEM_COUNT, \
            f'item {i!r} appeared {c} times - expected {_ITEM_COUNT}'
    return True

def vial_solved(vial) -> bool:
    return vial[0] == vial[1] == vial[2] == vial[3]

def vial_empty(vial) -> bool:
    return None is vial[0] is vial[1] is vial[2] is vial[3]

def solve(vials):
    solution = []

    return solution
