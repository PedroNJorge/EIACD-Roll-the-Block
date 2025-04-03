class Renderer:
    def __init__(self, block, board, width=800, height=600, tile_size=50):
        self.block = block
        self.board = board
        self.tile_size = tile_size
        self.screen = pygame.display.set_mode((width, height))
        
import pygame
import sys
import os
from block import Block
from board import Board
from game_logic import GameLogic
from input_handler import InputHandler

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TILE_SIZE = 50
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (100, 100, 100)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
PURPLE = (128, 0, 128)
TRANSPARENT_BLUE = (0, 0, 255, 128)
DARK_GRAY = (50, 50, 50)
LIGHT_BLUE = (173, 216, 230)

# Game states
MAIN_MENU = 0
RULES = 1
LEVEL_SELECT = 2
PLAYING = 3
GAME_OVER = 4
LEVEL_COMPLETE = 5

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
        return self.rect.collidepoint(mouse_pos) and mouse_click


class EnhancedRenderer:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Block Shifter")
        self.clock = pygame.time.Clock()
        self.game_state = MAIN_MENU
        self.current_level = "LEVEL1"
        self.block = None
        self.board = None
        self.game_logic = None
        self.input_handler = None
        self.init_buttons()
        
        # Animation properties
        self.animation_active = False
        self.animation_direction = None
        self.animation_progress = 0
        self.animation_speed = 0.1
        self.old_block_position = None
        self.target_block_position = None
        
        # Load background
        self.background = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.background.fill(LIGHT_BLUE)
        
        # Camera offset for centering the level
        self.camera_offset_x = 0
        self.camera_offset_y = 0
        
        # Transition variables
        self.transition_alpha = 0
        self.transition_state = None

    def init_buttons(self):
        center_x = SCREEN_WIDTH // 2
        
        # Main menu buttons
        self.play_button = Button(center_x - 100, 200, 200, 50, "Play", GREEN, (100, 255, 100))
        self.rules_button = Button(center_x - 100, 270, 200, 50, "Rules", YELLOW, (255, 255, 100))
        self.quit_button = Button(center_x - 100, 340, 200, 50, "Quit", RED, (255, 100, 100))
        
        # Rules screen button
        self.back_button = Button(center_x - 100, 500, 200, 50, "Back", GRAY, (150, 150, 150))
        
        # Level select buttons
        self.level_buttons = []
        for i in range(3):
            for j in range(3):
                level_num = i * 3 + j + 1
                x = 150 + j * 175
                y = 150 + i * 120
                self.level_buttons.append(Button(x, y, 125, 80, f"Level {level_num}", CYAN, (100, 255, 255)))
        
        # Game buttons
        self.menu_button = Button(SCREEN_WIDTH - 120, 20, 100, 40, "Menu", GRAY, (150, 150, 150))
        self.restart_button = Button(SCREEN_WIDTH - 120, 70, 100, 40, "Restart", YELLOW, (255, 255, 100))

    def initialize_level(self, level_name):
        self.current_level = level_name
        self.board = Board(level_name)
        x, y = self.board.level.start
        self.block = Block(x, y)
        self.game_logic = GameLogic(self.block, self.board)
        self.input_handler = InputHandler(self.block, self.board, self.game_logic)
        
        # Update the layout with the initial block position
        self.board.refresh_layout(self.block)
        
        # Calculate camera offsets to center the level
        self.calculate_camera_offset()

    def calculate_camera_offset(self):
        level_pixel_width = len(self.board.level.layout[0]) * TILE_SIZE
        level_pixel_height = len(self.board.level.layout) * TILE_SIZE
        
        self.camera_offset_x = (SCREEN_WIDTH - level_pixel_width) // 2
        self.camera_offset_y = (SCREEN_HEIGHT - level_pixel_height) // 2

    def handle_events(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = False
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_click = True
            
            if self.game_state == PLAYING and not self.animation_active:
                if event.type == pygame.KEYDOWN:
                    if event.key in [pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d]:
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
        
        if self.game_state == MAIN_MENU:
            self.handle_main_menu(mouse_pos, mouse_click)
        elif self.game_state == RULES:
            self.handle_rules_screen(mouse_pos, mouse_click)
        elif self.game_state == LEVEL_SELECT:
            self.handle_level_select(mouse_pos, mouse_click)
        elif self.game_state == PLAYING:
            self.handle_playing(mouse_pos, mouse_click)
        elif self.game_state == GAME_OVER:
            self.handle_game_over(mouse_pos, mouse_click)
        elif self.game_state == LEVEL_COMPLETE:
            self.handle_level_complete(mouse_pos, mouse_click)
            
        return True

    def handle_main_menu(self, mouse_pos, mouse_click):
        self.play_button.update(mouse_pos)
        self.rules_button.update(mouse_pos)
        self.quit_button.update(mouse_pos)
        
        if self.play_button.is_clicked(mouse_pos, mouse_click):
            self.game_state = LEVEL_SELECT
        elif self.rules_button.is_clicked(mouse_pos, mouse_click):
            self.game_state = RULES
        elif self.quit_button.is_clicked(mouse_pos, mouse_click):
            return False
            
        return True

    def handle_rules_screen(self, mouse_pos, mouse_click):
        self.back_button.update(mouse_pos)
        
        if self.back_button.is_clicked(mouse_pos, mouse_click):
            self.game_state = MAIN_MENU
            
        return True

    def handle_level_select(self, mouse_pos, mouse_click):
        self.back_button.update(mouse_pos)
        
        if self.back_button.is_clicked(mouse_pos, mouse_click):
            self.game_state = MAIN_MENU
            return True
            
        for i, button in enumerate(self.level_buttons):
            button.update(mouse_pos)
            if button.is_clicked(mouse_pos, mouse_click):
                level_name = f"LEVEL{i+1}"
                self.initialize_level(level_name)
                self.game_state = PLAYING
                break
                
        return True

    def handle_playing(self, mouse_pos, mouse_click):
        self.menu_button.update(mouse_pos)
        self.restart_button.update(mouse_pos)
        
        if self.menu_button.is_clicked(mouse_pos, mouse_click):
            self.game_state = MAIN_MENU
        elif self.restart_button.is_clicked(mouse_pos, mouse_click):
            self.initialize_level(self.current_level)
            
        # Check for game state changes
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
        
        next_level_button = Button(SCREEN_WIDTH // 2 - 100, 300, 200, 50, "Next Level", GREEN, (100, 255, 100))
        next_level_button.update(mouse_pos)
        
        if next_level_button.is_clicked(mouse_pos, mouse_click):
            # Get next level
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
        
        # Create a temporary block to calculate the new position
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
        self.screen.blit(self.background, (0, 0))
        
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
        # Draw title
        font = pygame.font.Font(None, 72)
        title = font.render("Block Shifter", True, BLUE)
        title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, 100))
        self.screen.blit(title, title_rect)
        
        # Draw buttons
        self.play_button.draw(self.screen)
        self.rules_button.draw(self.screen)
        self.quit_button.draw(self.screen)
        
        # Draw footer
        font = pygame.font.Font(None, 24)
        footer = font.render("© 2025 Block Shifter Game", True, BLACK)
        footer_rect = footer.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 30))
        self.screen.blit(footer, footer_rect)

    def draw_rules_screen(self):
        # Draw title
        font = pygame.font.Font(None, 48)
        title = font.render("Game Rules", True, BLUE)
        title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, 60))
        self.screen.blit(title, title_rect)
        
        # Draw rules text
        rules = [
            "Roll the Block is a puzzle game where you control a block",
            "as it moves through the level, by flipping it through different"
            "positions.",
            "",
            "Controls:",
            "- W: Move Up",
            "- S: Move Down",
            "- A: Move Left",
            "- D: Move Right",
            "",
            "Block positions:",
            "- Upright Block: Can stand on regular floors but breaks through glass",
            "- Horizontal/Vertical Block: Can stand on glass floors",
            "",
            "Game Elements:",
            "- Blue Floor: Regular floor",
            "- Green Square: Goal - reach it to complete the level",
            "- Yellow Button: Activates hidden paths when pressed",
            "- Dark Void: Falling here means game over",
            "- Glass Floor: Only horizontal/vertical blocks can stand here"
        ]
        
        font = pygame.font.Font(None, 24)
        for i, line in enumerate(rules):
            text = font.render(line, True, BLACK)
            self.screen.blit(text, (100, 120 + i * 25))
        
        # Draw back button
        self.back_button.draw(self.screen)

    def draw_level_select(self):
        # Draw title
        font = pygame.font.Font(None, 48)
        title = font.render("Select Level", True, BLUE)
        title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, 60))
        self.screen.blit(title, title_rect)
        
        # Draw level buttons
        for button in self.level_buttons:
            button.draw(self.screen)
        
        # Draw back button
        self.back_button.draw(self.screen)

    def draw_level(self):
        # Draw the game board
        layout = self.board.level.layout
        
        for i in range(len(layout)):
            for j in range(len(layout[0])):
                x = j * TILE_SIZE + self.camera_offset_x
                y = i * TILE_SIZE + self.camera_offset_y
                tile_type = layout[i][j]
                
                # Draw different tiles based on type
                if tile_type == 5:  # VOID
                    pygame.draw.rect(self.screen, BLACK, (x, y, TILE_SIZE, TILE_SIZE))
                elif tile_type == 0:  # FLOOR
                    pygame.draw.rect(self.screen, BLUE, (x, y, TILE_SIZE, TILE_SIZE))
                    pygame.draw.rect(self.screen, BLACK, (x, y, TILE_SIZE, TILE_SIZE), 1)
                elif tile_type == 3:  # GLASS_FLOOR
                    pygame.draw.rect(self.screen, CYAN, (x, y, TILE_SIZE, TILE_SIZE))
                    pygame.draw.rect(self.screen, BLACK, (x, y, TILE_SIZE, TILE_SIZE), 1)
                elif tile_type == 4:  # BUTTON
                    pygame.draw.rect(self.screen, YELLOW, (x, y, TILE_SIZE, TILE_SIZE))
                    pygame.draw.rect(self.screen, BLACK, (x, y, TILE_SIZE, TILE_SIZE), 1)
                elif tile_type == -2:  # HIDDEN_PATH
                    if self.board.button_is_active:
                        pygame.draw.rect(self.screen, BLUE, (x, y, TILE_SIZE, TILE_SIZE))
                    else:
                        pygame.draw.rect(self.screen, BLACK, (x, y, TILE_SIZE, TILE_SIZE))
                    pygame.draw.rect(self.screen, BLACK, (x, y, TILE_SIZE, TILE_SIZE), 1)
                elif tile_type == 7:  # GOAL
                    pygame.draw.rect(self.screen, GREEN, (x, y, TILE_SIZE, TILE_SIZE))
                    pygame.draw.rect(self.screen, BLACK, (x, y, TILE_SIZE, TILE_SIZE), 1)
        
        # Draw the block (with animation if active)
        if self.animation_active:
            self.draw_animated_block()
        else:
            self.draw_block()
        
        # Draw UI elements
        self.menu_button.draw(self.screen)
        self.restart_button.draw(self.screen)
        
        # Draw level info
        font = pygame.font.Font(None, 32)
        level_text = font.render(f"Level: {self.current_level.replace('LEVEL', '')}", True, BLACK)
        self.screen.blit(level_text, (20, 20))
        
        moves_text = font.render(f"Moves: {self.block.move_counter}", True, BLACK)
        self.screen.blit(moves_text, (20, 60))

    def draw_animated_block(self):
        progress = self.animation_progress
        
        # Linear interpolation between old and new positions
        x1 = self.old_block_position[0] + (self.target_block_position[0] - self.old_block_position[0]) * progress
        y1 = self.old_block_position[1] + (self.target_block_position[1] - self.old_block_position[1]) * progress
        x2 = self.old_block_position[2] + (self.target_block_position[2] - self.old_block_position[2]) * progress
        y2 = self.old_block_position[3] + (self.target_block_position[3] - self.old_block_position[3]) * progress
        
        # Draw block based on current orientation
        if self.block.orientation == "upright":
            block_x = y1 * TILE_SIZE + self.camera_offset_x
            block_y = x1 * TILE_SIZE + self.camera_offset_y
            pygame.draw.rect(self.screen, RED, (block_x, block_y, TILE_SIZE, TILE_SIZE))
            pygame.draw.rect(self.screen, BLACK, (block_x, block_y, TILE_SIZE, TILE_SIZE), 2)
        else:
            block_x1 = y1 * TILE_SIZE + self.camera_offset_x
            block_y1 = x1 * TILE_SIZE + self.camera_offset_y
            block_x2 = y2 * TILE_SIZE + self.camera_offset_x
            block_y2 = x2 * TILE_SIZE + self.camera_offset_y
            
            pygame.draw.rect(self.screen, RED, (block_x1, block_y1, TILE_SIZE, TILE_SIZE))
            pygame.draw.rect(self.screen, RED, (block_x2, block_y2, TILE_SIZE, TILE_SIZE))
            pygame.draw.rect(self.screen, BLACK, (block_x1, block_y1, TILE_SIZE, TILE_SIZE), 2)
            pygame.draw.rect(self.screen, BLACK, (block_x2, block_y2, TILE_SIZE, TILE_SIZE), 2)
            
            # Draw connection between blocks
            if self.block.orientation == "horizontal":
                pygame.draw.rect(self.screen, RED, (min(block_x1, block_x2), block_y1, abs(block_x2 - block_x1), TILE_SIZE))
            else:  # vertical
                pygame.draw.rect(self.screen, RED, (block_x1, min(block_y1, block_y2), TILE_SIZE, abs(block_y2 - block_y1)))

    def draw_block(self):
        if self.block.orientation == "upright":
            block_x = self.block.y1 * TILE_SIZE + self.camera_offset_x
            block_y = self.block.x1 * TILE_SIZE + self.camera_offset_y
            pygame.draw.rect(self.screen, RED, (block_x, block_y, TILE_SIZE, TILE_SIZE))
            pygame.draw.rect(self.screen, BLACK, (block_x, block_y, TILE_SIZE, TILE_SIZE), 2)
        else:
            block_x1 = self.block.y1 * TILE_SIZE + self.camera_offset_x
            block_y1 = self.block.x1 * TILE_SIZE + self.camera_offset_y
            block_x2 = self.block.y2 * TILE_SIZE + self.camera_offset_x
            block_y2 = self.block.x2 * TILE_SIZE + self.camera_offset_y
            
            pygame.draw.rect(self.screen, RED, (block_x1, block_y1, TILE_SIZE, TILE_SIZE))
            pygame.draw.rect(self.screen, RED, (block_x2, block_y2, TILE_SIZE, TILE_SIZE))
            pygame.draw.rect(self.screen, BLACK, (block_x1, block_y1, TILE_SIZE, TILE_SIZE), 2)
            pygame.draw.rect(self.screen, BLACK, (block_x2, block_y2, TILE_SIZE, TILE_SIZE), 2)
            
            # Draw connection between blocks
            if self.block.orientation == "horizontal":
                pygame.draw.rect(self.screen, RED, (min(block_x1, block_x2), block_y1, abs(block_x2 - block_x1), TILE_SIZE))
            else:  # vertical
                pygame.draw.rect(self.screen, RED, (block_x1, min(block_y1, block_y2), TILE_SIZE, abs(block_y2 - block_y1)))

    def draw_game_over(self):
        # Semi-transparent overlay
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 150))
        self.screen.blit(overlay, (0, 0))
        
        # Game over text
        font = pygame.font.Font(None, 72)
        text = font.render("Game Over", True, RED)
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
        self.screen.blit(text, text_rect)
        
        # Buttons
        retry_button = Button(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 30, 200, 50, "Try Again", YELLOW, (255, 255, 100))
        retry_button.draw(self.screen)
        
        self.menu_button.update(pygame.mouse.get_pos())
        self.menu_button.draw(self.screen)

    def draw_level_complete(self):
        # Semi-transparent overlay
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 150))
        self.screen.blit(overlay, (0, 0))
        
        # Level complete text
        font = pygame.font.Font(None, 72)
        text = font.render("Level Complete!", True, GREEN)
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
        self.screen.blit(text, text_rect)
        
        # Display move count
        font = pygame.font.Font(None, 36)
        moves_text = font.render(f"Moves: {self.block.move_counter}", True, WHITE)
        moves_rect = moves_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.screen.blit(moves_text, moves_rect)
        
        # Buttons
        next_button = Button(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 50, 200, 50, "Next Level", GREEN, (100, 255, 100))
        next_button.draw(self.screen)
        
        self.menu_button.update(pygame.mouse.get_pos())
        self.menu_button.draw(self.screen)

    def run(self):
        running = True
        while running:
            self.clock.tick(FPS)
            running = self.handle_events()
            self.update_animation()
            self.draw()


def main():
    game = EnhancedRenderer()
    game.run()
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
