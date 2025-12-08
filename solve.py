from src import EMPTY_VIAL, validate, solve

vials = [
    'ASDF',
    'ASDF',
    ['A', 'S', 'D', 'F'],
    'ASDF',
    EMPTY_VIAL,
    EMPTY_VIAL,
    EMPTY_VIAL,
    EMPTY_VIAL,
]

validate(vials)
solve(vials)
