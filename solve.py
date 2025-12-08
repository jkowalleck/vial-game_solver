from src import EMPTY_VIAL, validate, solve

vials = [
    'AADF',
    'SSDF',
    ['A', 'S', 'D', 'F'],
    'ASDF',
    EMPTY_VIAL,
    EMPTY_VIAL,
    EMPTY_VIAL,
    EMPTY_VIAL,
]

validate(vials)
solve(vials)
