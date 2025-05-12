#import pillow and pygame
from PIL import Image
import pygame
#import button


#screen
screen_width = 800 #make into constant
screen_height = 600 #make into a constant not in main
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Dress Up')

exit_image  = pygame.image.load('images/exit.png').convert_alpha()

    

#load images
base_image = pygame.image.load('images/test_base.png').convert_alpha()

#clothes images
overalls =  pygame.image.load('images/clothes/overalls_test.png').convert_alpha()
sweater = pygame.image.load('images/clothes/sweater_test.png').convert_alpha()

#hair list
curly = pygame.image.load('images/hair/curly_hair.png').convert_alpha()
straight = pygame.image.load('images/hair/straight_hair.png').convert_alpha()
thick = pygame.image.load('images/hair/thick_hair_test.png').convert_alpha()
wavy = pygame.image.load('images/hair/wavy_hair_test.png').convert_alpha()

dark = pygame.image.load('images/skin/skin_d_hair.png').convert_alpha()
medium = pygame.image.load('images/skin/skin_m.png').convert_alpha()
light = pygame.image.load('images/skin/skin_l.png').convert_alpha()

overalls =  pygame.image.load('images/clothes/overalls_test.png').convert_alpha()
sweater = pygame.image.load('images/clothes/sweater_test.png').convert_alpha()

#hair list
curly_icon = pygame.image.load('images/icon/curly_icon.png').convert_alpha()
straight_icon = pygame.image.load('images/icon/curly_icon.png').convert_alpha()
thick_icon = pygame.image.load('images/icon/curly_icon.png').convert_alpha()
wavy_icon = pygame.image.load('images/icon/curly_icon.png').convert_alpha()

dark_icon = pygame.image.load('images/icon/curly_icon.png').convert_alpha()
medium_icon = pygame.image.load('images/icon/curly_icon.png').convert_alpha()
light_icon = pygame.image.load('images/icon/curly_icon.png').convert_alpha()





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


        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        screen.blit(self.image, (self.rect.x, self.rect.y))

        return results



exit_icon =  Button(100, 500, exit_image, 0.1)
dress_icon = Button(100, 100, dress, 1)

#def clothes_picker(clothes_choice):
    #dress
    #suit

#def hair_picker(hair_choice):
    #curly
    #straight

def main():
    clicked_clothes = None
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
    show_clothes = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        
        
        screen.blit(base_image, (0,0))

        if dress_icon.draw(screen):
            clicked_clothes = dress
            show_clothes = True
           # screen.blit(dress,(0,0))



        if exit_icon.draw(screen):
            running = False

        if show_clothes:
            screen.blit(clicked_clothes, (0, 0)) #dress could be a def clothes_picker(chosen_clothes) ex.
            #screen.blit(clothes_picker(clicked_clothes))
        #screen.blit(clothes_picker(clothes_choice), (0,0))
        pygame.display.update()
    

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