# import the pygame module, so you can use it
import os
from typing import Text
import pygame
from pygame import color

from asset_managers.Sprite import Sprite
from asset_managers.Text import Text

# define a main function
class main():

    _running = False
    _screenWidth = 800
    _screenHeight = 600
    # Cornflower blue
    _bgColor = [100, 149, 237]

    _tempCounter = 0

    def _initialize(self):
        # initialize the pygame module
        pygame.init()
        # load and set the logo
        print (os.getcwd())
        asset_path = os.path.join(os.getcwd(), './assets/icon.png')
        logo = pygame.image.load(asset_path)
        pygame.display.set_icon(logo)
        pygame.display.set_caption("Darkryder's Awesome Game")
        
        # create a surface on screen that has the size of _screenWidth x _screenHeight
        self._screen = pygame.display.set_mode((self._screenWidth,self._screenHeight))

        self.all_sprites_list = pygame.sprite.Group()

        pygame.font.init()

        # define a variable to control the main loop
        self._running = True
    
    def _loadAssets(self):
        self.face_ = Sprite('Face.png', 10, 100)
        self.all_sprites_list.add(self.face_)

        self.info_ = Text('Hello World', 500, 250)
        pass

    def _update(self):
        self.face_.update()
        self.all_sprites_list.update()

        self._tempCounter += 1
        self.info_.SetText('Frame Counter: ' + str(self._tempCounter))

        pass

    def _draw(self):
         # fill the screen with cornflower blue first
        self._screen.fill(self._bgColor)
        self.all_sprites_list.draw(self._screen)
        self.info_.Draw(self._screen)
        pygame.display.flip()
    
    def __init__(self):
        self._initialize()
        self._loadAssets()
        # main loop
        while self._running:
            # event handling, gets all event from the event queue
            for event in pygame.event.get():
                # only do something if the event is of type QUIT
                if event.type == pygame.QUIT:
                    # change the value to False, to exit the main loop
                    self._running = False
            self._update()
            self._draw()

     
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main = main()