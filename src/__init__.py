__all__ = ['EMPTY_VIAL', 'solve']

from collections.abc import Iterable

from collections import Counter
from itertools import chain
from typing import TypeVar

T = TypeVar('T')

VIAL_SIZE = 4
"number of items per vial"

T_ITEM = object
T_EMPTY = None
T_VIAL = tuple[T_EMPTY, T_EMPTY, T_EMPTY, T_EMPTY] | \
         tuple[T_EMPTY, T_EMPTY, T_EMPTY, T_ITEM] | \
         tuple[T_EMPTY, T_EMPTY, T_ITEM, T_ITEM] | \
         tuple[T_EMPTY, T_ITEM, T_ITEM, T_ITEM] | \
         tuple[T_ITEM, T_ITEM, T_ITEM, T_ITEM]
EMPTY_VIAL: T_VIAL = (None, None, None, None)

T_game_state = tuple[T_VIAL, ...]

ITEM_COUNT = 4
"number of appearances of each item/colo/symbol"


def make_vials(vials_: Iterable[Iterable[T_ITEM | T_EMPTY]]) -> T_game_state:
    vials = tuple(map(tuple, vials_))
    for v, vial in enumerate(vials):
        assert (l := len(vial)) == VIAL_SIZE, \
            f'veil #{v} has len {l} - expected {VIAL_SIZE}'
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
        assert c == ITEM_COUNT, \
            f'item {i!r} appeared {c} times - expected {ITEM_COUNT}'
    return vials


def vial_complete(vial) -> bool:
    return vial[0] is not None \
        and vial[0] == vial[1] == vial[2] == vial[3]


def vial_topmost_item(vial: T_VIAL) -> T_ITEM | T_EMPTY:
    for v in vial:
        if v is not None:
            return v
    return None


def remove_left_nones(t: T) -> T:
    for i, val in enumerate(t):
        if val is not None:
            return t[i:]
    return type(t)()


def fill_left_nones(l: list) -> list:
    for _ in range(len(l), VIAL_SIZE):
        l.insert(0, None)
    return l


def vial_trans(f: T_VIAL, t: T_VIAL) -> tuple[T_VIAL, T_VIAL]:
    nf = remove_left_nones(list(f))
    nt = remove_left_nones(list(t))
    for _ in range(len(nt), VIAL_SIZE):
        if not nf or (nt and nt[0] != nf[0]):
            break
        nt.insert(0, nf.pop(0))
    return tuple(fill_left_nones(nf)), tuple(fill_left_nones(nt))


T_Step = tuple[int, int]
T_Solution = Iterable[T_Step, ...] | None


def _solve(vials: T_game_state, tried: set) -> T_Solution:
    print_vials(vials)
    completes = tuple(v for v, vial in enumerate(vials) if vial_complete(vial))
    if len(completes) >= VIAL_SIZE:
        return (-1, -1),
    not_full = tuple(v for v, vial in enumerate(vials) if vial[0] is None)
    tops = tuple(map(vial_topmost_item, vials))
    options: list[T_Step, ...] = []
    for nf in not_full:
        nf_top = tops[nf]
        if nf_top is None:  # empty
            for o, o_top in enumerate(tops):
                if o == nf:  # is same
                    continue
                if o in completes:
                    continue
                if o_top is not None:
                    options.append((o, nf))
        else:
            for o, o_top in enumerate(tops):
                if o == nf:  # is same
                    continue
                if o in completes:
                    continue
                if o_top == nf_top:
                    options.append((o, nf))
    for f, t in options:
        n_ = list(vials)
        n_[f], n_[t] = vial_trans(vials[f], vials[t])
        if n_[t] == vials[f] and n_[f] == vials[t]:
            continue  # no new state, just a swap
        vials_next: T_game_state = tuple(n_)
        del n_
        vials_next_h = hash(vials_next)
        if vials_next_h in tried:
            continue
        tried.add(vials_next_h)
        print(f'{f} --> {t}')
        if solved := _solve(vials_next, tried):
            return (f, t), solved
        print('< back <')
    return None


def print_vials(vials: T_game_state) -> None:
    print(*range(0, len(vials)), sep="|")
    print(*(v[0] or ' ' for v in vials), sep='|')
    print(*(v[1] or ' ' for v in vials), sep='|')
    print(*(v[2] or ' ' for v in vials), sep='|')
    print(*(v[3] or ' ' for v in vials), sep='|')
    print()


def solve(vials: Iterable[Iterable[T_ITEM | T_EMPTY]]) -> T_Solution:
    return _solve(make_vials(vials), set())
