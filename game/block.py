class Block:
    def __init__(self, x, y):
        # make x2, y2
        # if h or v
        self.x = x
        self.y = y
        self.orientation = "upright"    # "upright", "vertical", "horizontal"

    def move(self, direction):
        # take max(x1, x2)
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
        match(self.orientation):
            case "upright":
                match(direction):
                    case "up" | "down":
                        self.orientation = "vertical"

                    case "left" | "right":
                        self.orientation = "horizontal"

            case "vertical":
                match(direction):
                    case "up" | "down":
                        self.orientation = "upright"

            case "horizontal":
                match(direction):
                    case "left" | "right":
                        self.orientation = "upright"
