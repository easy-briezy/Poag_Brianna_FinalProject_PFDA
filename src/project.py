#import pillow and pygame
#import pillow
import pygame

def main():


    #pyagme
    #screen (images I made)
    #placement of clickable icons
    #mouse controls
    #full screen 
    pygame.init()

    width, height = pygame.display.Info().current_w, pygame.display.Info().current_h
    width = max(width, 1920)
    height = max(height, 1080)
    screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)

    pygame.display.set_caption('Dress Up')

        #exit button

    #store images
        #bg image
    base_image = pygame.image.load('images/test_base.png')
    #clothes list?
    #hair list?

    #loop for base image bg
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        #make base
        screen.blit(base_image, (0,0))
        pygame.display.flip()

    pygame.quit()

#image changer/loader
    #clothes changer
    #hair changer
#image placement

#mouse click icon choice
#the clicked choice is inputed into the matching item category image changer








#call main
if __name__ == "__main__":
    main()