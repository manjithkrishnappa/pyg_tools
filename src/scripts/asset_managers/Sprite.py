import pygame
import os
from os import path

class Sprite(pygame.sprite.Sprite):

    def __init__(self, spriteName, a_iStartX : int, a_iStartY : int):
        super().__init__()

        asset_path = os.path.join('../assets', spriteName)
        self.image = pygame.image.load(asset_path)
        self.rect = self.image.get_rect()
        self.rect.x = a_iStartX
        self.rect.y = a_iStartY
    
    def update(self):
        # self.rect.x += 1
        pass