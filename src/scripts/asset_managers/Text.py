import pygame

class Text():

    def __init__(self, text, PosX, PosY):
        self.font = pygame.font.SysFont('freesanbold.ttf', 50)
        self.SetText(text)
        self.SetPosition(PosX, PosY)
        pass

    def SetText(self, text):
        self.text = self.font.render(text, True, (255, 255, 255))
    
    def SetPosition(self, PosX, PosY):
        self.textRect = self.text.get_rect()
        # setting center for the first text
        self.textRect.center = (PosX, PosY)

    def Draw(self, _screen):
        _screen.blit(self.text, self.textRect)