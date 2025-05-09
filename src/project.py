#import pillow and pygame
from PIL import Image
import pygame



def main():

    
    
    #pyagme
    #screen (images I made)
    #placement of clickable icons
    #mouse controls
    #full screen 
    pygame.init()

    #screen
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    

    pygame.display.set_caption('Dress Up')


        #exit button

    #store images
        #clothes list?
        #hair list?

    

    #load and store each image option
    base_image = pygame.image.load('images/test_base.png').convert_alpha()
    dress =  pygame.image.load('images/clothes/dress_test.png').convert_alpha()
    suit = pygame.image.load('images/clothes/suit_test.png').convert_alpha()
    curly = pygame.image.load('images/hair/curly_hair_test.png').convert_alpha()
    straight = pygame.image.load('images/hair/straight_hair_test.png').convert_alpha()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        
        
        screen.blit(base_image, (0,0))
        screen.blit(clothes_picker(clothes_choice), (0,0))
        pygame.display.update()
    

    pygame.quit()



#image changer/loader
    #clothes changer
    #hair changer
#image placement

#mouse click icon choice
#the clicked choice is inputed into the matching item category image changer

def clothes_picker(clothes_choice):
    







#call main
if __name__ == "__main__":
    main()