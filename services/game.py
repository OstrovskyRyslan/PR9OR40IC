import pygame
import os
class Game:
    def __init__(self):
        self.selected_menu_item = None
        self.small_font = None
        self.font = None
        self.menu_items = None
        self.screen = None
        self.background = None
    def init(self):
        pygame.init()
        self.screen_width, self.screen_height = 800, 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Початок гри")
        self.menu_items = ["Почати гру", "Завантажити гру", "Вийти"]
        self.selected_menu_item = 0
        self.font = pygame.font.Font(None, 74)
        self.small_font = pygame.font.Font(None, 50)
        background_path = os.path.join("C:\\Users\\Ruslan Ostrovsky\\Desktop\\pr9\\fon", "fon.jpg")
        if os.path.exists(background_path):
            self.background = pygame.image.load(background_path).convert()
        else:
            print(f"Файл {background_path} не знайдено. Перевірте шлях!")
            self.background = None
    def flip(self):
        pygame.display.flip()
    def update_menu_item_render(self):
        for i, item in enumerate(self.menu_items):
            color = (255, 255, 255) if i == self.selected_menu_item else (100, 100, 100)
            text_surface = self.small_font.render(item, True, color)
            text_rect = text_surface.get_rect(center=(self.screen_width // 2, 100 + i * 60))
            self.screen.blit(text_surface, text_rect)
    def start_game(self):
        player_x, player_y = 50, 50
        player_speed = 5
        bg_x = 0  
        game_running = True
        clock = pygame.time.Clock()
        fps = 60
        while game_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_running = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                player_x -= player_speed
                bg_x += 2  
            if keys[pygame.K_RIGHT]:
                player_x += player_speed
                bg_x -= 2 
            if keys[pygame.K_UP]:
                player_y -= player_speed
            if keys[pygame.K_DOWN]:
                player_y += player_speed
            player_x = max(0, min(player_x, self.screen_width - 50))
            player_y = max(0, min(player_y, self.screen_height - 50))
            if self.background:
                self.screen.blit(self.background, (bg_x, 0))  
                self.screen.blit(self.background, (bg_x + self.screen_width, 0))  
            pygame.draw.rect(self.screen, (255, 0, 0), (player_x, player_y, 50, 50))
            self.flip()
            clock.tick(fps)
            if bg_x <= -self.screen_width:
                bg_x = 0
        self.screen.fill((0, 0, 0))
    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:  
                        self.selected_menu_item = (self.selected_menu_item + 1) % len(self.menu_items)
                    if event.key == pygame.K_UP: 
                        self.selected_menu_item = (self.selected_menu_item - 1) % len(self.menu_items)
                    if event.key == pygame.K_RETURN:  
                        if self.selected_menu_item == 0:  
                            print("Гра запускається...")
                            self.start_game()
                        elif self.selected_menu_item == 1: 
                            print("Завантаження гри...")
                        elif self.selected_menu_item == 2:  
                            running = False
            self.screen.fill((0, 0, 0))  
            self.update_menu_item_render()
            self.flip()
        pygame.quit()
