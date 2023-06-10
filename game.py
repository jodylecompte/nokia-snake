import pygame, sys
from pygame.locals import QUIT

from src.snake import Snake

BACKGROUND_COLOR = pygame.Color(184, 194, 2)
FILL_COLOR = pygame.Color(112, 96, 1)

class Game:
  def __init__(self):
    self.gameState = 'running'
    self.score = 0;

    self.game_width = 400
    self.game_height = 500
    self.game_margin = 30

    self.bootstrap_pygame()

  def bootstrap_pygame(self):
    pygame.init()

    self.screen = pygame.display.set_mode((self.game_width, self.game_height))
    self.clock = clock = pygame.time.Clock()
    pygame.display.set_caption('Snake')

    self.font_large = pygame.font.SysFont(None, 36)
    self.font_small = pygame.font.SysFont(None, 20)

    self.snake = Snake(100, 100, self.screen, FILL_COLOR)

  def draw_base_screen(self):
    self.screen.fill(BACKGROUND_COLOR)

    rect_width = self.screen.get_width() - 2 * self.game_margin
    rect_height = self.screen.get_height() - 2 * self.game_margin

    self.game_area = pygame.Rect(self.game_margin, self.game_margin, rect_width, rect_height)
    pygame.draw.rect(self.screen, FILL_COLOR, self.game_area, 2)

    text_rendered = self.font_large.render("Snake", True, FILL_COLOR)
    text_width = text_rendered.get_width()
    text_x = (400 - text_width) // 2

    self.screen.blit(text_rendered, (text_x, 5)) 


  def draw_paused_screen(self):
    paused_text_rendered = self.font_large.render("Paused", True, FILL_COLOR)
    paused_text_width = paused_text_rendered.get_width()
    paused_text_height = paused_text_rendered.get_height()
    paused_text_x = (self.screen.get_width() - paused_text_width) // 2
    paused_text_y = (self.screen.get_height() - paused_text_height) // 2 - 20

    # Render and center the "Press 'p' to return to game" text using font_small
    return_text_rendered = self.font_small.render("Press 'p' to return to game", True, FILL_COLOR)
    return_text_width = return_text_rendered.get_width()
    return_text_height = return_text_rendered.get_height()
    return_text_x = (self.screen.get_width() - return_text_width) // 2
    return_text_y = (self.screen.get_height() - return_text_height) // 2 + 20

    # Draw the texts on the screen
    self.screen.blit(paused_text_rendered, (paused_text_x, paused_text_y))
    self.screen.blit(return_text_rendered, (return_text_x, return_text_y))

  def draw_game_over_screen(self):
    pass

  def draw_game_screen(self):
    font = pygame.font.SysFont(None, 24)
    score_text_rendered = font.render("Score: " + str(self.score), True, FILL_COLOR)
    score_text_width = score_text_rendered.get_width()
    score_text_x = (400 - score_text_width) // 2
    
    self.screen.blit(score_text_rendered, (score_text_x, 500 - 25)) 

  def run(self):
    while True:
      self.clock.tick(10)

      self.draw_base_screen()

      if self.gameState == 'running':
        self.draw_game_screen()
        self.snake.draw()
      elif self.gameState == 'paused':
        self.draw_paused_screen()
      elif self.gameState == 'game_over':
        self.draw_game_over_screen()


      # TODO - Extract to snake class
      if self.snake.x < self.game_area.left or self.snake.x + 10 > self.game_area.right or self.snake.y < self.game_area.top or self.snake.y + 10 > self.game_area.bottom:
        pygame.quit()
        sys.exit()

      for event in pygame.event.get():
          if event.type == QUIT:
              pygame.quit()
              sys.exit()

          # Motion Events
          if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
              if self.gameState == 'running':
                self.gameState = 'paused'
              else:
                self.gameState = 'running'

            # self.snake.handle_event(event)

      pygame.display.update()

if __name__ == "__main__":
  game = Game()
  game.run()

