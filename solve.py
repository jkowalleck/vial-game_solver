from src import EMPTY_VIAL, solve

vials = (
    '0178',
    '1590',
    '0186',
    '2576',
    '2549',
    '3483',
    '4781',
    '5290',
    '6439',
    '3276',
    EMPTY_VIAL,
    EMPTY_VIAL,
)

solved = solve(vials)
print('solution', solved)
