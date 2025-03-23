class Block:
    def __init__(self, x, y):
        # x1 <= x2 & y1 <= y2, always
        self.x1 = self.x2 = x
        self.y1 = self.y2 = y
        self.orientation = "upright"    # "upright", "vertical", "horizontal"
        self.move_counter = 0

    def move(self, direction):
        self.move_counter += 1
        match self.orientation:
            case "upright":
                match direction:
                    case "up":
                        self.x1 -= 2
                        self.x2 -= 1
                    case "down":
                        self.x1 += 1
                        self.x2 += 2
                    case "left":
                        self.y1 -= 2
                        self.y2 -= 1
                    case "right":
                        self.y1 += 1
                        self.y2 += 2

            case "vertical":
                match direction:
                    case "up":
                        self.x1 = self.x2 = min(self.x1, self.x2) - 1
                    case "down":
                        self.x1 = self.x2 = max(self.x1, self.x2) + 1
                    case "left":
                        self.y1 -= 1
                        self.y2 -= 1
                    case "right":
                        self.y1 += 1
                        self.y2 += 1

            case "horizontal":
                match direction:
                    case "up":
                        self.x1 -= 1
                        self.x2 -= 1
                    case "down":
                        self.x1 += 1
                        self.x2 += 1
                    case "left":
                        self.y1 = self.y2 = min(self.y1, self.y2) - 1
                    case "right":
                        self.y1 = self.y2 = max(self.y1, self.y2) + 1

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
