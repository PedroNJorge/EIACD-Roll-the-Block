import pygame
import sys
from game.block import Block
from game.board import Board
from game.game_logic import GameLogic
from game.input_handler import InputHandler

#Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TILE_SIZE = 50
FPS = 60

#Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (100, 100, 100)
BLUE = (51, 51, 255) #grid
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255) #new path discovered by button
PURPLE = (128, 0, 128) #button
TRANSPARENT_BLUE = (0, 0, 255, 128) #glass floor
DARK_GRAY = (50, 50, 50)
LIGHT_BLUE = (173, 216, 230) #sky
HOT_PINK = (255, 0, 127) #block
WHITE_CLOUD = (204, 255, 204) #clouds

#Game states
MAIN_MENU=0
RULES = 1
LEVEL_SELECT = 2
PLAYING = 3
GAME_OVER = 4
LEVEL_COMPLETE = 5

#All buttons shape and color
class Button:
        def __init__(self, x, y, width, height, text, color, hover_color, text_color=BLACK):
            self.rect = pygame.Rect(x, y, width, height)
            self.text = text
            self.color = color
            self.hover_color = hover_color
            self.text_color = text_color
            self.is_hovered = False

        def draw(self, screen):
            color = self.hover_color if self.is_hovered else self.color
            pygame.draw.rect(screen, color, self.rect, border_radius=10)
            pygame.draw.rect(screen, BLACK, self.rect, 2, border_radius=10)

            font = pygame.font.Font(None, 32)
            text_surface = font.render(self.text, True, self.text_color)
            text_rect = text_surface.get_rect(center=self.rect.center)
            screen.blit(text_surface, text_rect)

        def update(self, mouse_pos):
            self.is_hovered = self.rect.collidepoint(mouse_pos)

        def is_clicked(self, mouse_pos, mouse_click):
            return (self.rect.collidepoint(mouse_pos) and mouse_click)


