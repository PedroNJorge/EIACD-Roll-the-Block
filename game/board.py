from copy import deepcopy
from pprint import pprint
from .levels import Levels, levels


class Board:
    def __init__(self, level_name):
        self.level = Levels(level_name)
        self.button_is_active = 0

    def __str__(self):
        pprint(self.level.layout)
        return ""

    def __eq__(self, other):
        if not isinstance(other, Board):
            return False
        return tuple(map(tuple, self.level.layout)) == tuple(map(tuple, other.level.layout))

    def __hash__(self):
        return hash(tuple(map(tuple, self.level.layout)))

    def is_goal(self, position):
        return self.level.is_goal(position)

    def is_fatal(self, block):
        position = ((block.x1, block.y1), (block.x2, block.y2))
        tiles_list = list(map(self.level.get_tiletype, position))
        if "VOID" in tiles_list:
            return True
        elif "HIDDEN_PATH" in tiles_list and not self.button_is_active:
            return True
        elif tiles_list.count("BUTTON") == 2:
            self.button_is_active = not self.button_is_active
        elif block.orientation == "upright" and tiles_list.count("GLASS_FLOOR") == 2:
            return True
        return False

    def refresh_layout(self, block):
        self.level.layout = deepcopy(levels[self.level.level_name]["layout"])

        if self.level.hidden_path:
            if self.button_is_active:
                for x, y in self.level.hidden_path:
                    self.level.layout[x][y] = 0
            else:
                for x, y in self.level.hidden_path:
                    '''
                    Mudar para -1 ("VOID")
                    '''
                    self.level.layout[x][y] = 5

        if block.orientation == "upright":
            self.level.layout[block.x1][block.y1] = 1
        else:
            self.level.layout[block.x1][block.y1] = 2
            self.level.layout[block.x2][block.y2] = 2

        return self.level.layout

    def switch_level(self):
        next_level = self.level.switch_level()
        self.level = Levels(next_level)
