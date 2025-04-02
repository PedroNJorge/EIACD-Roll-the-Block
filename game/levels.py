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
            0: "LEVEL1",
            1: "LEVEL2",
            2: "LEVEL3",
            3: "LEVEL4",
            4: "LEVEL5",
            5: "LEVEL6",
            6: "LEVEL7",
            7: "LEVEL8",
            8: "LEVEL9"
            }


reverse_level_menu = {value: key for key, value in level_menu.items()}


levels = {
        "LEVEL1": {
            "layout": [[5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
                       [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
                       [5, 5, 0, 0, 0, 5, 5, 5, 5, 5, 5, 5, 5, 5],
                       [5, 5, 0, 0, 0, 0, 0, 0, 5, 5, 5, 5, 5, 5],
                       [5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 5],
                       [5, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5],
                       [5, 5, 5, 5, 5, 5, 5, 0, 0, 7, 0, 0, 5, 5],
                       [5, 5, 5, 5, 5, 5, 5, 5, 0, 0, 0, 5, 5, 5],
                       [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
                       [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]],
            "start": (3, 3),

            "goal": (6, 9),

            "button": None,

            "hidden_path": None
            },

        "LEVEL2": {
            "layout": [[5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
                       [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
                       [5, 5, 5, 5, 5, 3, 3, 3, 3, 3, 3, 3, 3, 5, 5, 5, 5, 5, 5],
                       [5, 5, 5, 5, 5, 3, 3, 3, 3, 3, 3, 3, 3, 5, 5, 5, 5, 5, 5],
                       [5, 5, 0, 0, 0, 0, 5, 5, 5, 5, 5, 5, 0, 0, 0, 5, 5, 5, 5],
                       [5, 5, 0, 0, 0, 5, 5, 5, 5, 5, 5, 5, 5, 0, 0, 5, 5, 5, 5],
                       [5, 5, 0, 0, 0, 5, 5, 5, 5, 5, 5, 5, 5, 0, 0, 5, 5, 5, 5],
                       [5, 5, 0, 0, 0, 5, 5, 5, 0, 0, 0, 0, 3, 3, 3, 3, 3, 5, 5],
                       [5, 5, 0, 0, 0, 5, 5, 5, 0, 0, 0, 0, 3, 3, 3, 3, 3, 5, 5],
                       [5, 5, 5, 5, 5, 5, 5, 5, 0, 7, 0, 5, 5, 3, 3, 0, 3, 5, 5],
                       [5, 5, 5, 5, 5, 5, 5, 5, 0, 0, 0, 5, 5, 3, 3, 3, 3, 5, 5],
                       [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
                       [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]],

            "start": (7, 3),

            "goal": (9, 9),

            "button": None,

            "hidden_path": None
            },

        "LEVEL3": {
            "layout": [[5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
                       [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
                       [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 0, 0, 0, 0, 5, 5, 5, 5, 5, 5],
                       [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 0, 0, 0, 0, 5, 5, 5, 5, 5, 5],
                       [5, 5, 0, 0, 0, 5, 5, 5, 5, 5, 0, 5, 5, 0, 0, 0, 0, 5, 5, 5],
                       [5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 5, 0, 7, 0, 5, 5, 5],
                       [5, 5, 0, 0, 0, 5, 5, 5, 5, 0, 0, 4, 5, 5, 0, 0, 0, 5, 5, 5],
                       [5, 5, 0, 0, 0, 5, 5, 5, 5, 0, 0, 0, 5, 5, 0, 0, 0, 5, 5, 5],
                       [5, 5, 5, 0, 0,-2, 5, 5, 5, 0, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
                       [5, 5, 5, 5, 0, 0, 0, 0, 0, 0, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
                       [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
                       [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
                       [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]],

            "start": (5, 3),

            "goal": (5, 15),

            "button": (6, 11),

            "hidden_path": [(8, 5)]
            },

        "LEVEL4": {
            "layout": [[5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
                       [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
                       [5, 5, 5, 5, 5, 3, 3, 3, 3, 3, 3, 3, 5, 5, 5, 5, 5, 5],
                       [5, 5, 5, 5, 5, 3, 3, 3, 3, 3, 3, 3, 5, 5, 5, 5, 5, 5],
                       [5, 5, 0, 0, 0, 0, 5, 5, 5, 5, 5, 0, 0, 0, 5, 5, 5, 5],
                       [5, 5, 0, 0, 0, 5, 5, 5, 5, 5, 5, 5, 0, 0, 5, 5, 5, 5],
                       [5, 5, 0, 0, 0, 5, 5, 5, 5, 5, 5, 5, 0, 0, 5, 5, 5, 5],
                       [5, 5, 0, 0, 0, 5, 5, 0, 0, 0, 0, 3, 3, 3, 3, 3, 5, 5],
                       [5, 5, 0, 0, 0, 5, 5, 0, 0, 0, 0, 3, 3, 3, 3, 3, 5, 5],
                       [5, 5, 5, 5, 5, 5, 5, 0, 7, 0, 5, 5, 3, 3, 0, 3, 5, 5],
                       [5, 5, 5, 5, 5, 5, 5, 0, 0, 0, 5, 5, 3, 3, 3, 3, 5, 5],
                       [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
                       [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]],
                    
            "start": (7, 3),

            "goal": (9, 8),

            "button": None,

            "hidden_path": None
            },

        "LEVEL5": {
            "layout": [[5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
                       [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
                       [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 0, 0, 0, 0, 5, 5],
                       [5, 5, 5, 0, 0, 0, 0, -2, -2, 0, 4, 0, 0, 0, 0, 0, 0, 5],
                       [5, 5, 5, 0, 0, 0, 0, 5, 5, 5, 5, 5, 5, 5, 0, 0, 0, 5],
                       [5, 5, 5, 0, 0, 4, 0, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
                       [5, 5, 5, 0, 0, 0, 0, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
                       [5, 5, 5, 5, 5, 0, 0, 0, 4, 5, -2, -2, 0, 0, 0, 5, 5, 5],
                       [5, 5, 0, 0, 0, 5, 5, 5, 5, 5, 5, 5, 0, 0, 0, 0, 4, 5],
                       [5, 5, 0, 7, 0, 0, 0, -2, -2, 0, 0, 0, 0, 0, 0, 5, 5, 5],
                       [5, 5, 0, 0, 0, 0, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
                       [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
                       [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]],

            "start": (3, 15),

            "goal": (9, 3),

            "button": [(3, 10), (5, 5), (7, 8), (8, 16)],

            "hidden_path": [(3, 7), (3, 8), (7, 10), (7, 11), (9, 7), (9, 8)]
            },
                       
        "LEVEL6": {
            "layout": [[5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
                       [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
                       [5, 5, 5, 5, 5, 5, 5, 0, 0, 0, 0, 0, 0, 5, 5, 5, 5, 5, 5],
                       [5, 5, 5, 5, 5, 5, 5, 0, 5, 5, 0, 0, 0, 5, 5, 5, 5, 5, 5],
                       [5, 5, 5, 5, 5, 5, 5, 0, 5, 5, 0, 0, 0, 0, 0, 5, 5, 5, 5],
                       [5, 5, 0, 0, 0, 0, 0, 0, 5, 5, 5, 5, 5, 0, 0, 0, 0, 5, 5],
                       [5, 5, 5, 5, 5, 5, 0, 0, 0, 5, 5, 5, 5, 0, 0, 7, 0, 5, 5],
                       [5, 5, 5, 5, 5, 5, 0, 0, 0, 5, 5, 5, 5, 5, 0, 0, 0, 5, 5],
                       [5, 5, 5, 5, 5, 5, 5, 5, 0, 5, 5, 0, 0, 5, 5, 5, 5, 5, 5],
                       [5, 5, 5, 5, 5, 5, 5, 5, 0, 0, 0, 0, 0, 5, 5, 5, 5, 5, 5],
                       [5, 5, 5, 5, 5, 5, 5, 5, 0, 0, 0, 0, 0, 5, 5, 5, 5, 5, 5],
                       [5, 5, 5, 5, 5, 5, 5, 5, 5, 0, 0, 0, 5, 5, 5, 5, 5, 5, 5],
                       [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
                       [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]],
                       
            "start": (2, 5),

            "goal": (15, 6),

            "button": None,

            "hidden_path": None
            },

        "LEVEL7": {
            "layout": [[5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
                       [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
                       [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 0, 0, 0, 0, 5, 5, 5, 5, 5],
                       [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 0, 0, 0, 0, 5, 5, 5, 5, 5],
                       [5, 5, 0, 0, 0, 5, 5, 5, 5, 5, 0, 5, 5, 0, 0, 0, 0, 5, 5],
                       [5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 5, 0, 7, 0, 5, 5],
                       [5, 5, 0, 0, 0, 5, 5, 5, 5, 0, 0, 4, -2, -2, 0, 0, 0, 5, 5],
                       [5, 5, 0, 0, 0, 5, 5, 5, 5, 0, 0, 0, 5, 5, 0, 0, 0, 5, 5],
                       [5, 5, 5, 0, 0, 5, 5, 5, 5, 0, 5, 5, 5, 5, 5, 5, 5, 5, 5],
                       [5, 5, 5, 5, 0, 0, 0, 0, 0, 0, 5, 5, 5, 5, 5, 5, 5, 5, 5],
                       [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
                       [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]],
                       
            "start": (5, 3),

            "goal": (5, 15), 

            "button": (6, 11),

            "hidden_path": [(6, 12), (6, 13)]
            },
                       
       "LEVEL8": {
            "layout": [[5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
                       [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
                       [5, 5, 5, 0, 0, 0, -2, 0, 0, 0, 0, 0, 0, 5, 5],
                       [5, 5, 5, 0, 7, 0, -2, 5, 5, 5, 5, 5, 5, 5, 5],
                       [5, 5, 5, 0, 0, 0, 5, 5, 5, 5, 5, 5, 5, 5, 5],
                       [5, 5, 5, 0, 5, 5, 5, 0, 0, 0, 0, 0, 0, 5, 5],
                       [5, 5, 5, 0, 5, 5, 5, 0, 0, 5, 5, 0, 0, 5, 5],
                       [5, 5, 0, 0, 0, 0, 0, 0, 0, 5, 5, 0, 0, 0, 5],
                       [5, 5, 5, 5, 5, 5, 5, 0, 4, 5, 5, 5, 5, 0, 5],
                       [5, 5, 5, 5, 5, 5, 5, 0, 0, 0, 0, 5, 5, 0, 5],
                       [5, 5, 5, 5, 5, 5, 5, 0, 0, 0, 0, 0, 0, 0, 5],
                       [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 0, 0, 0, 5, 5],
                       [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
                       [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]],
                       
            "start": (7, 2),

            "goal": (3, 4), 

            "button": (8, 8),

            "hidden_path": [(2, 6), (3, 6)]
            },
            
       "LEVEL9": {
            "layout": [[5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
                       [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
                       [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 5, 5],
                       [5, 5, 5, 5, 5, 5, 5, 0, 0, 0, 5, 5, 0, 0, 0, 5, 5],
                       [5, 5, 5, 5, 5, 5, 5, 0, 4, 0, 0, 0, 0, 0, -2, 5, 5],
                       [5, 5, 5, 5, 5, 0, 0, 0, 0, 0, 5, 5, 0, 0, 5, 5, 5],
                       [5, 5, 5, 5, 5, 0, 7, 0, -2, 5, 5, 5, 0, 0, 5, 5, 5],
                       [5, 5, 0, 0, 0, 0, 0, 0, 5, 5, 5, 0, 0, 0, 0, 5, 5],
                       [5, 5, 0, 0, 0, 0, 5, 5, 5, 5, 5, 0, 0, 0, 0, 5, 5],
                       [5, 5, 0, 0, 0, 0, 5, 5, 0, 0, 0, 0, 0, 5, 5, 5, 5],
                       [5, 5, 5, 5, 5, 5, 5, 0, 0, 0, 5, 5, 5, 5, 5, 5, 5],
                       [5, 5, 5, 5, 5, 5, 5, 0, 0, 0, 5, 5, 5, 5, 5, 5, 5],
                       [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
                       [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]],
                       
            "start": (8, 4),

            "goal":  (6, 6),

            "button": [(4, 8), (2, 14)],

            "hidden_path": [(6, 8), (4, 14)],
            },
                       
NUM_LEVELS = len(levels)


class Levels:
    def __init__(self, chosen_level):
        self.level_name = chosen_level
        self.level_data = levels[self.level_name]

        self.layout = deepcopy(self.level_data["layout"])
        self.start = self.level_data["start"]
        self.goal = self.level_data["goal"]
        self.button = self.level_data["button"]
        self.hidden_path = self.level_data["hidden_path"]

        self.width = len(self.layout[0])
        self.height = len(self.layout)

    def get_tiletype(self, position):
        x, y = position
        if not (0 <= x <= self.height and 0 <= y <= self.width):
            return "VOID"

        match levels[self.level_name]["layout"][x][y]:
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
                return "BUTTON"
            case 5:
                return "ACTIVE_BUTTON"
            case 7:
                return "GOAL"

    def is_goal(self, position):
        return position == self.goal

    def switch_level(self):
        level_num = reverse_level_menu[self.level_name]
        self.level_name = level_menu[(level_num + 1) % NUM_LEVELS]
        self.level_data = levels[self.level_name]
        self.layout = deepcopy(self.level_data["layout"])
        self.start = self.level_data["start"]
        self.goal = self.level_data["goal"]

        return self.level_name
