import enum

from src import EMPTY_VIAL, solve


@enum.unique
class C(enum.Enum):
    GREEN = enum.auto()
    ROYAL = enum.auto()
    BROWN = enum.auto()
    BLUE = enum.auto()
    LULLABY = enum.auto()
    YELLOW = enum.auto()
    RED = enum.auto()
    LIGHTBLUE = enum.auto()
    LIGHTGREEN = enum.auto()
    PINK = enum.auto()


LEVEL5 = (
    (C.GREEN, C.ROYAL, C.BROWN, C.BLUE),
    (C.ROYAL, C.LULLABY, C.YELLOW, C.GREEN),
    (C.GREEN, C.ROYAL, C.BLUE, C.RED),
    (C.LIGHTBLUE, C.LULLABY, C.BROWN, C.RED),
    (C.LIGHTBLUE, C.LULLABY, C.PINK, C.YELLOW),
    (C.LIGHTGREEN, C.PINK, C.BLUE, C.LIGHTGREEN),

    (C.PINK, C.BROWN, C.BLUE, C.ROYAL),
    (C.LULLABY, C.LIGHTBLUE, C.YELLOW, C.GREEN),
    (C.RED, C.PINK, C.LIGHTGREEN, C.YELLOW),
    (C.LIGHTGREEN, C.LIGHTBLUE, C.BROWN, C.RED),
    EMPTY_VIAL,
    EMPTY_VIAL,
)

print('solution', solve(LEVEL5))
