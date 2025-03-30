from copy import deepcopy
from pprint import pprint
from .levels import Levels, levels


class Board:
    def __init__(self, level_name):
        self.level = Levels(level_name)

    def __str__(self):
        return self.level.layout

    def __eq__(self, other):
        if not isinstance(other, Board):
            return False
        return tuple(map(tuple, self.level.layout)) == tuple(map(tuple, other.level.layout))

    def __hash__(self):
        return hash(tuple(map(tuple, self.level.layout)))

    def is_goal(self, position):
        return self.level.is_goal(position)

    def is_fatal(self, position):
        if "VOID" in map(self.level.get_tiletype, position):
            return True

    def refresh_layout(self, block):
        self.level.layout = deepcopy(levels[self.level.level_name]["layout"])

        if block.orientation == "upright":
            self.level.layout[block.x1][block.y1] = 1
        else:
            self.level.layout[block.x1][block.y1] = 2
            self.level.layout[block.x2][block.y2] = 2

        return self.level.layout

    def switch_level(self):
        next_level = self.level.switch_level()
        self.level = Levels(next_level)
