import sys
import pygame
from pygame.examples.go_over_there import screen
from settings import Settings
from Pythoncrashcourse.pygame import ship

ai_settings = Settings()
def check_events():
 for event in pygame.event.get():  """Respond to keypresses and mouse events."""
 if event.type == pygame.QUIT:
   sys.exit()
def update_screen(ai_settings, screen, ship):
"""Update images on the screen and flip to the new screen."""
# Redraw the screen during each pass through the loop.
 screen.fill(ai_settings.bg_color)
 ship.blitme()
# Make the most recently drawn screen visible.
pygame.display.flip()