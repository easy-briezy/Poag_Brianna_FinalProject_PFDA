#import pillow and pygame
from PIL import Image
import pygame
#import button


#screen
screen_width = 800 
screen_height = 600 
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Dress Up')



    

#base images
base_image = pygame.image.load('images/base.png').convert_alpha()
exit_image  = pygame.image.load('images/exit.png').convert_alpha()
menu = pygame.image.load('images/menu.png').convert_alpha()

#clothes images
overalls =  pygame.image.load('images/clothes/overalls.png').convert_alpha()
sweater = pygame.image.load('images/clothes/sweater.png').convert_alpha()

#hair list
curly = pygame.image.load('images/hair/curly_hair.png').convert_alpha()
straight = pygame.image.load('images/hair/straight_hair.png').convert_alpha()
thick = pygame.image.load('images/hair/thick_hair.png').convert_alpha()
wavy = pygame.image.load('images/hair/wavy_hair.png').convert_alpha()

#skin list
dark = pygame.image.load('images/skin/skin_d.png').convert_alpha()
medium = pygame.image.load('images/skin/skin_m.png').convert_alpha()
light = pygame.image.load('images/skin/skin_l.png').convert_alpha()


#clothes icons
overalls_icon =  pygame.image.load('images/icon/overalls_icon.png').convert_alpha()
sweater_icon = pygame.image.load('images/icon/sweater_icon.png').convert_alpha()

#hair icons
curly_icon = pygame.image.load('images/icon/c_icon.png').convert_alpha()
straight_icon = pygame.image.load('images/icon/s_icon.png').convert_alpha()
thick_icon = pygame.image.load('images/icon/t_icon.png').convert_alpha()
wavy_icon = pygame.image.load('images/icon/w_icon.png').convert_alpha()

#skin icons
dark_icon = pygame.image.load('images/icon/d_icon.png').convert_alpha()
medium_icon = pygame.image.load('images/icon/m_icon.png').convert_alpha()
light_icon = pygame.image.load('images/icon/l_icon.png').convert_alpha()





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



exit_button =  Button(20, 20, exit_image, 1)

#skin buttons

dark_button = Button(300, 450, dark_icon, 1)
medium_button = Button(420, 450, medium_icon, 1)
light_button = Button(520, 450, light_icon, 1)

#hair buttons
curly_button = Button(550, 300, curly_icon, 1)
wavy_button = Button(550, 300, wavy_icon, 1)
thick_button = Button(550, 300, thick_icon, 1)
straight_button = Button(550, 300, straight_icon, 1)


#clothes buttons
sweater_button = Button(100, 300, sweater_icon, 1)
overalls_button = Button(100, 400, overalls_icon, 1)



#def clothes_picker(clothes_choice):
    #dress
    #suit

#def hair_picker(hair_choice):
    #curly
    #straight

#def icon_placement()

def main():
    clicked_skin = None
    clicked_hair = None
    clicked_clothes = None

    
    pygame.init()





    #store images
        #clothes list?
        #hair list?

    

    #load and store each image option


    running = True
    show_skin = False
    show_hair = False
    show_clothes = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        
        
        screen.blit(base_image, (0,0))
        screen.blit(menu, (0,0))






        if overalls_button.draw(screen):
            clicked_clothes = overalls_icon
            show_clothes = True

        if sweater_button.draw(screen):
            clicked_clothes = sweater_icon
            show_clothes = True
           # screen.blit(dress,(0,0))


        #exit button
        if exit_button.draw(screen):
            running = False

        if show_clothes:
            screen.blit(clicked_clothes, (0, 0)) #dress could be a def clothes_picker(chosen_clothes) ex.

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