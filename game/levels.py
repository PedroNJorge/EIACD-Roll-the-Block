from copy import deepcopy


'''
            "layout": [[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                       [-1,  0,  0,  0, -1, -1, -1, -1, -1, -1, -1, -1],
                       [-1,  0,  1,  0,  0,  0,  0, -1, -1, -1, -1, -1],
                       [-1,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1, -1],
                       [-1, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1],
                       [-1, -1, -1, -1, -1, -1,  0,  0,  7,  0,  0, -1],
                       [-1, -1, -1, -1, -1, -1, -1,  0,  0,  0, -1, -1],
                       [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],],
'''
level_menu = {
            1: "LEVEL1",
            2: "LEVEL2",
            3: "LEVEL3",
            4: "LEVEL4",
            5: "LEVEL5",
            6: "LEVEL6",
            7: "LEVEL7",
            8: "LEVEL8",
            9: "LEVEL9"
            }


reverse_level_menu = {value: key for key, value in level_menu.items()}


levels = {
        "LEVEL1": {
            "layout": [[5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
                       [5, 0, 0, 0, 5, 5, 5, 5, 5, 5, 5, 5],
                       [5, 0, 0, 0, 0, 0, 0, 5, 5, 5, 5, 5],
                       [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5],
                       [5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
                       [5, 5, 5, 5, 5, 5, 0, 0, 7, 0, 0, 5],
                       [5, 5, 5, 5, 5, 5, 5, 0, 0, 0, 5, 5],
                       [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],],
            "start": (2, 2),

            "goal": (5, 8)
            #maybe insert hidden path here
            },

        # "LEVEL2": []
        }

NUM_LEVELS = len(levels)


class Levels:
    def __init__(self, chosen_level):
        self.level_name = chosen_level
        self.level_data = levels[self.level_name]
        self.layout = deepcopy(self.level_data["layout"])
        self.start = self.level_data["start"]
        self.goal = self.level_data["goal"]

    def get_tiletype(self, position):
        match levels[self.level_name]["layout"][position[0]][position[1]]:
            case -2:
                return "HIDDEN_PATH"
            case -1 | 5:
                return "VOID"
            case 0:
                return "FLOOR"
            case 1:
                return "BLOCK_UPRIGHT"
            case 2:
                return "BLOCK_PRONE"
            case 3:
                return "GLASS_FLOOR"
            case 4:
                return "DEACTIVE_BUTTON"
            case 5:
                return "ACTIVE_BUTTON"
            case 7:
                return "GOAL"

    def is_goal(self, position):
        return position == self.goal

    def switch_level(self):
        level_num = reverse_level_menu[self.level_name]
        self.level_name = level_menu[(level_num + 1) % NUM_LEVELS + 1]
        self.level_data = levels[self.level_name]
        self.layout = deepcopy(self.level_data["layout"])
        self.start = self.level_data["start"]
        self.goal = self.level_data["goal"]

        return self.level_name