# Running the game itself
class Renderer:
        def __init__(self, block, board, game_logic, input_handler):
            self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
            pygame.display.set_caption("Roll the Block!")
            self.clock = pygame.time.Clock()
            self.game_state = MAIN_MENU
            self.block = block
            self.board = board
            self.game_logic = game_logic
            self.input_handler = input_handler
            self.init_buttons()

            self.animation_active = False
            self.animation_direction = None
            self.animation_progress = 0
            self.animation_speed = 0.1
            self.old_block_position = None
            self.target_block_position = None

        def draw(self):
            #self.screen.fill(LIGHT_BLUE)
            self.camera_offset_x = 0
            self.camera_offset_y = 0

            self.transition_alpha = 0
            self.transition_state = None

        def init_buttons(self):
            center_x = SCREEN_WIDTH // 2
            #Main menu
            self.play_button = Button(center_x - 100, 200, 200, 50, "Play", WHITE_CLOUD, (204, 255, 204))
            self.rules_button = Button(center_x - 100, 270, 200, 50, "Rules", WHITE_CLOUD, (204, 225, 204))
            self.quit_button = Button(center_x -100, 340, 200, 50, "Quit", WHITE_CLOUD, (204, 225, 204))
	    #Back from rules
            self.back_button = Button(center_x - 100, 500, 200, 50, "Back", WHITE_CLOUD, (204, 255, 204))
	    #Level select buttons
            self.level_buttons = []
            for i in range(3):
                    for j in range(3):
                            level_num = i * 3 + j + 1
                            x = 150 + j * 175
                            y = 150 + i * 120
                            self.level_buttons.append(Button(x, y, 125, 80, f"Level {level_num}", CYAN, (100, 255, 255)))
	    #Game buttons
            self.menu_button = Button(SCREEN_WIDTH - 120, 20, 100, 40, "Menu", WHITE_CLOUD, (204, 255, 204))
            self.restart_button = Button(SCREEN_WIDTH - 120, 70, 100, 40, "Restart", WHITE_CLOUD, (204, 255, 204))

        def initialize_level(self, level_name):
            self.current_level = level_name
            self.board = Board(level_name)
            x, y = self.board.level.start
            self.block = Block(x, y)
            self.game_logic = GameLogic(self.block, self.board)
            self.input_handler = InputHandler(self.block, self.board, self.game_logic)

	    #Update the layout with the initial block position
            self.board.refresh_layout(self.block)

            self.calculate_camera_offset()

        def calculate_camera_offset(self):
            level_pixel_width = len(self.board.level.layout[0]) * TILE_SIZE
            level_pixel_height = len(self.board.level.layout) * TILE_SIZE
            self.camera_offset_x = (SCREEN_WIDTH - level_pixel_width) // 2
            self.camera_offset_y = (SCREEN_HEIGHT - level_pixel_height) // 2

        def handle_events(self):
            mouse_pos = pygame.mouse.get_pos()
            mouse_click = False
            quit_requested = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_click = True

                if self.game_state == PLAYING and not self.animation_active:
                    if event.type == pygame.KEYDOWN:
                            direction = None
                            if event.key == pygame.K_w:
                                direction = "up"
                            elif event.key == pygame.K_s:
                                direction = "down"
                            elif event.key == pygame.K_a:
                                direction = "left"
                            elif event.key == pygame.K_d:
                                direction = "right"

                            if direction:
                                self.start_animation(direction)

            if mouse_click:
                if self.game_state == MAIN_MENU:
                    quit_requested = self.handle_main_menu(mouse_pos)
                elif self.game_state == RULES:
                    self.handle_rules_screen(mouse_pos, True)
                elif self.game_state == LEVEL_SELECT:
                    self.handle_level_select(mouse_pos)
                elif self.game_state == PLAYING:
                    self.handle_playing(mouse_pos)
                elif self.game_state == GAME_OVER:
                    self.handle_game_over(mouse_pos)
                elif self.game_state == LEVEL_COMPLETE:
                    self.handle_level_complete(mouse_pos)

            return not quit_requested

        def handle_main_menu(self, mouse_pos):
            self.play_button.update(mouse_pos)
            self.rules_button.update(mouse_pos)
            self.quit_button.update(mouse_pos)

            if self.play_button.is_clicked(mouse_pos, True):
                self.game_state = LEVEL_SELECT
                return False
            elif self.rules_button.is_clicked(mouse_pos, True):
                self.game_state = RULES
                return False
            elif self.quit_button.is_clicked(mouse_pos, mouse_click):
                return True

            return False

        def handle_rules_screen(self, mouse_pos, mouse_click):
            self.back_button.update(mouse_pos)

            if self.back_button.is_clicked(mouse_pos, mouse_click):
                self.game_state = MAIN_MENU

            return True

        def handle_level_select(self, mouse_pos):
            self.back_button.update(mouse_pos)

            if self.back_button.is_clicked(mouse_pos, True):
                self.game_state = MAIN_MENU
                return True

            for i, button in enumerate(self.level_buttons):
                button.update(mouse_pos)
                if button.is_clicked(mouse_pos, True):
                    level_name = f"LEVEL{i+1}"
                    self.initialize_level(level_name)
                    self.game_state = PLAYING
                    return True

            return True

        def handle_playing(self, mouse_pos, mouse_click):
            self.menu_button.update(mouse_pos)
            self.restart_button.update(mouse_pos)

            if self.menu_button.is_clicked(mouse_pos, mouse_click):
                self.game_state = MAIN_MENU
            elif self.restart_button.is_clicked(mouse_pos, mouse_click):
                self.initialize_level(self.current_level)

            if self.game_logic.game_over:
                self.game_state = GAME_OVER
            elif self.game_logic.level_completed:
                self.game_state = LEVEL_COMPLETE

            return True

        def handle_game_over(self, mouse_pos, mouse_click):
            self.restart_button.update(mouse_pos)
            self.menu_button.update(mouse_pos)

            if self.restart_button.is_clicked(mouse_pos, mouse_click):
                self.initialize_level(self.current_level)
                self.game_state = PLAYING
            elif self.menu_button.is_clicked(mouse_pos, mouse_click):
                self.game_state = MAIN_MENU

            return True

        def handle_level_complete(self, mouse_pos, mouse_click):
            self.menu_button.update(mouse_pos)

            next_level_button.update = Button(SCREEN_WIDTH // 2 - 100, 300, 200, 50, "Next Level", BLUE, (51, 51, 255))
            next_level_button.update(mouse_pos)

            if next_level_button.is_clicked(mouse_pos, mouse_click):
                #Switching levels in case of a win
                self.board.switch_level()
                next_level = self.board.level.level_name
                self.initialize_level(next_level)
                self.game_state = PLAYING
            elif self.menu_button.is_clicked(mouse_pos, mouse_click):
                self.game_state = MAIN_MENU

            return True

        def start_animation(self, direction):
            self.animation_active = True
            self.animation_direction = direction
            self.animation_progress = 0
            self.old_block_position = (self.block.x1, self.block.y1, self.block.x2, self.block.y2)

            #Temporary block used to calculate following moves
            temp_block = Block(self.block.x1, self.block.y1)
            temp_block.x2 = self.block.x2
            temp_block.y2 = self.block.y2
            temp_block.orientation = self.block.orientation
            temp_block.move(direction)

            self.target_block_position = (temp_block.x1, temp_block.y1, temp_block.x2, temp_block.y2)

        def update_animation(self):
            if not self.animation_active:
                return

            self.animation_progress += self.animation_speed

            if self.animation_progress >= 1:
                self.animation_active = False
                self.block.move(self.animation_direction)
                self.board.refresh_layout(self.block)
                self.game_logic.update()

        def draw(self):
            self.screen.fill(LIGHT_BLUE)

            if self.game_state == MAIN_MENU:
                self.draw_main_menu()
            elif self.game_state == RULES:
                self.draw_rules_screen()
            elif self.game_state == LEVEL_SELECT:
                self.draw_level_select()
            elif self.game_state == PLAYING:
                self.draw_level()
            elif self.game_state == GAME_OVER:
                self.draw_level()
                self.draw_game_over()
            elif self.game_state == LEVEL_COMPLETE:
                self.draw_level()
                self.draw_level_complete()

            pygame.display.flip()

        def draw_main_menu(self):
        #Draw title
            font = pygame.font.Font(None, 72)
            title = font.render("Roll the Block", True, BLUE)
            title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, 100))
            self.screen.blit(title, title_rect)
        #Draw buttons
            self.play_button.draw(self.screen)
            self.rules_button.draw(self.screen)
            self.quit_button.draw(self.screen)

        def draw_rules_screen(self):
            #Draw title
            font = pygame.font.Font(None, 40)
            title = font.render("Game Rules", True, BLUE)
            title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, 50))
            self.screen.blit(title, title_rect)

            rules = [
                "Roll the Block é um jogo de quebra-cabeças, no qual o jogador controla"
                " os movimentos de um bloco, que se move por um tabuleiro, com o objetivo"
                " de o colocar num local específico.",
                "Movimentos das teclas:"
                " -W: Cima",
                " -S: Baixo",
                " -A: Esquerda",
                " -D: Direita",
                "Posições do bloco:",
                " -Bloco de pé: pode estar no chão regular,",
                " mas parte o chão de vidro",
                " -Bloco na horizontal/vertical: pode estar tanto no",
                " chão regular como em chão de vidro",
                "Elementos do jogo:",
                " -Chão azul: Chão regular",
                " -Chão verde: Objetivo",
                " -Botão amarelo: Ativa caminhos escondidos quando o bloco",
                " o pressiona",
                " -Espaço preto: Se o bloco cair aqui, o jogo acaba",
                " -Chão de vidro: O bloco só consegue andar neste chão se",
                " estiver na horizontal ou na vertical"
            ]

            font = pygame.font.Font(None, 24)
            for i, line in enumerate(rules):
                text = font.render(line, True, BLACK)
                self.screen.blit(text, (100, 120 + i * 25))

            #Draw back button
            self.back_button.draw(self.screen)

        def draw_level_select(self):
            #Draw title
            font = pygame.font.Font(None, 48)
            title = font.render("Select Level", True, BLUE)
            title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, 60))
            self.screen.blit(title, title_rect)

            #Draw level buttons
            for button in self.level_buttons:
                button.draw(self.screen)

            #Draw back button
            self.back_button.draw(self.screen)

        def draw_level(self):
            #Draw the game grid
            layout = self.board.level.layout

            for i in range (len(layout)):
                for j in range (len(layout[0])):
                    x = j * TILE_SIZE + self.camera_offset_x
                    y = i * TILE_SIZE + self.camera_offset_y
                    tile_type = layout[i][j]

                    #Drawing different types of tiles
                    if tile_type == 5: #Void
                        pygame.draw.rect(self.screen, BLACK, (x,y, TILE_SIZE, TILE_SIZE))
                    elif tile_type == 0: #Regular floor
                        pygame.draw.rect(self.screen, BLUE, (x, y, TILE_SIZE, TILE_SIZE))
                        pygame.draw.rect(self.screen, BLACK, (x, y, TILE_SIZE, TILE_SIZE), 1)
                    elif tile_type == 3: #Glass floor
                        pygame.draw.rect(self.screen, CYAN, (x, y, TILE_SIZE, TILE_SIZE))
                        pygame.draw.rect(self.screen, BLACK, (x, y, TILE_SIZE, TILE_SIZE), 1)
                    elif tile_type == 4: #Button
                        pygame.draw.rect(self.screen, YELLOW, (x, y, TILE_SIZE, TILE_SIZE))
                        pygame.draw.rect(self.screen, BLACK, (x, y, TILE_SIZE, TILE_SIZE), 1)
                    elif tile_type == -2: #Hidden path
                        if self.board.button_is_active:
                            pygame.draw.rect(self.screen, BLUE, (x, y, TILE_SIZE, TILE_SIZE))
                        else:
                            pygame.draw.rect(self.screen, BLACK, (x, y, TILE_SIZE, TILE_SIZE))
                            pygame.draw.rect(self.screen, BLACK, (x, y, TILE_SIZE, TILE_SIZE), 1)
                    elif tile_type == 7: #Goal
                        pygame.draw.rect(self.screen, GREEN, (x, y, TILE_SIZE, TILE_SIZE))
                        pygame.draw.rect(self.screen, BLACK, (x, y, TILE_SIZE, TILE_SIZE), 1)

            #Draw the block
            if self.animation_active:
                self.draw_animated_block()
            else:
                self.draw_block()

            #Draw UI elements
            self.menu_button.draw(self.screen)
            self.restart_button.draw(self.screen)

            #Draw level information
            font = pygame.font.Font(None, 32)
            level_text = font.render(f"Level: {self.current_level.replace('LEVEL', '')}", True, BLACK)
            self.screen.blit(level_text, (20, 20))

            moves_text = font.render(f"Moves: {self.block.move_counter}", True, BLACK)
            self.screen.blit(moves_text, (20, 60))

        def draw_animated_block(self):
            progress = self.animation_progress

            # New interpolated coordinates
            x1 = self.old_block_position[0] + (self.target_block_position[0] - self.old_block_position[0]) * progress
            x2 = self.old_block_position[1] + (self.target_block_position[1] - self.old_block_position[1]) * progress
            y1 = self.old_block_position[2] + (self.target_block_position[2] - self.old_block_position[2]) * progress
            y2 = self.old_block_position[3] + (self.target_block_position[3] - self.old_block_position[3]) * progress

            if self.block.orientation == "upright":
                block_x = y1 * TILE_SIZE + self.camera_offset_x
                block_y = x1 * TILE_SIZE + self.camera_offset_y
                pygame.draw.rect(self.screen, HOT_PINK, (block_x, block_y, TILE_SIZE, TILE_SIZE))
                pygame.draw.rect(self.screen, BLACK, (block_x, block_y, TILE_SIZE, TILE_SIZE), 2)
            else:
            # Define animated positions for both ends of the block
                block_x1 = y1 * TILE_SIZE + self.camera_offset_x
                block_y1 = x1 * TILE_SIZE + self.camera_offset_y
                block_x2 = y2 * TILE_SIZE + self.camera_offset_x
                block_y2 = x2 * TILE_SIZE + self.camera_offset_y

                pygame.draw.rect(self.screen, HOT_PINK, (block_x1, block_y1, TILE_SIZE, TILE_SIZE))
                pygame.draw.rect(self.screen, HOT_PINK, (block_x2, block_y2, TILE_SIZE, TILE_SIZE))

            # Draw connection
            if self.block.orientation == "horizontal":
                connection_width = abs(block_x2 - block_x1) + TILE_SIZE
                pygame.draw.rect(self.screen, HOT_PINK, (min(block_x1, block_x2), block_y1, connection_width, TILE_SIZE))
            else:  # vertical
                connection_height = abs(block_y2 - block_y1) + TILE_SIZE
                pygame.draw.rect(self.screen, HOT_PINK, (block_x1, min(block_y1, block_y2), TILE_SIZE, connection_height))

            pygame.draw.rect(self.screen, BLACK, (block_x1, block_y1, TILE_SIZE, TILE_SIZE), 2)
            pygame.draw.rect(self.screen, BLACK, (block_x2, block_y2, TILE_SIZE, TILE_SIZE), 2)


        def draw_block(self):
            if self.block.orientation != "upright":
                x2, y2 = self.block.x2, self.block.y2
                block_x2 = self.block.y2 * TILE_SIZE + self.camera_offset_x
                block_y2 = self.block.x2 * TILE_SIZE + self.camera_offset_y

                pygame.draw.rect(self.screen, HOT_PINK, (block_x, block_y, TILE_SIZE, TILE_SIZE))
                pygame.draw.rect(self.screen, HOT_PINK, (block_x2, block_y2, TILE_SIZE, TILE_SIZE))

                # Draw connection between blocks
                if self.block.orientation == "horizontal":
                    connection_width = abs(block_x2 - block_x) + TILE_SIZE
                    pygame.draw.rect(self.screen, HOT_PINK, (min(block_x, block_x2), block_y, connection_width, TILE_SIZE))
                else:  # vertical
                    connection_height = abs(block_y2 - block_y) + TILE_SIZE
                    pygame.draw.rect(self.screen, HOT_PINK, (block_x, min(block_y, block_y2), TILE_SIZE, connection_height))

                # Borders
                pygame.draw.rect(self.screen, BLACK, (block_x, block_y, TILE_SIZE, TILE_SIZE), 2)
                pygame.draw.rect(self.screen, BLACK, (block_x2, block_y2, TILE_SIZE, TILE_SIZE), 2)
            else:
                # Just upright block
                x1, y1 = self.block.x1, self.block.y1
                block_x = y1 * TILE_SIZE + self.camera_offset_x
                block_y = x1 * TILE_SIZE + self.camera_offset_y
                pygame.draw.rect(self.screen, HOT_PINK, (block_x, block_y, TILE_SIZE, TILE_SIZE))
                pygame.draw.rect(self.screen, BLACK, (block_x, block_y, TILE_SIZE, TILE_SIZE), 2)


        def draw_game_over(self):
            #Semi-transparent overlay
            overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 150))
            self.screen.blit(overlay, (0, 0))

            #Game over text
            font = pygame.font.Font(None, 72)
            text = font.render("Game Over", True, RED)
            text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 -50))
            self.screen.blit(text, text_rect)

            #Buttons
            retry_button = Button(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 +30, 200, 50, "Try Again", YELLOW, (225, 255, 100))
            retry_button.draw(self.screen)

        def draw_level_complete(self):
            #Semi-transparent overlay
            overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 150))
            self.screen.blit(overlay, (0, 0))

            #Level complete text
            font = pygame.font.Font(None, 72)
            text = font.render("Level Complete!", True, RED)
            text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 -50))
            self.screen.blit(text, text_rect)

            #Display move count
            font = pygame.font.Font(None, 36)
            moves_text = font.render(f"Moves: {self.block.move_counter}", True, WHITE)
            moves_rect = moves_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            self.screen.blit(moves_text, moves_rect)

            #Buttons
            next_button = Button(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 +50, 200, 50, "Next Level", GREEN, (100, 255, 100))
            next_button.draw(self.screen)

            self.menu_button.update(pygame.mouse.get_pos())
            self.menu_button.draw(self.screen)

        def update_animation(self):
            pygame.display.flip()

        def run(self):
            running = True
            while running:
                    self.clock.tick(60)
                    running = self.handle_events()
                    mouse_pos = pygame.mouse.get_pos()
                    if self.game_state == MAIN_MENU:
                        self.play_button.update(mouse_pos)
                        self.rules_button.update(mouse_pos)
                        self.quit_button.update(mouse_pos)
                    self.draw()
                    self.update_animation()

