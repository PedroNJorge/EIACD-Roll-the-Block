from .levels import Levels


class Board:
    def __init__(self, level_name):
        self.level = Levels(level_name)
        self.width = len(self.level.layout[0])
        self.height = len(self.level.layout)

    def is_goal(self, position):
        return self.level.is_goal(position)

    def is_fatal(self, position):
        pass
