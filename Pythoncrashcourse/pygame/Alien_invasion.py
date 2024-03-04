import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(screen)  # make a ship

    # Start the main loop for the game.
    while True:
        # Watch for keyboard and mouse events.
        gf.check_events()

        screen.fill(ai_settings.bg_color)
        ship.blitme()
        gf.update_screen(ai_settings, screen, ship)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Make the most recently drawn screen visible.
        pygame.display.flip()


run_game()
