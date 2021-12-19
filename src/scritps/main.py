# import the pygame module, so you can use it
import os
import pygame
from pygame import color

# define a main function
class main():

    _running = False
    _screenWidth = 800
    _screenHeight = 600
    # Cornflower blue
    _bgColor = [100, 149, 237]

    def _initialize(self):
        # initialize the pygame module
        pygame.init()
        # load and set the logo
        asset_path = os.path.join('../assets', 'icon.png')
        logo = pygame.image.load(asset_path)
        pygame.display.set_icon(logo)
        pygame.display.set_caption("Darkryder's Awesome Game")
        
        # create a surface on screen that has the size of _screenWidth x _screenHeight
        self._screen = pygame.display.set_mode((self._screenWidth,self._screenHeight))
        
        # define a variable to control the main loop
        self._running = True
    
    def _loadAssets(self):
        asset_path = os.path.join('../assets', 'Face.png')
        self._face = pygame.image.load(asset_path)

    def _update(self):
        pass

    def _draw(self):
         # fill the screen with cornflower blue first
        self._screen.fill(self._bgColor)
        self._screen.blit(self._face, (50,50))
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