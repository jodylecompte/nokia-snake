import pygame

class Snake:
    def __init__(self, x, y, screen, fill_color):
        self.x = x
        self.y = y
        self.speed_x = 0
        self.speed_y = 0
        self.screen = screen
        self.fill_color = fill_color
        self.rect = pygame.Rect(x, y, 10, 10)

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y
        self.rect.x = self.x
        self.rect.y = self.y

    def reset(self):
      self.x = 100
      self.y = 100
      self.speed_x = 0
      self.speed_y = 0

    def draw(self):
        self.update()

        pygame.draw.rect(self.screen, self.fill_color, self.rect)

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
