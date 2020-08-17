import pygame

class UI:
   def __init__(self, screen):
      self.screen = screen

   def draw_score(self, score):
      self.draw("Score: " + str(score), 35, (255,255,255), (360,50))
   def draw_level(self, level):
      self.draw("Level: " + str(level), 35, (255,255,255), (360,20))

   def draw(self, text, size, color, position):
      self.screen.blit(pygame.Surface(position), position)
      my_font = pygame.font.Font(None, size)
      surface = my_font.render(str(text), 0, color)
      self.screen.blit(surface, position) 