import sys

import pygame


class AlienInvasion:
    """a class to manage game resources and behaviors"""

    def __init__(self):
        """initialize game and create game resources"""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """begin the main loop"""
        while True:
            # monitoring the keyboard and mouse event
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # let the most recent drawn screen visible
            pygame.display.flip()


if __name__ == "__main__":
    # create an instance of game and run game
    ai = AlienInvasion()
    ai.run_game()

