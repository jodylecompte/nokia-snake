import pygame

class Snake:
    def __init__(self, x, y, screen, fill_color, game):
        self.x = x
        self.y = y
        self.speed_x = 0
        self.speed_y = 0
        self.screen = screen
        self.fill_color = fill_color
        self.rect = pygame.Rect(x, y, 10, 10)
        self.parts = []  
        self.length = 1  
        self.game = game

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y
        self.rect.x = self.x
        self.rect.y = self.y

        self.update_body_parts()

        self.check_collision()

    def reset(self):
        self.x = 100
        self.y = 100
        self.speed_x = 0
        self.speed_y = 0
        self.parts.clear() 
        self.length = 1

    def draw(self):
        self.update()

        pygame.draw.rect(self.screen, self.fill_color, self.rect)

        for part in self.parts:
            pygame.draw.rect(self.screen, self.fill_color, part)

    def handle_event(self, event):
        if event.key == pygame.K_LEFT:
            self.speed_x = -10
            self.speed_y = 0
        elif event.key == pygame.K_RIGHT:
            self.speed_x = 10
            self.speed_y = 0
        elif event.key == pygame.K_UP:
            self.speed_x = 0
            self.speed_y = -10
        elif event.key == pygame.K_DOWN:
            self.speed_x = 0
            self.speed_y = 10

    def update_body_parts(self):
        self.parts.append(pygame.Rect(self.x, self.y, 10, 10))

        if len(self.parts) > self.length:
            self.parts.pop(0)

    def grow(self):
        self.length += 1

    def check_collision(self):
        for part in self.parts[:-1]: 
            if self.rect.colliderect(part):
                self.game.game_state = 'game_over'

