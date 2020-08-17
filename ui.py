import pygame

class UI:
   def __init__(self, screen):
      self.screen = screen

   def draw_score(self, score):
      my_font = pygame.font.Font(None, 25)
      surface = my_font.render("Score: " + str(score), 0,(255,255,255))
      self.screen.blit(surface, (30,40)) 