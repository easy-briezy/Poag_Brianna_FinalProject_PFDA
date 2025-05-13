#import pillow and pygame
from PIL import Image
import pygame



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

#hair images
curly = pygame.image.load('images/hair/curly_hair.png').convert_alpha()
straight = pygame.image.load('images/hair/straight_hair.png').convert_alpha()
thick = pygame.image.load('images/hair/thick_hair.png').convert_alpha()
wavy = pygame.image.load('images/hair/wavy_hair.png').convert_alpha()

#skin images
dark = pygame.image.load('images/skin/skin_d.png').convert_alpha()
medium = pygame.image.load('images/skin/skin_m.png').convert_alpha()
light = pygame.image.load('images/skin/skin_l.png').convert_alpha()





#clothes icons
overalls_icon =  pygame.image.load('images/icon/overalls _icon.png').convert_alpha()
sweater_icon = pygame.image.load('images/icon/sweater _icon.png').convert_alpha()

#hair icons
curly_icon = pygame.image.load('images/icon/c _icon.png').convert_alpha()
straight_icon = pygame.image.load('images/icon/s _icon.png').convert_alpha()
thick_icon = pygame.image.load('images/icon/t _icon.png').convert_alpha()
wavy_icon = pygame.image.load('images/icon/w _icon 2.png').convert_alpha()

#skin icons
dark_icon = pygame.image.load('images/icon/d_icon.png').convert_alpha()
medium_icon = pygame.image.load('images/icon/m _icon.png').convert_alpha()
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


#exit button
exit_button =  Button(32, 20, exit_image, 1)

#skin buttons
dark_button = Button(170, 450, dark_icon, 1)
medium_button = Button(300, 450, medium_icon, 1)
light_button = Button(430, 450, light_icon, 1)

#hair buttons
curly_button = Button(647, 135, curly_icon, 1)
wavy_button = Button(647, 240, wavy_icon, 1)
thick_button = Button(647, 345, thick_icon, 1)
straight_button = Button(647, 445, straight_icon, 1)

#clothes buttons
sweater_button = Button(50, 200, sweater_icon, 1)
overalls_button = Button(50, 300, overalls_icon, 1)


def music():
    pygame.mixer.init()

    pygame.mixer.music.load('music/game_song.mp3')

    #volume
    pygame.mixer.music.set_volume(0.4)

    song_playing = pygame.mixer.music.play(-1)

    return song_playing




def player_choice():
    choices = {
        "clicked_skin": None,
        "clicked_hair": None,
        "clicked_clothes": None,

        "show_skin": False,
        "show_hair": False,
        "show_clothes": False
        }

    #draw skin button icons
    if dark_button.draw(screen):
        choices["clicked_skin"] = dark
        choices["show_skin"] = True    
    if medium_button.draw(screen):
        choices["clicked_skin"] = medium
        choices["show_skin"] = True
    if light_button.draw(screen):
        choices["clicked_skin"] = light
        choices["show_skin"] = True

    #draw hair button icons
    if curly_button.draw(screen):
        choices["clicked_hair"] = curly
        choices["show_hair"] = True   
    if wavy_button.draw(screen):
        choices["clicked_hair"] = wavy
        choices["show_hair"] = True
    if thick_button.draw(screen):
        choices["clicked_hair"] = thick
        choices["show_hair"] = True
    if straight_button.draw(screen):
        choices["clicked_hair"] = straight
        choices["show_hair"] = True

    #draw clothes button icons onto screen
    if overalls_button.draw(screen):
        choices["clicked_clothes"] = overalls
        choices["show_clothes"] = True
    if sweater_button.draw(screen):
        choices["clicked_clothes"] = sweater
        choices["show_clothes"] = True

    return choices


def main():
    clicked_skin = None
    clicked_hair = None
    clicked_clothes = None
    show_skin = False
    show_hair = False
    show_clothes = False
    
    pygame.init()

    music()
    running = True
    #main loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        #base images
        screen.blit(base_image, (0,0))
        screen.blit(menu, (0,0))

        #call player choices function
        choice = player_choice()

        if choice["show_skin"]:
            clicked_skin = choice["clicked_skin"]
            show_skin = True

        if choice["show_hair"]:
            clicked_hair = choice["clicked_hair"]
            show_hair = True

        if choice["show_clothes"]:
            clicked_clothes = choice["clicked_clothes"]
            show_clothes = True 


        
        #load chosen player choice onto base image
        if show_skin:
            screen.blit(clicked_skin, (0, 0))
        if show_hair:
            screen.blit(clicked_hair, (0, 0))
        if show_clothes:
            screen.blit(clicked_clothes, (0, 0))


        #exit button
        if exit_button.draw(screen):
            running = False

        pygame.display.update()
    

    pygame.quit()





#call main
if __name__ == "__main__":
    main()