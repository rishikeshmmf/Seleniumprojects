import sys
import pygame

def check_events():
 for event in pygame.event.get():  """Respond to keypresses and mouse events."""
 if event.type == pygame.QUIT:
   sys.exit()
