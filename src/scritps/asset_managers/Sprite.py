import pygame
import os
from os import path

class Sprite(pygame.sprite.Sprite):

    def __init__(self, spriteName):
        super().__init__()

        asset_path = os.path.join('../assets', spriteName)
        self.image = pygame.image.load(asset_path)
        pygame.draw.rect(self.image,(255, 255, 255),pygame.Rect(0, 0, 50, 50))
        self.rect = self.image.get_rect()

    def PrintHelloWorld(self):
        pass

    # def _draw(self):
