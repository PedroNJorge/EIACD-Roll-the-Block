from enum import Enum


class LevelType(Enum):
    LEVEL1 = 1
    LEVEL2 = 2
    LEVEL3 = 3
    LEVEL4 = 4
    LEVEL5 = 5
    LEVEL6 = 6
    LEVEL7 = 7
    LEVEL8 = 8
    LEVEL9 = 9


class TileType(Enum):
    HIDDEN_PATH = -2
    VOID = -1
    FLOOR = 0
    BLOCK_UPRIGHT = 1
    BLOCK_PRONE = 2
    GLASS_FLOOR = 3
    DEACTIVE_BUTTON = 4
    ACTIVE_BUTTON = 5
    GOAL = 7


class Colors(Enum):
    pass
