import pygame


class Ship:
    """a class to manage the ship"""

    def __init__(self, ai_game):
        """initialize the ship and set the original position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # load the ship image and get the circum rectangle
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # for each ship, place it on the mid-bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """draw the ships at the specific position"""
        self.screen.blit(self.image, self.rect)