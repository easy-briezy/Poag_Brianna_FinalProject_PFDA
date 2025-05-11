#import pillow and pygame
from PIL import Image
import pygame
#import button

#def store_images():
   # base_image = pygame.image.load('images/test_base.png').convert_alpha()

    #clothes list
    #dress =  pygame.image.load('images/clothes/dress_test.png').convert_alpha()
    #suit = pygame.image.load('images/clothes/suit_test.png').convert_alpha()

    #hair list
    #curly = pygame.image.load('images/hair/curly_hair_test.png').convert_alpha()
    #straight = pygame.image.load('images/hair/straight_hair_test.png').convert_alpha()

#screen
screen_width = 800 #make into constant
screen_height = 600 #make into a constant not in main
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Dress Up')

exit_image  = pygame.image.load('images/exit.png').convert_alpha()

    


base_image = pygame.image.load('images/test_base.png').convert_alpha()

#clothes list
dress =  pygame.image.load('images/clothes/dress_test.png').convert_alpha()
suit = pygame.image.load('images/clothes/suit_test.png').convert_alpha()

#hair list
curly = pygame.image.load('images/hair/curly_hair_test.png').convert_alpha()
straight = pygame.image.load('images/hair/straight_hair_test.png').convert_alpha()

class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, screen):
        results = False
        pos = pygame.mouse.get_pos() #where mouse is on screen

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                results = True

        if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
            self.clicked = True
            results = True

        screen.blit(self.image, (self.rect.x, self.rect.y))

        return results



exit_icon =  Button(100, 500, exit_image, 0.1)


def main():
    
    #pyagme
    #screen (images I made)
    #placement of clickable icons
    #mouse controls
    #full screen 
    pygame.init()



        #exit button

    #store images
        #clothes list?
        #hair list?

    

    #load and store each image option


    running = True
    while running:



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        
        
        screen.blit(base_image, (0,0))

        if exit_icon.draw(screen):
            print('EXIT')
            running = False
        #screen.blit(clothes_picker(clothes_choice), (0,0))
        pygame.display.update()
    

    pygame.quit()



#image changer/loader
    #clothes changer
    #hair changer
#image placement

#mouse click icon choice
#the clicked choice is inputed into the matching item category image changer

#def clothes_picker(clothes_choice):
    #dress
    #suit

#def hair_picker(hair_choice):
    #curly
    #straight








#call main
if __name__ == "__main__":
    main()