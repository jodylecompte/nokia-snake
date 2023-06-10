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

    self.clock = clock = pygame.time.Clock()

    self.bootstrap_pygame()

  def bootstrap_pygame(self):
    pygame.init()

    self.screen = pygame.display.set_mode((400, 500))
    pygame.display.set_caption('Snake')

  def run(self):
    print("Snake")
    while True:
      self.clock.tick(10)

      self.screen.fill(BACKGROUND_COLOR)
      game_area_margin = 30
      rect_width = self.screen.get_width() - 2 * game_area_margin
      rect_height = self.screen.get_height() - 2 * game_area_margin

      game_area = pygame.Rect(game_area_margin, game_area_margin, rect_width, rect_height)
      pygame.draw.rect(self.screen, FILL_COLOR, game_area, 2)

      snake = Snake(100, 100, self.screen, FILL_COLOR)

      font = pygame.font.SysFont(None, 36)
      text_rendered = font.render("Snake", True, FILL_COLOR)
      text_width = text_rendered.get_width()
      text_x = (400 - text_width) // 2

      score_text_rendered = font.render("Score: " + str(self.score), True, FILL_COLOR)
      score_text_width = score_text_rendered.get_width()
      score_text_x = (400 - score_text_width) // 2

      
      self.screen.blit(text_rendered, (text_x, 5))  # Adjust the vertical position as needed
      self.screen.blit(score_text_rendered, (score_text_x, 500 - 25))  # Adjust the vertical position as needed

      snake.draw()

      if snake.x < game_area.left or snake.x + 10 > game_area.right or snake.y < game_area.top or snake.y + 10 > game_area.bottom:
        pygame.quit()
        sys.exit()

      for event in pygame.event.get():
          if event.type == QUIT:
              pygame.quit()
              sys.exit()

          # Motion Events
          if event.type == pygame.KEYDOWN:
            snake.handle_event(event)

      pygame.display.update()

if __name__ == "__main__":
  game = Game()
  game.run()

