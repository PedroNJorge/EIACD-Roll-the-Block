class Block:
    def __init__(self, x, y):
        '''
        self.x -> gives the x coordinate
        self.y -> gives the y coordinate
        self.orientation -> gives the orientation
                            ("upright", "vertical", "horizontal")
        '''
        self.x = x
        self.y = y
        self.orientation = "upright"

    def move(self, direction):
        match direction:
            case "up":
                self.y -= 1
            case "down":
                self.y += 1
            case "left":
                self.x -= 1
            case "right":
                self.x += 1

        self.update_orientation(direction)

    def update_orientation(self, direction):
        pass
