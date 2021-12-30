import pygame
import os
from os import path

class Sprite(pygame.sprite.Sprite):

    def __init__(self, spriteName):
        super().__init__()

        asset_path = os.path.join('../assets', spriteName)
        self.image = pygame.image.load(asset_path)
        self.rect = self.image.get_rect()
        self.rect.x = 10
        self.rect.y = 100
    
    def update(self):
        self.rect.x += 1