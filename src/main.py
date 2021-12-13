# import the pygame module, so you can use it
import os
import pygame

# define a main function
class main():

    _running = False

    def _initialize(self):
        # initialize the pygame module
        pygame.init()
        # load and set the logo
        asset_path = os.path.join('./assets', 'icon.png')
        logo = pygame.image.load(asset_path)
        pygame.display.set_icon(logo)
        pygame.display.set_caption("Darkryder's Awesome Game")
        
        # create a surface on screen that has the size of 240 x 180
        self._screen = pygame.display.set_mode((800,600))
        
        # define a variable to control the main loop
        self._running = True
    
    def _loadAssets(self):
        asset_path = os.path.join('./assets', 'Face.png')
        _face = pygame.image.load(asset_path)
        pass
    
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
     
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main = main()