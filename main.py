import pygame
import constants
from interface_drawer import PictureDrawer, ChosenPicture


pygame.init()

screen = pygame.display.set_mode((constants.WIDTH, constants.HEIGTH)) # TODO add full screen support
pygame.display.set_caption("Level creator")


clock = pygame.time.Clock()

pd = PictureDrawer(screen)
pd_group = pygame.sprite.Group()
pd_group.add(pd)

chosen_picture_square = ChosenPicture(constants.WIDTH // 2 - 20, 40, pd.exporter()[7])
chosen_picture_square_group = pygame.sprite.Group()
chosen_picture_square_group.add(chosen_picture_square)

running = True
while running:
    pressed = pygame.mouse.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if pressed[1]: #lmb
            pass # set chosen image to be drawn
        if pressed[2]:
            chosen_picture_square.state_setter()


    for p in pd_group:
        p.update()
        p.draw(screen)
    
    for cp in chosen_picture_square_group:
        cp.update()
        cp.draw(screen)


    # TODO draw grid placement
    # TODO solve picking image


    
    pygame.display.update()
    clock.tick(60)


