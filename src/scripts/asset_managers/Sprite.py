import pygame
from os import path

from Utils.Utils import Utils


class Sprite(pygame.sprite.Sprite):

    def __init__(self, spriteName, a_iStartX: int, a_iStartY: int):
        super().__init__()

        asset_basepath = Utils.resource_path('./assets')
        asset_path = path.join(asset_basepath, spriteName)
        self.image = pygame.image.load(asset_path)
        self.rect = self.image.get_rect()
        self.rect.x = a_iStartX
        self.rect.y = a_iStartY

    def update(self):
        # self.rect.x += 1
        pass
