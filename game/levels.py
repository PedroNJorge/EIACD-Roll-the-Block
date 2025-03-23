levels = {
        "LEVEL1": {
            "layout": [[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                       [-1,  0,  0,  0, -1, -1, -1, -1, -1, -1, -1, -1],
                       [-1,  0,  1,  0,  0,  0,  0, -1, -1, -1, -1, -1],
                       [-1,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1, -1],
                       [-1, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1],
                       [-1, -1, -1, -1, -1, -1,  0,  0,  7,  0,  0, -1],
                       [-1, -1, -1, -1, -1, -1, -1,  0,  0,  0, -1, -1],
                       [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],],

            "start": (2, 2),

            "goal": (4, 7)
            },

        "LEVEL2": []}


class Levels:
    def __init__(self, chosen_level):
        self.level_data = levels[chosen_level]
        self.layout = self.level_data["layout"]
        self.start = self.level_data["start"]
        self.goal = self.level_data["goal"]

    def get_tiletype(self, position):
        pass

    def is_goal(self, position):
        return position == self.goal
