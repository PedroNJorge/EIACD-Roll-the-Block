import pygame


class InputHandler:
    def __init__(self, block, game_logic):
        self.block = block
        self.game_logic = game_logic

    def handle_events(self):
        for event in pygame.event.get():
            match(event.type):
                case pygame.QUIT:
                    return False    # used to update run in main.py

        return True

    def handle_keyboard(self, event):
        match(event.key):
            case pygame.K_UP:
                pass

        self.game_logic.update()
