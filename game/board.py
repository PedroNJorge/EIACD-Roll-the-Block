from copy import deepcopy
from .levels import Levels, levels


class Board:
    def __init__(self, level_name):
        self.level = Levels(level_name)
        self.width = len(self.level.layout[0])
        self.height = len(self.level.layout)

    def is_goal(self, position):
        return self.level.is_goal(position)

    def is_fatal(self, position):
        print(list(map(self.level.get_tiletype, position)))
        if "VOID" in map(self.level.get_tiletype, position):
            return True

    def refresh_layout(self, block):
        self.level.layout = deepcopy(levels[self.level.level_name]["layout"])

        if block.orientation == "upright":
            self.level.layout[block.x1][block.y1] = 1
        else:
            self.level.layout[block.x1][block.y1] = 2
            self.level.layout[block.x2][block.y2] = 2

    def switch_level(self):
        next_level = self.level.switch_level()
        self.level = Levels(next_level)
